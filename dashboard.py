# app/dashboard.py

# Import required libraries
import streamlit as st                # For creating the web app
import pandas as pd                  # For data manipulation
import plotly.express as px          # For interactive visualizations

# Load the dataset using Streamlit's caching for performance
@st.cache_data
def load_data():
    # Load data from a CSV file stored in the 'data' folder
    df = pd.read_csv('data/civil_service_list.csv')
    return df

# Call the data loading function
df = load_data()

# -----------------------------
# Main App Layout Starts Here
# -----------------------------

# Set the page title
st.title("🧑‍⚖️ Who Gets Hired? NYC Civil Service Score Explorer")

# Add a sidebar for user interaction
st.sidebar.header("Filter Options")

# Dropdown for selecting job titles to include in the analysis
title_filter = st.sidebar.multiselect(
    "Filter by Job Title",
    options=df['List Title Desc'].unique(),      # All unique job titles
    default=df['List Title Desc'].unique()       # Default to all selected
)

# Dropdown for selecting agencies (e.g., NYPD, Sanitation, etc.)
agency_filter = st.sidebar.multiselect(
    "Filter by Agency",
    options=df['List Agency Desc'].dropna().unique(),  # Drop NaN agencies
    default=df['List Agency Desc'].dropna().unique()   # Default to all selected
)

# Apply filters to the original dataset based on sidebar selections
filtered_df = df[
    (df['List Title Desc'].isin(title_filter)) &
    (df['List Agency Desc'].isin(agency_filter))
]

# -----------------------------
# Score Distribution Section
# -----------------------------

# Add a subheader for score visualization
st.subheader("Score Distribution by Job Title")

# Create a box plot of Adjusted Final Averages (Adj. FA) per job title
fig = px.box(
    filtered_df,
    x='List Title Desc',
    y='Adj. FA',
    color='List Title Desc',        # Color-coded by title
    title="Adjusted Scores by Job Title"
)

# Display the plot in the app
st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Hiring Timeline Section
# -----------------------------

# Add a subheader for hiring timeline analysis
st.subheader("Hiring Timeline Overview")

# Ensure both date columns exist before proceeding
if 'Established Date' in df.columns and 'Published Date' in df.columns:

    # Create a copy to safely manipulate without affecting filtered_df
    timeline_df = filtered_df.copy()

    # Convert date strings to datetime objects
    timeline_df['Published Date'] = pd.to_datetime(timeline_df['Published Date'], errors='coerce')
    timeline_df['Established Date'] = pd.to_datetime(timeline_df['Established Date'], errors='coerce')

    # Calculate time delta (in days) between Published and Established dates
    timeline_df['Days to Establish'] = (timeline_df['Established Date'] - timeline_df['Published Date']).dt.days

    # Create a histogram to show the distribution of Days to Establish
    fig2 = px.histogram(
        timeline_df,
        x='Days to Establish',
        nbins=20,
        title="Days Between Publishing and Establishment"
    )

    # Display the timeline histogram
    st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# Raw Data Table
# -----------------------------

# Show a sample of the filtered dataset
st.subheader("Raw Dataset Preview")
st.dataframe(filtered_df.head(20))   # Display first 20 rows only

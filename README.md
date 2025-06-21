# Who Gets Hired? Score Trends in NYC Civil Service Exams

This project explores patterns and trends in civil service exam results across various NYC public sector jobs. By analyzing adjusted scores, agency codes, hiring dates, and eligibility credits, the project aims to reveal which factors most influence candidate placement and job assignment.

---

## 📊 Overview

New York City conducts open competitive exams for a wide range of municipal jobs—from sanitation workers to police officers. But how do scores translate into real job opportunities? This project investigates:

- Score distributions across job titles
- The relationship between credits (e.g., residency, veteran) and exam outcomes
- Time gaps between list publication, establishment, and expiration
- The most competitive and accessible job titles

---

## 🧾 Dataset Information

**Source:** NYC Civil Service List Data  
**Format:** CSV/Excel  
**Columns Include:**
- `Exam No`, `List No`, `First Name`, `Last Name`
- `Adj. FA` (Adjusted Final Average)
- `List Title Code`, `List Title Desc`
- `List Agency Code`, `List Agency Desc`
- `Published Date`, `Established Date`, `Anniversary Date`, `Extension Date`
- Credit Types: `Residency`, `Veteran`, `Parent`, `Sibling`

---

## 📌 Project Features

- 📈 Score distribution and trend visualizations by job title
- 🧮 Calculated average time from exam to hiring eligibility
- 🗂️ Breakdown of credits and their effect on final scores
- 🏢 Competitive vs. non-competitive agency comparisons
- ⏳ Timeline projections for list expiration and extension

---

## 📍 Visualizations

Key charts and visuals include:
- Bar plots of average scores per title
- Boxplots of score distribution by agency
- Timelines of hiring list milestones
- Heatmaps of credit impact

All visualizations are saved under `/charts`.

---

## 🔗 Complementary Datasets (Planned)

- NYC Government Payroll Data (for job salary analysis)
- NYC Open Data (demographics, hiring trends, exam announcements)
- SSA Baby Names Dataset (for fun first-name trend visualizations)

---

## 🚧 Future Work

- Build an interactive dashboard (Streamlit or Dash)
- Add predictive modeling for list eligibility and job offer likelihood
- Incorporate external datasets (e.g., payroll or census data)
- Create a chatbot for civil service hiring guidance

---

## 🛠️ Tech Stack

- Python (Pandas, NumPy, Matplotlib, Seaborn, Plotly)
- Jupyter Notebooks
- Git/GitHub
- Optional: Streamlit or Dash for interactive dashboards

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request with your improvements, ideas, or visualizations.

---

## 📄 License

MIT License


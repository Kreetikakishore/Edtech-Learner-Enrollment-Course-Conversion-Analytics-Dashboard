# 🎓 EdTech Enrollment & Engagement Analytics Dashboard

> A business intelligence case study designed to analyze learner demographics, enrollment behavior, and course engagement patterns on an online education platform using Python, Pandas, Plotly, and Streamlit.

---

## 📌 Executive Summary

Online education platforms generate large volumes of learner interaction data, but converting this raw data into actionable enrollment strategy requires structured analytics.

This project analyzes **10,000 learner enrollments** across demographic groups, course categories, pricing models, and skill levels to uncover:

- who the most active learners are,
- what courses drive the highest engagement,
- when enrollment peaks occur,
- and where strategic opportunities exist to improve learner retention and paid course adoption.

The final output is an interactive **Streamlit business dashboard** built for decision-makers to monitor learner participation and optimize platform growth.

---

## 🎯 Business Questions Addressed

This analytics case study was developed to answer the following key questions:

- Which learner age segment contributes the highest enrollment volume?
- Are users more inclined toward free courses or paid programs?
- Which course categories generate the strongest engagement?
- How balanced is participation across gender groups?
- Which skill level attracts the largest learner base?
- Are there identifiable monthly enrollment spikes?
- What strategic actions can improve conversion from casual learners to repeat users?

---

## 📊 Core KPI Snapshot

| KPI Metric | Value |
|------------|-------|
| Total Enrollments | 10,000 |
| Active Learners | 3,000 |
| Average Courses per Learner | 3.33 |
| Highest Contributing Age Group | 26–35 Years |
| Most Popular Category | Data Science |
| Most Enrolled Course | Deep Learning |
| Free Course Share | 64.03% |
| Gender Participation | 50.78% Female / 49.22% Male |
| Peak Enrollment Month | June |

---

## 🧠 Key Analytical Findings

### 1. Mid-Career Learners Dominate Platform Usage
Learners in the **26–35 age group account for nearly half of all enrollments**, indicating that working professionals and career-switchers form the platform’s most engaged user base.

### 2. Free Courses Act as Primary Acquisition Funnel
More than **64% of all enrollments are concentrated in free courses**, revealing strong price sensitivity and highlighting free offerings as a top-of-funnel learner acquisition strategy.

### 3. Data Science Leads Overall Course Demand
Among all categories, **Data Science records the highest enrollment count**, suggesting sustained demand for career-oriented technical upskilling.

### 4. Beginner-Level Programs Drive Highest Participation
The majority of users prefer beginner-friendly content, indicating that a large percentage of learners are entering new learning domains rather than pursuing advanced specialization.

### 5. June Shows Strong Seasonal Enrollment Spike
Enrollment volume peaks sharply in June, signaling a recurring opportunity for targeted promotional campaigns and certification pushes.

---

## 📈 Strategic Recommendations

Based on the observed learner behavior patterns, the following actions are recommended:

- **Use free beginner courses as conversion channels** into premium intermediate certification programs.
- **Target 26–35 year learners** with career advancement bundles, as they represent the strongest recurring audience.
- **Launch pre-June marketing campaigns** to capitalize on historical enrollment surges.
- **Expand high-demand Data Science and Programming tracks** with progressive paid pathways.
- **Introduce learner retention nudges** to increase the average courses-per-user metric beyond 3.33.

---

## 🗂️ Dataset Scope

The analysis was performed on a multi-sheet EdTech dataset consisting of learner, course, instructor, and transaction-level information.

| Dataset Table | Records | Description |
|---------------|---------|-------------|
| Users | 3,000 | Learner demographics and identities |
| Teachers | 60 | Instructor expertise and ratings |
| Courses | 60 | Category, level, pricing, duration |
| Transactions | 10,000 | Enrollment and payment records |

---

## 🧰 Technology Stack

| Tool | Role |
|------|------|
| Python | Core analytics programming |
| Pandas | Data cleaning & KPI generation |
| NumPy | Numerical computations |
| Plotly | Interactive visual analytics |
| Matplotlib / Seaborn | Exploratory chart generation |
| Streamlit | Executive dashboard deployment |
| OpenPyXL | Excel ingestion |

---

## 🖥️ Dashboard Modules

The final Streamlit dashboard includes:

- Executive KPI Overview
- Learner Demographic Segmentation
- Age vs Enrollment Analysis
- Gender Participation Trends
- Course Category Popularity
- Free vs Paid Course Preference
- Enrollment Heatmaps
- Monthly Trend Monitoring
- Raw Data Exploration with Filters

---

## 📸 Dashboard Preview

![Dashboard Screenshot](https://raw.githubusercontent.com/Kreetikakishore/edtech-enrollment-engagement-dashboard/main/assets/dashboard.png)

## 🚀 Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://kreetikakishore-edtech-enrollment-engagement-dashboa-app-3iz12v.streamlit.app/)


## 📁 Repository Structure

```bash
edtech-enrollment-engagement-dashboard/
│
├── data/
│   ├── EduPro Online Platform (1).xlsx
│   ├── users_cleaned.csv
│   ├── master.csv
│   └── KPI_Summary.csv
│
├── charts/
│   └── static_visualizations/
│
├── analysis.py
├── charts.py
├── app.py
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run the Dashboard

### 1. Clone Repository

```bash
git clone https://github.com/your-username/edtech-enrollment-engagement-dashboard.git
cd edtech-enrollment-engagement-dashboard
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Launch Streamlit App

```bash
python -m streamlit run app.py
```

### 4. Open Browser

```bash
http://localhost:8501
```

---

## 📌 Deliverables Produced

- Cleaned and merged learner analytics dataset
- KPI summary file
- Static EDA visualizations
- Interactive executive dashboard
- Strategic business recommendations

---

## ⚠️ Note

This project was developed as a data analytics portfolio case study to demonstrate learner behavior intelligence, KPI dashboarding, and business recommendation generation in the EdTech domain.

---

## 👤 Author

**Kreetika Kishore**  
Data Analytics Portfolio Project | 2026

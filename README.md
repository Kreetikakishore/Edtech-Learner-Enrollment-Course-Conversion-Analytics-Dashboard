# 🎓 EdTech Enrollment & Engagement Dashboard

![Python](https://img.shields.io/badge/Python-3.11-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red) ![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green) ![Plotly](https://img.shields.io/badge/Plotly-Visualizations-orange)

## 📋 Project Overview

This project provides a comprehensive demographic and behavioral analysis of learners on the **EduPro** online learning platform. Built for the **Toronto Government Parks, Forestry & Recreation**, it uncovers enrollment patterns across age groups, gender, course categories, and skill levels to help decision-makers design data-driven education strategies.

---

## 🎯 Key Findings

| Metric | Value |
|---|---|
| Total Enrollments | 10,000 |
| Active Learners | 3,000 |
| Avg Courses per Learner | 3.33 |
| Top Age Group | 26–35 (48% of enrollments) |
| Top Course Category | Data Science (916 enrollments) |
| Top Course | Deep Learning |
| Free Course Popularity | 64.03% |
| Gender Balance | 50.78% Female / 49.22% Male |
| Peak Enrollment Month | June (899 enrollments) |

---

## 📁 Project Structure

```
edupro_project/
├── data/
│   ├── EduPro Online Platform (1).xlsx    # Original dataset
│   ├── users_cleaned.csv                  # Cleaned users data
│   ├── master.csv                         # Merged master dataset
│   └── KPI_Summary.csv                    # All KPIs saved
├── charts/
│   ├── 01_age_distribution.png
│   ├── 02_enrollments_by_age.png
│   ├── 03_gender_distribution.png
│   ├── 04_category_popularity.png
│   ├── 05_course_type.png
│   ├── 06_course_level.png
│   ├── 07_heatmap_age_category.png
│   ├── 08_gender_vs_category.png
│   ├── 09_gender_vs_level.png
│   ├── 10_age_vs_level.png
│   ├── 11_top_courses.png
│   ├── 12_monthly_trend.png
│   └── 13_payment_methods.png
├── analysis.py                            # EDA & KPI calculations
├── charts.py                              # Static chart generation
├── app.py                                 # Streamlit dashboard
├── requirements.txt
└── README.md
```

---

## 🗂️ Dataset Description

| Sheet | Rows | Description |
|---|---|---|
| Users | 3,000 | UserID, UserName, Age, Gender, Email |
| Teachers | 60 | TeacherID, Name, Expertise, Experience, Rating |
| Courses | 60 | CourseID, Name, Category, Type, Level, Price, Duration, Rating |
| Transactions | 10,000 | TransactionID, UserID, CourseID, Date, Amount, PaymentMethod |

---

## 📊 Segments Analyzed

| Segment | Groups |
|---|---|
| Age Group | Under 18 / 18–25 / 26–35 |
| Course Type | Free / Paid |
| Course Level | Beginner / Intermediate / Advanced |
| Course Category | 12 categories including Data Science, Programming, Finance etc. |

---

## 📈 KPIs Tracked

- **Total Enrollments** — Platform engagement indicator
- **Enrollments by Age Group** — Demographic reach
- **Gender Participation Ratio** — Inclusivity metric
- **Category Popularity Index** — Course demand
- **Level Preference Distribution** — Skill maturity insight

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Kreetikakishore/edupro-analytics.git
cd edupro_project
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the analysis
```bash
python analysis.py
```

### 4. Generate charts
```bash
python charts.py
```

### 5. Launch the dashboard
```bash
python -m streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 🖥️ Dashboard Features

| Module | Description |
|---|---|
| Platform Overview | 5 live KPI cards updating with filters |
| Learner Demographics | Age group and gender distribution charts |
| Age-wise Enrollment | Age vs course level and category analysis |
| Gender Preferences | Gender vs category and level comparisons |
| Category Popularity | Horizontal bar chart and free vs paid split |
| Enrollment Heatmaps | Age x Category and Gender x Level heatmaps |
| Monthly Trends | Line chart of enrollment trends + top 10 courses |
| Raw Data Explorer | Filterable table of all 10,000 enrollments |

### Sidebar Filters
- Age Group (Under 18 / 18–25 / 26–35)
- Gender (Male / Female)
- Course Category (all 12 categories)
- Course Level (Beginner / Intermediate / Advanced)

---

## 🔍 Key Insights

1. **26–35 age group dominates** with 48% of all enrollments — the most active learner segment
2. **Data Science is the most popular category** with 916 enrollments across all demographics
3. **Free courses account for 64%** of all enrollments — price sensitivity is high among learners
4. **Gender is nearly balanced** at 50.78% Female vs 49.22% Male — strong platform inclusivity
5. **Beginner level is most popular** — most learners are starting their learning journey
6. **June is the peak enrollment month** with 899 enrollments — seasonal pattern worth leveraging
7. **Average 3.33 courses per learner** — moderate engagement with room to grow

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.11 | Core programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical calculations |
| Matplotlib | Static chart generation |
| Seaborn | Statistical visualizations |
| Plotly | Interactive dashboard charts |
| Streamlit | Web dashboard framework |
| OpenPyXL | Excel file reading |

---

## 📄 Deliverables

- ✅ Cleaned and merged master dataset
- ✅ 13 static visualizations
- ✅ KPI summary CSV
- ✅ Interactive Streamlit dashboard
- ✅ Research paper with insights and recommendations

---

## 👤 Author

**Kreetika**
Toronto Government — Parks, Forestry & Recreation | EduPro Learner Analytics Project
2026

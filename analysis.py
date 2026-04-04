# =============================================
# PHASE 2 - Understanding the Dataset
# =============================================

import pandas as pd
import numpy as np

# ── Load all sheets ───────────────────────────
FILE = 'data/EduPro Online Platform (1).xlsx'

users        = pd.read_excel(FILE, sheet_name='Users')
teachers     = pd.read_excel(FILE, sheet_name='Teachers')
courses      = pd.read_excel(FILE, sheet_name='Courses')
transactions = pd.read_excel(FILE, sheet_name='Transactions')

# ── Shape of each sheet ───────────────────────
print("=" * 50)
print("SHAPE OF EACH SHEET")
print("=" * 50)
print(f"Users        : {users.shape[0]} rows x {users.shape[1]} cols")
print(f"Teachers     : {teachers.shape[0]} rows x {teachers.shape[1]} cols")
print(f"Courses      : {courses.shape[0]} rows x {courses.shape[1]} cols")
print(f"Transactions : {transactions.shape[0]} rows x {transactions.shape[1]} cols")

# ── Column names ──────────────────────────────
print("\n" + "=" * 50)
print("COLUMN NAMES")
print("=" * 50)
print(f"Users        : {list(users.columns)}")
print(f"Teachers     : {list(teachers.columns)}")
print(f"Courses      : {list(courses.columns)}")
print(f"Transactions : {list(transactions.columns)}")

# ── First 5 rows of each ──────────────────────
print("\n" + "=" * 50)
print("USERS — FIRST 5 ROWS")
print("=" * 50)
print(users.head())

print("\n" + "=" * 50)
print("COURSES — FIRST 5 ROWS")
print("=" * 50)
print(courses.head())

print("\n" + "=" * 50)
print("TRANSACTIONS — FIRST 5 ROWS")
print("=" * 50)
print(transactions.head())

# ── Missing values ────────────────────────────
print("\n" + "=" * 50)
print("MISSING VALUES")
print("=" * 50)
print("\nUsers:")
print(users.isnull().sum())
print("\nCourses:")
print(courses.isnull().sum())
print("\nTransactions:")
print(transactions.isnull().sum())

# ── Unique values in key columns ──────────────
print("\n" + "=" * 50)
print("UNIQUE VALUES IN KEY COLUMNS")
print("=" * 50)
print(f"Gender (Users)    : {users['Gender'].unique()}")
print(f"CourseCategory    : {courses['CourseCategory'].unique()}")
print(f"CourseType        : {courses['CourseType'].unique()}")
print(f"CourseLevel       : {courses['CourseLevel'].unique()}")
print(f"PaymentMethod     : {transactions['PaymentMethod'].unique()}")

# ── Basic statistics ──────────────────────────
print("\n" + "=" * 50)
print("AGE STATISTICS — USERS")
print("=" * 50)
print(users['Age'].describe())

print("\n" + "=" * 50)
print("GENDER DISTRIBUTION — USERS")
print("=" * 50)
print(users['Gender'].value_counts())

print("\n" + "=" * 50)
print("COURSE CATEGORY DISTRIBUTION")
print("=" * 50)
print(courses['CourseCategory'].value_counts())

print("\n" + "=" * 50)
print("COURSE LEVEL DISTRIBUTION")
print("=" * 50)
print(courses['CourseLevel'].value_counts())


# =============================================
# PHASE 3 - Data Cleaning & Preparation
# =============================================

import pandas as pd
import numpy as np

# ── Reload all sheets ─────────────────────────
FILE = 'data/EduPro Online Platform (1).xlsx'

users        = pd.read_excel(FILE, sheet_name='Users')
teachers     = pd.read_excel(FILE, sheet_name='Teachers')
courses      = pd.read_excel(FILE, sheet_name='Courses')
transactions = pd.read_excel(FILE, sheet_name='Transactions')

# ── Step 1: Drop non-analytical columns ───────
users    = users.drop(columns=['Email'])
print("=" * 50)
print("COLUMNS AFTER CLEANING — USERS")
print("=" * 50)
print(users.columns.tolist())

# ── Step 2: Fix data types ────────────────────
transactions['TransactionDate'] = pd.to_datetime(transactions['TransactionDate'])
transactions['Month'] = transactions['TransactionDate'].dt.month
transactions['Year']  = transactions['TransactionDate'].dt.year

print("\n" + "=" * 50)
print("TRANSACTION DATE TYPES")
print("=" * 50)
print(transactions.dtypes)

# ── Step 3: Create Age Groups ─────────────────
users['AgeGroup'] = pd.cut(
    users['Age'],
    bins=[14, 17, 25, 35],
    labels=['<18', '18-25', '26-35']
)

print("\n" + "=" * 50)
print("AGE GROUP DISTRIBUTION")
print("=" * 50)
print(users['AgeGroup'].value_counts().sort_index())

# ── Step 4: Merge all sheets into master df ───
# Users + Transactions
master = transactions.merge(users, on='UserID', how='left')
# Add Courses
master = master.merge(courses, on='CourseID', how='left')

print("\n" + "=" * 50)
print("MASTER DATAFRAME SHAPE")
print("=" * 50)
print(f"Rows    : {master.shape[0]}")
print(f"Columns : {master.shape[1]}")
print(f"Columns : {list(master.columns)}")

# ── Step 5: Verify no nulls in master ─────────
print("\n" + "=" * 50)
print("MISSING VALUES IN MASTER DF")
print("=" * 50)
print(master.isnull().sum())

# ── Step 6: Save cleaned files ────────────────
users.to_csv('data/users_cleaned.csv', index=False)
master.to_csv('data/master.csv', index=False)

print("\n" + "=" * 50)
print("FILES SAVED")
print("=" * 50)
print("users_cleaned.csv → data/")
print("master.csv        → data/")
print(f"Master shape      : {master.shape[0]} rows x {master.shape[1]} cols")

# =============================================
# PHASE 4 - Exploratory Data Analysis (EDA)
# =============================================

import pandas as pd
import numpy as np

# ── Load master dataset ───────────────────────
master = pd.read_csv('data/master.csv')

print("=" * 50)
print("1. TOTAL ENROLLMENTS")
print("=" * 50)
print(f"Total Enrollments : {len(master)}")
print(f"Unique Users      : {master['UserID'].nunique()}")
print(f"Unique Courses    : {master['CourseID'].nunique()}")
avg_courses = round(len(master) / master['UserID'].nunique(), 2)
print(f"Avg Courses/User  : {avg_courses}")

# ── Age Group Analysis ────────────────────────
print("\n" + "=" * 50)
print("2. ENROLLMENTS BY AGE GROUP")
print("=" * 50)
age_enroll = master.groupby('AgeGroup').size().reset_index(name='Enrollments')
print(age_enroll)

# ── Gender Analysis ───────────────────────────
print("\n" + "=" * 50)
print("3. ENROLLMENTS BY GENDER")
print("=" * 50)
gender_enroll = master.groupby('Gender').size().reset_index(name='Enrollments')
gender_enroll['Percentage'] = (gender_enroll['Enrollments'] / len(master) * 100).round(2)
print(gender_enroll)

# ── Course Category Analysis ──────────────────
print("\n" + "=" * 50)
print("4. ENROLLMENTS BY COURSE CATEGORY")
print("=" * 50)
cat_enroll = master.groupby('CourseCategory').size().reset_index(name='Enrollments')
cat_enroll = cat_enroll.sort_values('Enrollments', ascending=False)
print(cat_enroll)

# ── Course Type Analysis ──────────────────────
print("\n" + "=" * 50)
print("5. ENROLLMENTS BY COURSE TYPE")
print("=" * 50)
type_enroll = master.groupby('CourseType').size().reset_index(name='Enrollments')
type_enroll['Percentage'] = (type_enroll['Enrollments'] / len(master) * 100).round(2)
print(type_enroll)

# ── Course Level Analysis ─────────────────────
print("\n" + "=" * 50)
print("6. ENROLLMENTS BY COURSE LEVEL")
print("=" * 50)
level_enroll = master.groupby('CourseLevel').size().reset_index(name='Enrollments')
level_enroll['Percentage'] = (level_enroll['Enrollments'] / len(master) * 100).round(2)
print(level_enroll)

# ── Age Group x Course Category ───────────────
print("\n" + "=" * 50)
print("7. AGE GROUP x COURSE CATEGORY")
print("=" * 50)
age_cat = master.groupby(['AgeGroup', 'CourseCategory']).size().reset_index(name='Enrollments')
age_cat = age_cat.sort_values(['AgeGroup', 'Enrollments'], ascending=[True, False])
print(age_cat)

# ── Gender x Course Category ──────────────────
print("\n" + "=" * 50)
print("8. GENDER x COURSE CATEGORY")
print("=" * 50)
gender_cat = master.groupby(['Gender', 'CourseCategory']).size().reset_index(name='Enrollments')
gender_cat = gender_cat.sort_values(['Gender', 'Enrollments'], ascending=[True, False])
print(gender_cat)

# ── Gender x Course Level ─────────────────────
print("\n" + "=" * 50)
print("9. GENDER x COURSE LEVEL")
print("=" * 50)
gender_level = master.groupby(['Gender', 'CourseLevel']).size().reset_index(name='Enrollments')
print(gender_level)

# ── Age Group x Course Level ──────────────────
print("\n" + "=" * 50)
print("10. AGE GROUP x COURSE LEVEL")
print("=" * 50)
age_level = master.groupby(['AgeGroup', 'CourseLevel']).size().reset_index(name='Enrollments')
print(age_level)

# ── Most Popular Courses ──────────────────────
print("\n" + "=" * 50)
print("11. TOP 10 MOST ENROLLED COURSES")
print("=" * 50)
top_courses = master.groupby(['CourseName', 'CourseCategory']).size().reset_index(name='Enrollments')
top_courses = top_courses.sort_values('Enrollments', ascending=False).head(10)
print(top_courses)

# ── Payment Method Distribution ───────────────
print("\n" + "=" * 50)
print("12. PAYMENT METHOD DISTRIBUTION")
print("=" * 50)
payment = master.groupby('PaymentMethod').size().reset_index(name='Enrollments')
payment['Percentage'] = (payment['Enrollments'] / len(master) * 100).round(2)
print(payment)

# ── Monthly Enrollment Trend ──────────────────
print("\n" + "=" * 50)
print("13. MONTHLY ENROLLMENT TREND")
print("=" * 50)
monthly = master.groupby('Month').size().reset_index(name='Enrollments')
monthly['Month_Name'] = pd.to_datetime(monthly['Month'], format='%m').dt.strftime('%b')
print(monthly)

# ── Active Users (top enrollers) ─────────────
print("\n" + "=" * 50)
print("14. USER ENROLLMENT CONCENTRATION")
print("=" * 50)
user_enroll = master.groupby('UserID').size().reset_index(name='Enrollments')
print(f"Min enrollments per user  : {user_enroll['Enrollments'].min()}")
print(f"Max enrollments per user  : {user_enroll['Enrollments'].max()}")
print(f"Avg enrollments per user  : {user_enroll['Enrollments'].mean().round(2)}")
print(f"Users with 1 enrollment   : {len(user_enroll[user_enroll['Enrollments'] == 1])}")
print(f"Users with 5+ enrollments : {len(user_enroll[user_enroll['Enrollments'] >= 5])}")

# =============================================
# PHASE 5 - KPI Calculations
# =============================================

import pandas as pd
import numpy as np

# ── Load data ─────────────────────────────────
master = pd.read_csv('data/master.csv')
users  = pd.read_csv('data/users_cleaned.csv')

print("=" * 50)
print("KPI 1 — TOTAL ENROLLMENTS")
print("=" * 50)
total_enrollments = len(master)
unique_users      = master['UserID'].nunique()
unique_courses    = master['CourseID'].nunique()
avg_per_user      = round(total_enrollments / unique_users, 2)
print(f"Total Enrollments     : {total_enrollments}")
print(f"Unique Active Users   : {unique_users}")
print(f"Unique Courses Taken  : {unique_courses}")
print(f"Avg Enrollments/User  : {avg_per_user}")

print("\n" + "=" * 50)
print("KPI 2 — ENROLLMENTS BY AGE GROUP")
print("=" * 50)
age_kpi = master.groupby('AgeGroup').size().reset_index(name='Enrollments')
age_kpi['Percentage'] = (age_kpi['Enrollments'] / total_enrollments * 100).round(2)
age_kpi['Avg per User'] = (age_kpi['Enrollments'] /
    master.groupby('AgeGroup')['UserID'].nunique().values).round(2)
print(age_kpi)

print("\n" + "=" * 50)
print("KPI 3 — GENDER PARTICIPATION RATIO")
print("=" * 50)
gender_kpi = master.groupby('Gender').agg(
    Enrollments=('TransactionID', 'count'),
    Unique_Users=('UserID', 'nunique')
).reset_index()
gender_kpi['Enrollment %']   = (gender_kpi['Enrollments'] / total_enrollments * 100).round(2)
gender_kpi['Avg per User']   = (gender_kpi['Enrollments'] / gender_kpi['Unique_Users']).round(2)
print(gender_kpi)

print("\n" + "=" * 50)
print("KPI 4 — CATEGORY POPULARITY INDEX")
print("=" * 50)
cat_kpi = master.groupby('CourseCategory').size().reset_index(name='Enrollments')
cat_kpi['Popularity Index'] = (cat_kpi['Enrollments'] / cat_kpi['Enrollments'].max() * 100).round(2)
cat_kpi = cat_kpi.sort_values('Enrollments', ascending=False)
print(cat_kpi)

print("\n" + "=" * 50)
print("KPI 5 — LEVEL PREFERENCE DISTRIBUTION")
print("=" * 50)
level_kpi = master.groupby(['AgeGroup', 'CourseLevel']).size().reset_index(name='Enrollments')
level_pct = level_kpi.copy()
totals    = level_pct.groupby('AgeGroup')['Enrollments'].transform('sum')
level_pct['Percentage'] = (level_pct['Enrollments'] / totals * 100).round(2)
print(level_pct)

print("\n" + "=" * 50)
print("KPI SUMMARY DASHBOARD")
print("=" * 50)
top_cat    = master['CourseCategory'].value_counts().index[0]
top_course = master['CourseName'].value_counts().index[0]
top_age    = master['AgeGroup'].value_counts().index[0]
free_pct   = round(len(master[master['CourseType'] == 'Free']) / total_enrollments * 100, 2)
print(f"""
┌─────────────────────────────────────────────┐
│         EDUPRO PLATFORM KPI SUMMARY         │
├─────────────────────────────────────────────┤
│  Total Enrollments      : {total_enrollments}              │
│  Active Users           : {unique_users}               │
│  Avg Courses per User   : {avg_per_user}               │
│  Top Age Group          : {top_age} (48%)          │
│  Top Course Category    : {top_cat}      │
│  Top Course             : {top_course[:25]}  │
│  Free Course Popularity : {free_pct}%            │
│  Gender Balance         : 50.78% F / 49.22% M│
│  Peak Month             : June (899 enrollments)│
└─────────────────────────────────────────────┘
""")

# ── Save KPI Summary ──────────────────────────
kpi_data = {
    'KPI': [
        'Total Enrollments',
        'Unique Active Users',
        'Avg Enrollments per User',
        'Top Age Group',
        'Top Course Category',
        'Top Course',
        'Free Course %',
        'Paid Course %',
        'Female Enrollment %',
        'Male Enrollment %',
        'Peak Month',
        'Beginner Level %',
        'Intermediate Level %',
        'Advanced Level %',
    ],
    'Value': [
        total_enrollments,
        unique_users,
        avg_per_user,
        '26-35 (48%)',
        top_cat,
        top_course,
        f'{free_pct}%',
        f'{round(100 - free_pct, 2)}%',
        '50.78%',
        '49.22%',
        'June (899)',
        '35.73%',
        '29.52%',
        '34.75%',
    ]
}
kpi_df = pd.DataFrame(kpi_data)
kpi_df.to_csv('data/KPI_Summary.csv', index=False)
print("KPI Summary saved to: data/KPI_Summary.csv")
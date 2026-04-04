# =============================================
# PHASE 6 - Visualizations
# =============================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import os

# ── Load data ─────────────────────────────────
master = pd.read_csv('data/master.csv')
users  = pd.read_csv('data/users_cleaned.csv')

# ── Create charts folder ──────────────────────
os.makedirs('charts', exist_ok=True)

# ── Global style ──────────────────────────────
sns.set_theme(style='whitegrid')
COLORS  = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12',
           '#9b59b6', '#1abc9c', '#e67e22', '#34495e',
           '#e91e8c', '#00bcd4', '#ff5722', '#607d8b']

print("Building charts... please wait")

# ─────────────────────────────────────────────
# CHART 1 — Age Distribution of Users (Histogram)
# ─────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 5))
ax.hist(users['Age'], bins=20, color='#3498db',
        edgecolor='white', linewidth=0.8)
ax.set_title('Age Distribution of Learners', fontsize=16, fontweight='bold')
ax.set_xlabel('Age', fontsize=12)
ax.set_ylabel('Number of Users', fontsize=12)
ax.axvline(users['Age'].mean(), color='red', linestyle='--',
           linewidth=1.5, label=f"Mean Age: {users['Age'].mean():.1f}")
ax.legend(fontsize=11)
plt.tight_layout()
plt.savefig('charts/01_age_distribution.png', dpi=150)
plt.close()
print("Chart 1 done — Age Distribution")

# ─────────────────────────────────────────────
# CHART 2 — Age Group Enrollments (Bar)
# ─────────────────────────────────────────────
age_order = ['<18', '18-25', '26-35']
age_enroll = master.groupby('AgeGroup').size().reindex(age_order)
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(age_enroll.index, age_enroll.values,
              color=['#e74c3c', '#3498db', '#2ecc71'],
              edgecolor='white', width=0.5)
for bar, val in zip(bars, age_enroll.values):
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 30,
            f'{val:,}', ha='center',
            fontsize=12, fontweight='bold')
ax.set_title('Enrollments by Age Group', fontsize=16, fontweight='bold')
ax.set_ylabel('Number of Enrollments', fontsize=12)
ax.set_xlabel('Age Group', fontsize=12)
ax.set_ylim(0, 5500)
plt.tight_layout()
plt.savefig('charts/02_enrollments_by_age.png', dpi=150)
plt.close()
print("Chart 2 done — Enrollments by Age Group")

# ─────────────────────────────────────────────
# CHART 3 — Gender Distribution (Pie)
# ─────────────────────────────────────────────
gender_counts = users['Gender'].value_counts()
fig, ax = plt.subplots(figsize=(7, 7))
ax.pie(gender_counts, labels=gender_counts.index,
       colors=['#e91e8c', '#3498db'],
       autopct='%1.1f%%', startangle=90,
       textprops={'fontsize': 13})
ax.set_title('Gender Distribution of Learners',
             fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('charts/03_gender_distribution.png', dpi=150)
plt.close()
print("Chart 3 done — Gender Distribution")

# ─────────────────────────────────────────────
# CHART 4 — Course Category Popularity (Horizontal Bar)
# ─────────────────────────────────────────────
cat_enroll = master.groupby('CourseCategory').size().sort_values()
fig, ax = plt.subplots(figsize=(10, 7))
bars = ax.barh(cat_enroll.index, cat_enroll.values,
               color='#3498db', edgecolor='white')
for bar, val in zip(bars, cat_enroll.values):
    ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2,
            f'{val:,}', va='center', fontsize=10, fontweight='bold')
ax.set_title('Course Category Popularity', fontsize=16, fontweight='bold')
ax.set_xlabel('Number of Enrollments', fontsize=12)
ax.set_xlim(0, 1050)
plt.tight_layout()
plt.savefig('charts/04_category_popularity.png', dpi=150)
plt.close()
print("Chart 4 done — Category Popularity")

# ─────────────────────────────────────────────
# CHART 5 — Course Type Distribution (Pie)
# ─────────────────────────────────────────────
type_counts = master['CourseType'].value_counts()
fig, ax = plt.subplots(figsize=(7, 7))
ax.pie(type_counts, labels=type_counts.index,
       colors=['#2ecc71', '#e74c3c'],
       autopct='%1.1f%%', startangle=90,
       textprops={'fontsize': 13})
ax.set_title('Free vs Paid Course Enrollments',
             fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('charts/05_course_type.png', dpi=150)
plt.close()
print("Chart 5 done — Course Type Distribution")

# ─────────────────────────────────────────────
# CHART 6 — Course Level Distribution (Bar)
# ─────────────────────────────────────────────
level_order = ['Beginner', 'Intermediate', 'Advanced']
level_enroll = master.groupby('CourseLevel').size().reindex(level_order)
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(level_enroll.index, level_enroll.values,
              color=['#2ecc71', '#f39c12', '#e74c3c'],
              edgecolor='white', width=0.5)
for bar, val in zip(bars, level_enroll.values):
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 20,
            f'{val:,}', ha='center',
            fontsize=12, fontweight='bold')
ax.set_title('Enrollments by Course Level', fontsize=16, fontweight='bold')
ax.set_ylabel('Number of Enrollments', fontsize=12)
ax.set_xlabel('Course Level', fontsize=12)
ax.set_ylim(0, 4200)
plt.tight_layout()
plt.savefig('charts/06_course_level.png', dpi=150)
plt.close()
print("Chart 6 done — Course Level Distribution")

# ─────────────────────────────────────────────
# CHART 7 — Heatmap: Age Group x Course Category
# ─────────────────────────────────────────────
age_cat_pivot = master.pivot_table(
    values='TransactionID', index='AgeGroup',
    columns='CourseCategory', aggfunc='count'
)
age_cat_pivot = age_cat_pivot.reindex(['<18', '18-25', '26-35'])
fig, ax = plt.subplots(figsize=(14, 5))
sns.heatmap(age_cat_pivot, annot=True, fmt='.0f',
            cmap='YlOrRd', linewidths=0.5,
            linecolor='white', ax=ax,
            annot_kws={'size': 10, 'weight': 'bold'},
            cbar_kws={'label': 'Enrollments'})
ax.set_title('Enrollments Heatmap: Age Group x Course Category',
             fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Course Category', fontsize=12)
ax.set_ylabel('Age Group', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('charts/07_heatmap_age_category.png', dpi=150)
plt.close()
print("Chart 7 done — Heatmap Age x Category")

# ─────────────────────────────────────────────
# CHART 8 — Gender x Course Category (Grouped Bar)
# ─────────────────────────────────────────────
gender_cat = master.groupby(['CourseCategory', 'Gender']).size().unstack()
fig, ax = plt.subplots(figsize=(13, 6))
gender_cat.plot(kind='bar', ax=ax,
                color=['#e91e8c', '#3498db'],
                edgecolor='white', width=0.7)
ax.set_title('Gender vs Course Category Enrollments',
             fontsize=16, fontweight='bold')
ax.set_ylabel('Enrollments', fontsize=12)
ax.set_xlabel('Course Category', fontsize=12)
ax.legend(['Female', 'Male'], fontsize=11)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('charts/08_gender_vs_category.png', dpi=150)
plt.close()
print("Chart 8 done — Gender vs Category")

# ─────────────────────────────────────────────
# CHART 9 — Gender x Course Level (Grouped Bar)
# ─────────────────────────────────────────────
gender_level = master.groupby(['CourseLevel', 'Gender']).size().unstack()
gender_level = gender_level.reindex(['Beginner', 'Intermediate', 'Advanced'])
fig, ax = plt.subplots(figsize=(9, 5))
gender_level.plot(kind='bar', ax=ax,
                  color=['#e91e8c', '#3498db'],
                  edgecolor='white', width=0.6)
ax.set_title('Gender vs Course Level Enrollments',
             fontsize=16, fontweight='bold')
ax.set_ylabel('Enrollments', fontsize=12)
ax.set_xlabel('Course Level', fontsize=12)
ax.legend(['Female', 'Male'], fontsize=11)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('charts/09_gender_vs_level.png', dpi=150)
plt.close()
print("Chart 9 done — Gender vs Level")

# ─────────────────────────────────────────────
# CHART 10 — Age Group x Course Level (Grouped Bar)
# ─────────────────────────────────────────────
age_level = master.groupby(['CourseLevel', 'AgeGroup']).size().unstack()
age_level = age_level.reindex(['Beginner', 'Intermediate', 'Advanced'])
fig, ax = plt.subplots(figsize=(10, 5))
age_level.plot(kind='bar', ax=ax,
               color=['#e74c3c', '#3498db', '#2ecc71'],
               edgecolor='white', width=0.6)
ax.set_title('Age Group vs Course Level Enrollments',
             fontsize=16, fontweight='bold')
ax.set_ylabel('Enrollments', fontsize=12)
ax.set_xlabel('Course Level', fontsize=12)
ax.legend(['<18', '18-25', '26-35'], fontsize=11)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('charts/10_age_vs_level.png', dpi=150)
plt.close()
print("Chart 10 done — Age vs Level")

# ─────────────────────────────────────────────
# CHART 11 — Top 10 Most Enrolled Courses (Bar)
# ─────────────────────────────────────────────
top_courses = master.groupby('CourseName').size().sort_values(
    ascending=False).head(10)
fig, ax = plt.subplots(figsize=(11, 6))
bars = ax.barh(top_courses.index[::-1],
               top_courses.values[::-1],
               color='#9b59b6', edgecolor='white')
for bar, val in zip(bars, top_courses.values[::-1]):
    ax.text(bar.get_width() + 1,
            bar.get_y() + bar.get_height()/2,
            f'{val}', va='center',
            fontsize=10, fontweight='bold')
ax.set_title('Top 10 Most Enrolled Courses',
             fontsize=16, fontweight='bold')
ax.set_xlabel('Number of Enrollments', fontsize=12)
ax.set_xlim(0, 220)
plt.tight_layout()
plt.savefig('charts/11_top_courses.png', dpi=150)
plt.close()
print("Chart 11 done — Top 10 Courses")

# ─────────────────────────────────────────────
# CHART 12 — Monthly Enrollment Trend (Line)
# ─────────────────────────────────────────────
monthly = master.groupby('Month').size().reset_index(name='Enrollments')
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
fig, ax = plt.subplots(figsize=(11, 5))
ax.plot(month_names, monthly['Enrollments'],
        color='#3498db', linewidth=2.5,
        marker='o', markersize=7,
        markerfacecolor='#e74c3c')
ax.fill_between(month_names, monthly['Enrollments'],
                alpha=0.1, color='#3498db')
for i, val in enumerate(monthly['Enrollments']):
    ax.text(i, val + 10, str(val),
            ha='center', fontsize=9, fontweight='bold')
ax.set_title('Monthly Enrollment Trend',
             fontsize=16, fontweight='bold')
ax.set_ylabel('Number of Enrollments', fontsize=12)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylim(700, 980)
plt.tight_layout()
plt.savefig('charts/12_monthly_trend.png', dpi=150)
plt.close()
print("Chart 12 done — Monthly Trend")

# ─────────────────────────────────────────────
# CHART 13 — Payment Method Distribution (Pie)
# ─────────────────────────────────────────────
payment = master['PaymentMethod'].value_counts()
fig, ax = plt.subplots(figsize=(7, 7))
ax.pie(payment, labels=payment.index,
       colors=['#3498db', '#2ecc71', '#f39c12'],
       autopct='%1.1f%%', startangle=90,
       textprops={'fontsize': 13})
ax.set_title('Payment Method Distribution',
             fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('charts/13_payment_methods.png', dpi=150)
plt.close()
print("Chart 13 done — Payment Methods")

print("\n" + "=" * 50)
print("ALL 13 CHARTS SAVED TO charts/ FOLDER")
print("=" * 50)
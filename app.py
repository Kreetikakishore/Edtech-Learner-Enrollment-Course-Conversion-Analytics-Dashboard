# =============================================
# PHASE 7 - Streamlit Dashboard
# =============================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ── Page Configuration ────────────────────────
st.set_page_config(
    page_title="EdTech Enrollment & Engagement Analytics Dashboard",
    page_icon="🎓",
    layout="wide"
)

# ── Load Data ─────────────────────────────────
@st.cache_data
def load_data():
    master = pd.read_csv('data/master.csv')
    users  = pd.read_csv('data/users_cleaned.csv')
    return master, users

master, users = load_data()

# ── Sidebar ───────────────────────────────────
st.sidebar.image("https://img.icons8.com/color/96/graduation-cap.png", width=80)
st.sidebar.title("🎓 EduPro Analytics")
st.sidebar.markdown("---")
st.sidebar.header("Filters")

age_order = ['<18', '18-25', '26-35']
selected_age = st.sidebar.multiselect(
    "Select Age Group",
    options=age_order,
    default=age_order
)

selected_gender = st.sidebar.multiselect(
    "Select Gender",
    options=master['Gender'].unique(),
    default=master['Gender'].unique()
)

selected_cat = st.sidebar.multiselect(
    "Select Course Category",
    options=sorted(master['CourseCategory'].unique()),
    default=sorted(master['CourseCategory'].unique())
)

selected_level = st.sidebar.multiselect(
    "Select Course Level",
    options=['Beginner', 'Intermediate', 'Advanced'],
    default=['Beginner', 'Intermediate', 'Advanced']
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Toronto Government**")
st.sidebar.markdown("Parks, Forestry & Recreation")

# ── Apply Filters ─────────────────────────────
filtered = master[
    (master['AgeGroup'].isin(selected_age)) &
    (master['Gender'].isin(selected_gender)) &
    (master['CourseCategory'].isin(selected_cat)) &
    (master['CourseLevel'].isin(selected_level))
]

# ── Title ─────────────────────────────────────
st.title("🎓 EdTech Enrollment & Engagement Analytics")
st.markdown("Behavioral and demographic insights for the EduPro online learning platform")
st.markdown("---")

# =============================================
# MODULE 1 — KPI Summary Cards
# =============================================
st.header("📊 Platform Overview")

total      = len(filtered)
unique_u   = filtered['UserID'].nunique()
unique_c   = filtered['CourseID'].nunique()
avg_enroll = round(total / unique_u, 2) if unique_u > 0 else 0
free_pct   = round(len(filtered[filtered['CourseType'] == 'Free']) / total * 100, 1) if total > 0 else 0

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("Total Enrollments", f"{total:,}")
with col2:
    st.metric("Active Learners", f"{unique_u:,}")
with col3:
    st.metric("Courses Available", f"{unique_c:,}")
with col4:
    st.metric("Avg Courses/Learner", f"{avg_enroll}")
with col5:
    st.metric("Free Course %", f"{free_pct}%")

st.markdown("---")

# =============================================
# MODULE 2 — Learner Demographics
# =============================================
st.header("👥 Learner Demographic Overview")

col1, col2 = st.columns(2)

with col1:
    age_data = filtered.groupby('AgeGroup').size().reindex(
        age_order).reset_index()
    age_data.columns = ['Age Group', 'Enrollments']
    fig = go.Figure(go.Bar(
        x=age_data['Age Group'],
        y=age_data['Enrollments'],
        marker_color=['#e74c3c', '#3498db', '#2ecc71'],
        text=age_data['Enrollments'].apply(lambda x: f'{x:,}'),
        textposition='outside'
    ))
    fig.update_layout(
        title='Enrollments by Age Group',
        xaxis_title='Age Group',
        yaxis_title='Enrollments',
        showlegend=False,
        height=400,
        yaxis=dict(range=[0, 5800])
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    gender_data = filtered.groupby('Gender').size().reset_index()
    gender_data.columns = ['Gender', 'Enrollments']
    fig2 = px.pie(
        gender_data, values='Enrollments', names='Gender',
        color_discrete_sequence=['#e91e8c', '#3498db'],
        title='Gender Distribution'
    )
    fig2.update_layout(height=400)
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# =============================================
# MODULE 3 — Age-wise Enrollment Charts
# =============================================
st.header("📈 Age-wise Enrollment Analysis")

col1, col2 = st.columns(2)

with col1:
    age_level = filtered.groupby(['AgeGroup', 'CourseLevel']).size().reset_index()
    age_level.columns = ['Age Group', 'Course Level', 'Enrollments']
    fig3 = px.bar(
        age_level, x='Age Group', y='Enrollments',
        color='Course Level',
        color_discrete_map={
            'Beginner'    : '#2ecc71',
            'Intermediate': '#f39c12',
            'Advanced'    : '#e74c3c'
        },
        barmode='group',
        title='Age Group vs Course Level',
        category_orders={'Age Group': age_order}
    )
    fig3.update_layout(height=400)
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    age_cat = filtered.groupby(['AgeGroup', 'CourseCategory']).size().reset_index()
    age_cat.columns = ['Age Group', 'Category', 'Enrollments']
    fig4 = px.bar(
        age_cat, x='Age Group', y='Enrollments',
        color='Category',
        color_discrete_sequence=[
            '#1A5276', '#85C1E9',
            '#1A5276', '#85C1E9',
            '#1A5276', '#85C1E9',
            '#1A5276', '#85C1E9',
            '#1A5276', '#85C1E9',
            '#1A5276', '#85C1E9',
        ],
        title='Age Group vs Course Category',
        barmode='stack',
        category_orders={'Age Group': age_order}
    )
    fig4.update_layout(height=400)
    st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

# =============================================
# MODULE 4 — Gender-based Course Preferences
# =============================================
st.header("⚥ Gender-based Course Preference Analysis")

col1, col2 = st.columns(2)

with col1:
    gender_cat = filtered.groupby(['CourseCategory', 'Gender']).size().reset_index()
    gender_cat.columns = ['Category', 'Gender', 'Enrollments']
    fig5 = px.bar(
        gender_cat, x='Enrollments', y='Category',
        color='Gender',
        color_discrete_map={
            'Female': '#e91e8c',
            'Male'  : '#3498db'
        },
        barmode='group',
        title='Gender vs Course Category',
        orientation='h'
    )
    fig5.update_layout(height=500)
    st.plotly_chart(fig5, use_container_width=True)

with col2:
    gender_level = filtered.groupby(['CourseLevel', 'Gender']).size().reset_index()
    gender_level.columns = ['Level', 'Gender', 'Enrollments']
    fig6 = px.bar(
        gender_level, x='Level', y='Enrollments',
        color='Gender',
        color_discrete_map={
            'Female': '#e91e8c',
            'Male'  : '#3498db'
        },
        barmode='group',
        title='Gender vs Course Level',
        category_orders={'Level': ['Beginner', 'Intermediate', 'Advanced']}
    )
    fig6.update_layout(height=500)
    st.plotly_chart(fig6, use_container_width=True)

st.markdown("---")

# =============================================
# MODULE 5 — Course Category Popularity
# =============================================
st.header("📚 Course Category Popularity")

col1, col2 = st.columns(2)

with col1:
    cat_data = filtered.groupby('CourseCategory').size().reset_index()
    cat_data.columns = ['Category', 'Enrollments']
    cat_data = cat_data.sort_values('Enrollments', ascending=True)
    fig7 = go.Figure(go.Bar(
        x=cat_data['Enrollments'],
        y=cat_data['Category'],
        orientation='h',
        marker_color='#3498db',
        text=cat_data['Enrollments'].apply(lambda x: f'{x:,}'),
        textposition='outside'
    ))
    fig7.update_layout(
        title='Enrollments by Course Category',
        xaxis_title='Enrollments',
        yaxis_title='',
        showlegend=False,
        height=500,
        xaxis=dict(range=[0, 1050])
    )
    st.plotly_chart(fig7, use_container_width=True)

with col2:
    type_data = filtered.groupby('CourseType').size().reset_index()
    type_data.columns = ['Type', 'Enrollments']
    fig8 = px.pie(
        type_data, values='Enrollments', names='Type',
        color_discrete_sequence=['#2ecc71', '#e74c3c'],
        title='Free vs Paid Enrollments'
    )
    fig8.update_layout(height=500)
    st.plotly_chart(fig8, use_container_width=True)

st.markdown("---")

# =============================================
# MODULE 6 — Heatmaps
# =============================================
st.header("🗺️ Enrollment Heatmaps")

col1, col2 = st.columns(2)

with col1:
    pivot1 = filtered.pivot_table(
        values='TransactionID',
        index='AgeGroup',
        columns='CourseCategory',
        aggfunc='count'
    ).reindex(['<18', '18-25', '26-35'])
    fig9 = px.imshow(
        pivot1, text_auto='.0f',
        color_continuous_scale='YlOrRd',
        title='Enrollments — Age Group x Category',
        aspect='auto'
    )
    fig9.update_layout(height=400)
    st.plotly_chart(fig9, use_container_width=True)

with col2:
    pivot2 = filtered.pivot_table(
        values='TransactionID',
        index='Gender',
        columns='CourseLevel',
        aggfunc='count'
    )[['Beginner', 'Intermediate', 'Advanced']]
    fig10 = px.imshow(
        pivot2, text_auto='.0f',
        color_continuous_scale='Blues',
        title='Enrollments — Gender x Course Level',
        aspect='auto'
    )
    fig10.update_layout(height=400)
    st.plotly_chart(fig10, use_container_width=True)

st.markdown("---")

# =============================================
# MODULE 7 — Monthly Trend & Top Courses
# =============================================
st.header("📅 Enrollment Trends & Top Courses")

col1, col2 = st.columns(2)

with col1:
    monthly = filtered.groupby('Month').size().reset_index()
    monthly.columns = ['Month', 'Enrollments']
    month_names = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr',
                   5:'May', 6:'Jun', 7:'Jul', 8:'Aug',
                   9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
    monthly['Month Name'] = monthly['Month'].map(month_names)
    fig11 = px.line(
        monthly, x='Month Name', y='Enrollments',
        markers=True,
        title='Monthly Enrollment Trend',
        color_discrete_sequence=['#3498db']
    )
    fig11.update_traces(line_width=2.5, marker_size=8,
                        marker_color='#e74c3c')
    fig11.update_layout(height=400)
    st.plotly_chart(fig11, use_container_width=True)

with col2:
    top10 = filtered.groupby('CourseName').size().reset_index()
    top10.columns = ['Course', 'Enrollments']
    top10 = top10.sort_values('Enrollments', ascending=True).tail(10)
    fig12 = go.Figure(go.Bar(
        x=top10['Enrollments'],
        y=top10['Course'],
        orientation='h',
        marker_color='#9b59b6',
        text=top10['Enrollments'],
        textposition='outside'
    ))
    fig12.update_layout(
        title='Top 10 Most Enrolled Courses',
        xaxis_title='Enrollments',
        yaxis_title='',
        showlegend=False,
        height=400,
        xaxis=dict(range=[0, 380])
    )
    st.plotly_chart(fig12, use_container_width=True)

st.markdown("---")

# =============================================
# MODULE 8 — Raw Data Explorer
# =============================================
st.header("📋 Raw Data Explorer")

col1, col2 = st.columns([3, 1])
with col1:
    st.write(f"Showing {len(filtered):,} enrollments based on current filters")
with col2:
    show_free = st.checkbox("Show Free courses only", value=False)

display_df = filtered[filtered['CourseType'] == 'Free'] if show_free else filtered
st.dataframe(
    display_df[['UserID', 'Gender', 'AgeGroup', 'CourseName',
                'CourseCategory', 'CourseLevel', 'CourseType',
                'TransactionDate']].head(500),
    use_container_width=True
)

st.markdown("---")
st.markdown("**Toronto Government — Parks, Forestry & Recreation** | EduPro Learner Analytics | 2026")
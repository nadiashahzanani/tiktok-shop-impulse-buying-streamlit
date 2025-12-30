import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(page_title="Impulse Buying Factors - TikTok Shop", layout="wide")

# -----------------------------
# Load cleaned dataset
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_excel("responses.xlsx")

df = load_data()

# -----------------------------
# Title & Problem
# -----------------------------
st.title("Key Factors Influencing Students’ Impulse Buying on TikTok Shop")

st.subheader("Problem Statement")
st.write("""
TikTok Shop combines entertainment, promotions, and instant purchasing,
leading many students to make impulsive purchases without planning.
However, students are not fully aware of the factors influencing their
impulse buying behavior such as promotions, product presentation, trust,
and social influence.
""")

st.subheader("Objective")
st.write("""
To identify the key factors that influence students’ impulse buying behavior
on TikTok Shop through interactive visualization.
""")

# -----------------------------
# Sidebar filters
# -----------------------------
st.sidebar.header("Filter Respondents")
gender_filter = st.sidebar.multiselect("Gender", options=df["Gender"].unique(), default=df["Gender"].unique())
age_filter = st.sidebar.multiselect("Age", options=df["Age"].unique(), default=df["Age"].unique())
income_filter = st.sidebar.multiselect("Monthly Income", options=df["Monthly Income"].unique(), default=df["Monthly Income"].unique())

filtered_df = df[
    (df["Gender"].isin(gender_filter)) &
    (df["Age"].isin(age_filter)) &
    (df["Monthly Income"].isin(income_filter))
]

# -----------------------------
# Factor columns
# -----------------------------
factor_cols = [col for col in df.columns if "promotion" in col.lower() or "trust" in col.lower() or "presentation" in col.lower() or "influence" in col.lower()]
filtered_df["Impulse Score"] = filtered_df[factor_cols].mean(axis=1)

# ==================================================
# Visualization 1: Bar Chart (Interactive)
# ==================================================
st.subheader("1. Average Score of Impulse Buying Factors")
avg_scores = filtered_df[factor_cols].mean().reset_index()
avg_scores.columns = ["Factor", "Average Score"]
fig1 = px.bar(avg_scores, x="Factor", y="Average Score", color="Average Score", text="Average Score", title="Average Score of Impulse Buying Factors")
st.plotly_chart(fig1, use_container_width=True)

# ==================================================
# Visualization 2: Heatmap (Interactive)
# ==================================================
st.subheader("2. Correlation Between Factors")
corr = filtered_df[factor_cols].corr().round(2)
fig2 = px.imshow(corr, text_auto=True, color_continuous_scale='RdBu_r', title="Correlation Heatmap of Factors")
st.plotly_chart(fig2, use_container_width=True)

# ==================================================
# Visualization 3: Box Plot (Interactive)
# ==================================================
st.subheader("3. Distribution of Factor Influence")
fig3 = px.box(filtered_df, y=factor_cols, points="all", title="Distribution of Factor Influence")
st.plotly_chart(fig3, use_container_width=True)

# ==================================================
# Visualization 4: Stacked Bar (Likert) Interactive
# ==================================================
st.subheader("4. Agreement Levels for Impulse Buying Factors")
likert_data = filtered_df[factor_cols].apply(pd.value_counts).fillna(0)
likert_data = likert_data.T.reset_index().melt(id_vars="index")
likert_data.columns = ["Factor", "Response", "Count"]
fig4 = px.bar(likert_data, x="Factor", y="Count", color="Response", title="Stacked Agreement Levels", text="Count")
st.plotly_chart(fig4, use_container_width=True)

# ==================================================
# Visualization 5: Scatter Plot (Interactive)
# ==================================================
st.subheader("5. Factor vs Overall Impulse Score")
selected_factor = st.selectbox("Select a factor for scatter plot", factor_cols)
fig5 = px.scatter(filtered_df, x=selected_factor, y="Impulse Score", color="Gender", size="Impulse Score", hover_data=factor_cols, trendline="ols", title=f"{selected_factor} vs Overall Impulse Score")
st.plotly_chart(fig5, use_container_width=True)

# -----------------------------
# Final interpretation
# -----------------------------
st.subheader("Overall Interpretation")
st.write("""
Promotions, product presentation, trust, and social influence are the key
factors influencing impulse buying on TikTok Shop.
These interactive visualizations allow users to explore patterns and
relationships more deeply, making the insights clearer and more actionable.
""")

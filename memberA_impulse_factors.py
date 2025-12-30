import streamlit as st
import pandas as pd
import plotly.express as px

# 1️⃣ Page setup
st.set_page_config(page_title="Impulse Buying Factors", layout="wide")

# 2️⃣ Header & intro
st.header("TikTok Shop — Student Impulse Buying Behavior")
st.write("""
A scientific visualization exploring how promotions, product presentation,
trust, motivation, and discovery affect students' impulse buying behavior.
""")

# 3️⃣ Load dataset
df = pd.read_excel("tiktok_impulse_data_responses.xlsx")  # Adjust path if necessary

# 4️⃣ Factor scores (if not already in dataset)
factor_cols = [
    'promotion_score', 'discovery_score', 'trust_score',
    'motivation_score', 'presentation_score', 'impulse_score'
]

# 5️⃣ Sidebar filters
st.sidebar.header("Filter Respondents")
gender_filter = st.sidebar.multiselect("Gender", df['gender'].unique(), df['gender'].unique())
filtered_df = df[df['gender'].isin(gender_filter)]

# 6️⃣ Visualization 1: Correlation Heatmap
st.subheader("1. Correlation Between Factors")
corr = filtered_df[factor_cols].corr()
fig1 = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale='RdBu_r',
    title="Correlation Between Key Factors and Impulse Buying"
)
st.plotly_chart(fig1)

st.write("""
**Interpretation:**  
The correlation heatmap indicates that promotion, discovery, and presentation 
factors have a moderate positive relationship with impulse buying, while trust 
has a weaker relationship. This suggests that students’ unplanned purchases 
are largely driven by immediate stimuli such as time-limited promotions, 
exposure to attractive products, and visual presentation. Trust plays a lesser role.
""")

# 7️⃣ Visualization 2: Boxplot
st.subheader("2. Distribution of Factor Scores")
fig2 = px.box(
    filtered_df,
    y=factor_cols[:-1],
    points="all",
    title="Distribution of Impulse Buying Factors"
)
fig2.update_layout(yaxis_title="Agreement Level")
st.plotly_chart(fig2)

st.write("""
**Interpretation:**  
Promotion and presentation factors have higher median scores than trust, 
confirming their stronger influence. The wider spread in presentation scores 
suggests variability in how visual elements affect different students.
""")

# 8️⃣ Visualization 3: Scatter Plot (Promotion vs Impulse)
st.subheader("3. Promotion Influence vs Impulse Buying Score")
fig3 = px.scatter(
    filtered_df,
    x='promotion_score',
    y='impulse_score',
    trendline='ols',
    title="Promotion vs Impulse Buying Score"
)
st.plotly_chart(fig3)

st.write("""
**Interpretation:**  
Higher promotion scores are linked to higher impulse buying scores. 
Students who notice time-limited promotions or special deals are more likely 
to make spontaneous purchases. The trend line confirms promotions have a noticeable effect.
""")

# 9️⃣ Visualization 4: All Factors vs Impulse Score
st.subheader("4. All Factors vs Impulse Buying Score")
long_df = filtered_df.melt(
    id_vars='impulse_score',
    value_vars=factor_cols[:-1],
    var_name='Factor',
    value_name='Factor Score'
)
fig4 = px.scatter(
    long_df,
    x='Factor Score',
    y='impulse_score',
    color='Factor',
    trendline='ols',
    title="All Factors vs Impulse Score"
)
st.plotly_chart(fig4)

st.write("""
**Interpretation:**  
A positive relationship exists between factor scores and impulse buying. 
As students rate a factor higher, their tendency to make impulse purchases 
increases. Strengthening these key factors can effectively encourage impulsive shopping.
""")

# 10️⃣ Visualization 5: Average Factor Scores (Bar Chart)
st.subheader("5. Average Influence Level of Each Factor")
avg_scores = filtered_df[factor_cols[:-1]].mean().reset_index()
avg_scores.columns = ['Factor','Average Score']

fig5 = px.bar(
    avg_scores,
    x='Factor',
    y='Average Score',
    title="Average Factor Scores"
)
st.plotly_chart(fig5)

st.write("""
**Interpretation:**  
All factors have relatively high scores. Motivation and discovery have slightly 
higher averages, suggesting students are more influenced by exciting promotions 
or surprising product finds. Trust has the lowest average, indicating it plays a smaller role.
""")

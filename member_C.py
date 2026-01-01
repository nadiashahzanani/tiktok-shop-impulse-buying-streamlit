import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

def app():
    st.header(
        "Member C — Sub-Objective 3: Examine Trust, Enjoyment & Shopping Motivation on TikTok Shop"
    )

    # --------------------------------------------------
    # Load dataset
    # --------------------------------------------------
    df = pd.read_excel("cleaned_tiktok_data.xlsx")

    # --------------------------------------------------
    # Define factor groups
    # --------------------------------------------------
    trust_items = [
        'trust_no_risk',
        'trust_reliable',
        'trust_variety_meets_needs',
        'trust_sells_honestly',
        'trust_quality_matches_description'
    ]

    motivation_items = [
        'relax_reduce_stress',
        'motivated_by_discount_promo',
        'motivated_by_gifts'
    ]

    # --------------------------------------------------
    # Create composite scores
    # --------------------------------------------------
    df['Trust_Score'] = df[trust_items].mean(axis=1)
    df['Motivation_Score'] = df[motivation_items].mean(axis=1)

     # 🔧 SAFETY: remove missing values (important)
    df = df.dropna(subset=['Trust_Score', 'Motivation_Score'])

    # --------------------------------------------------
    # Sidebar filters
    # --------------------------------------------------
    st.sidebar.header("Filter Respondents")
    gender_filter = st.sidebar.multiselect(
        "Gender",
        options=df['gender'].unique(),
        default=df['gender'].unique()
    )

    filtered_df = df[df['gender'].isin(gender_filter)]

    # --------------------------------------------------
    # 1️⃣ Correlation Heatmap
    # --------------------------------------------------
    st.subheader("1️⃣ Correlation Between Trust & Motivation Items")

    corr_items = filtered_df[trust_items + motivation_items].corr()
    fig1 = px.imshow(
        corr_items,
        text_auto=True,
        color_continuous_scale='RdBu_r'
    )
    st.plotly_chart(fig1, use_container_width=True)

    st.write("""
    **Interpretation:**  
    The correlation heatmap supports the finding that trust-related factors such as
    reliability, honesty, and product quality are positively associated with motivation
    factors such as discounts and gifts. This indicates that higher trust increases
    shopping motivation on TikTok Shop.
    """)

    # --------------------------------------------------
    # 2️⃣ Bar Chart – Trust Item Means
    # --------------------------------------------------
    st.subheader("2️⃣ Average Trust Scores by Item")

    trust_means = filtered_df[trust_items].mean().reset_index()
    trust_means.columns = ['Trust Item', 'Mean Score']

    fig2 = px.bar(
        trust_means,
        x='Trust Item',
        y='Mean Score'
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.write("""
    **Interpretation:**  
    This bar chart compares the average trust scores across different trust dimensions.
    The results show that product variety and reliability receive the highest trust ratings,
    indicating these aspects are most important to respondents.
    """)

    # --------------------------------------------------
    # 3️⃣ Bar Chart – Motivation Item Means
    # --------------------------------------------------
    st.subheader("3️⃣ Average Motivation Scores by Item")

    motivation_means = filtered_df[motivation_items].mean().reset_index()
    motivation_means.columns = ['Motivation Item', 'Mean Score']

    fig3 = px.bar(
        motivation_means,
        x='Motivation Item',
        y='Mean Score'
    )
    st.plotly_chart(fig3, use_container_width=True)

    st.write("""
    **Interpretation:**  
    Discounts and promotions emerge as the strongest motivational factor,
    followed by gifts and stress reduction. This indicates that promotional
    strategies are highly effective in motivating impulse purchases.
    """)

    # --------------------------------------------------
    # 4️⃣ Scatter Plot – Trust vs Motivation
    # --------------------------------------------------
    st.subheader("4️⃣ Relationship Between Trust and Motivation")

    # Scatter plot
    fig4 = px.scatter(
        filtered_df,
        x='Trust_Score',
        y='Motivation_Score',
        labels={
            'Trust_Score': 'Trust Score',
            'Motivation_Score': 'Motivation Score'
        }
    )
    
    # ---- ADD MANUAL REGRESSION LINE (NumPy) ----
    x = filtered_df['Trust_Score'].values
    y = filtered_df['Motivation_Score'].values
    
    # Calculate line of best fit
    m, b = np.polyfit(x, y, 1)
    
    # Create line values
    x_line = np.linspace(x.min(), x.max(), 100)
    y_line = m * x_line + b
    
    # Add line to plot
    fig4.add_scatter(
        x=x_line,
        y=y_line,
        mode='lines',
        name='Trend Line',
        line=dict(width=3)
    )
    
    st.plotly_chart(fig4, use_container_width=True)

    st.write("""
    **Interpretation:**  
    The scatter plot shows a positive relationship between trust and shopping motivation.
    As trust increases, motivation also increases, supporting the importance of trust
    as a psychological driver of impulse buying behavior.
    """)

    # --------------------------------------------------
    # 5️⃣ Radar Chart – Trust Dimensions
    # --------------------------------------------------
    st.subheader("5️⃣ Trust Dimension Radar Chart")

    labels = trust_items
    values = trust_means['Mean Score'].tolist()
    values += values[:1]

    angles = np.linspace(0, 2 * np.pi, len(labels) + 1)

    fig5, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.plot(angles, values, linewidth=2)
    ax.fill(angles, values, alpha=0.25)
    ax.set_thetagrids(angles[:-1] * 180 / np.pi, labels)

    st.pyplot(fig5)

    st.write("""
    **Interpretation:**  
    The radar chart shows that trust dimensions are relatively balanced, with
    slightly higher scores for reliability and product quality, highlighting
    their importance in shaping overall trust.
    """)

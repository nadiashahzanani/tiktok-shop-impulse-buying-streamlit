import streamlit as st

# ------------------------------------------------------------
# Page Setup
# ------------------------------------------------------------
st.set_page_config(
    page_title="TikTok Shop Impulse Buying Visualization",
    layout="wide"
)

# ------------------------------------------------------------
# Header title
# ------------------------------------------------------------
st.header("📱 TikTok Shop — Student Impulse Buying Behavior")

# ------------------------------------------------------------
# Intro paragraph
# ------------------------------------------------------------
st.write(
    """
    A scientific visualization exploring how **promotions, product presentation, trust, motivation, and social influence**
 affect students' impulse buying behavior on TikTok Shop. 
    """
)

# ------------------------------------------------------------
# Dataset information
# ------------------------------------------------------------
st.write(
    """
    This dashboard uses survey data collected from university students about their shopping experiences on TikTok Shop.
    The aim is to analyze key factors driving impulse purchases and visualize patterns effectively.
    """
)

# ------------------------------------------------------------
# Navigation / Multi-page setup (Optional)
# ------------------------------------------------------------
# If you want this page only, you can skip the multi-page code.
# If your group uses multi-page Streamlit, you can rename your page:
# Example for multi-page:
# page1 = st.Page('member_impulse_factors.py', title='Page 1', icon=":bar_chart:")
# page2 = st.Page('Objectives2.py', title='Page 2', icon=":insights:")
# page3 = st.Page('Objectives3.py', title='Page 3', icon=":schedule:")
# page4 = st.Page('Objectives4.py', title='Page 4', icon=":schedule:")

# pg = st.navigation({"Menu": [page1, page2, page3, page4]}) 
# pg.run()

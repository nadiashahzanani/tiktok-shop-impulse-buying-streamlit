import streamlit as st

# Page configuration
st.set_page_config(
    page_title="TikTok Shop Impulse Buying Study",
    layout="wide"
)

st.title("📊 Determinants of Students' Impulse Buying Behavior on TikTok Shop")

# Sidebar for page navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to page:", ["Main Page", "Member A", "Member B", "Member C", "Member D"])

# Load member pages
if page == "Main Page":
    st.subheader("Project Overview")
    st.write("Interactive dashboard exploring students' impulse buying behavior.")
elif page == "Member C":
    import member_C
    member_C.app()
else:
    st.write(f"{page} page is under construction.")

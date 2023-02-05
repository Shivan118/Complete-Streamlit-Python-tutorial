import streamlit as st

st.title("Happy Birday!")

# ballon
st.balloons()


# Sidebar
st.sidebar.header("About")
st.sidebar.text("This is our demo project")

# Select Box
algoritmhs = st.sidebar.selectbox("Your Algorithm", ["Liner Regression", "Logistic Regression", "Decision tree",
"Random Forest"])
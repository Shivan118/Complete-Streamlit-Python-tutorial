import streamlit as st

# Title

st.title("Machine Learning project")

# Header / Subheader
st.header("This is a header")

st.subheader("This is a Subheader") # h1, h2, h3, h4 --

# text
st.text("Hello Streamlit")

# markdown
st.markdown(" # This is our first markdown")

st.markdown(" #### This is our first markdown")

# Error / Colorful text
st.success("Scuessful Done")

#Information
st.info("Information")

st.warning("This is a warning")

st.error("This is an error")

# Exception
st.exception("NameError('name pd is not defiened')")

import pandas
st.help(pandas)

# range function

st.help(range)

# Writing text super function
st.write("Text with write")

st.write(range(10))

from PIL import Image

img = Image.open("1.jpg")
st.image(img)
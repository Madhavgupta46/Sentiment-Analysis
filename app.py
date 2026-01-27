import streamlit as st

st.set_page_config(page_title="Test App", layout="centered")

st.title("🚀 Streamlit is working!")
st.write("If you can see this, deployment is successful.")

name = st.text_input("Your name")

if st.button("Say hi"):
    st.success(f"Hello {name}! 🎉")

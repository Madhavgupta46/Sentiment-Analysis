import streamlit as st
import joblib

# Load ONLY the model
model = joblib.load("model.joblib")

st.set_page_config(page_title="Sentiment Analysis", layout="centered")
st.title("Sentiment Analysis App 😊😐😠")

text = st.text_area("Enter text")

if st.button("Analyze Sentiment"):
    if text.strip() == "":
        st.warning("Please enter some text")
    else:
        pred = model.predict([text])[0]   # 👈 IMPORTANT

        if pred == 0:
            st.error("Negative 😠")
        elif pred == 1:
            st.warning("Neutral 😐")
        else:
            st.success("Positive 😊")

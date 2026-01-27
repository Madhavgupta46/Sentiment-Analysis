import streamlit as st
import joblib

st.set_page_config(page_title="Sentiment Analysis", layout="centered")

@st.cache_resource
def load_model():
    model = joblib.load("model.joblib")
    vectorizer = joblib.load("vectorizer.joblib")
    return model, vectorizer

model, vectorizer = load_model()

st.title("Sentiment Analysis App 😊😐😠")

text = st.text_area("Enter your text")

if st.button("Analyze Sentiment"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        vec = vectorizer.transform([text])
        pred = model.predict(vec)[0]

        if pred == 0:
            st.error("Negative 😠")
        elif pred == 1:
            st.warning("Neutral 😐")
        else:
            st.success("Positive 😊")

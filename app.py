# -*- coding: utf-8 -*-
import streamlit as st
import joblib

model = joblib.load("model.joblib")
vectorizer = joblib.load("vectorizer.joblib")

st.title("🧠 Sentiment Analysis App")

text = st.text_area("Enter text")

if st.button("Predict"):
    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0]

    if pred == 0:
        st.error("🔴 Negative")
    elif pred == 1:
        st.info("🟡 Neutral")
    else:
        st.success("🟢 Positive")

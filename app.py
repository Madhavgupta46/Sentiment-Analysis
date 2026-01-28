import streamlit as st
import joblib
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Sentiment Analysis App",
    layout="centered"
)

# ---------------- LOAD MODEL ----------------
# IMPORTANT:
# Replace these with your actual files
# vectorizer = joblib.load("vectorizer.pkl")
# model = joblib.load("model.pkl")

def predict_sentiment(text):
    """
    TEMPORARY DEMO FUNCTION
    Replace this logic with your trained ML model
    """
    text = text.lower()
    if any(word in text for word in ["good", "love", "excellent", "great", "amazing"]):
        return "Positive"
    elif any(word in text for word in ["bad", "hate", "worst", "terrible", "poor"]):
        return "Negative"
    else:
        return "Neutral"


# ---------------- CSS ----------------
st.markdown("""
<style>

/* GLOBAL */
.stApp {
    background-color: #F8FAFC;
    font-family: "Inter", sans-serif;
}

.block-container {
    max-width: 900px;
    padding-top: 2rem;
}

/* HEADINGS */
h1, h2, h3 {
    color: #0F172A !important;
    font-weight: 700;
}

/* CARD */
.card {
    background: #FFFFFF;
    border-radius: 16px;
    padding: 24px;
    margin-top: 20px;
    box-shadow: 0 10px 25px rgba(15, 23, 42, 0.08);
}

/* BUTTON */
.stButton > button {
    background: linear-gradient(135deg, #3B82F6, #2563EB);
    color: white;
    border-radius: 12px;
    padding: 12px 28px;
    font-size: 16px;
    font-weight: 600;
    border: none;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #2563EB, #1D4ED8);
}

/* TEXT AREA */
textarea {
    border-radius: 12px !important;
    border: 1px solid #CBD5E1 !important;
}

/* SENTIMENT STYLES */
.positive {
    border-left: 6px solid #22C55E;
}

.neutral {
    border-left: 6px solid #FACC15;
}

.negative {
    border-left: 6px solid #EF4444;
}

/* FOOTER */
.footer {
    text-align: center;
    color: #64748B;
    margin-top: 40px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO SECTION ----------------
st.markdown("""
<div style="text-align:center;">
    <h1>🧠 Sentiment Analysis</h1>
    <p style="font-size:1.1rem; color:#475569;">
        Analyze emotions in text using Machine Learning & NLP
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- INPUT CARD ----------------
st.markdown("""
<div class="card">
    <h3>✍️ Enter Text</h3>
    <p style="color:#64748B;">
        Type a sentence, review, or opinion below
    </p>
</div>
""", unsafe_allow_html=True)

user_text = st.text_area(
    "",
    placeholder="I really loved this product, it exceeded my expectations!",
    height=140
)

# ---------------- BUTTON ----------------
st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
analyze = st.button("✨ Analyze Sentiment")
st.markdown("</div>", unsafe_allow_html=True)

# ---------------- RESULT ----------------
if analyze:
    if user_text.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        sentiment = predict_sentiment(user_text)

        if sentiment == "Positive":
            st.markdown("""
            <div class="card positive">
                <h2>😊 Positive Sentiment</h2>
                <p>The text expresses a positive emotional tone.</p>
            </div>
            """, unsafe_allow_html=True)

        elif sentiment == "Neutral":
            st.markdown("""
            <div class="card neutral">
                <h2>😐 Neutral Sentiment</h2>
                <p>The text is emotionally neutral or factual.</p>
            </div>
            """, unsafe_allow_html=True)

        else:
            st.markdown("""
            <div class="card negative">
                <h2>😡 Negative Sentiment</h2>
                <p>The text expresses a negative emotional tone.</p>
            </div>
            """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
🚀 Built with Streamlit & Machine Learning <br>
by <b>Madhav Gupta</b>
</div>
""", unsafe_allow_html=True)

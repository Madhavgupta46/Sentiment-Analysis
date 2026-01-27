import streamlit as st
import joblib

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Sentiment Analyzer",
    page_icon="💬",
    layout="centered"
)

# ---------------- LOAD MODEL ----------------
model = joblib.load("model.joblib")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #0f172a;
    color: white;
}
.title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 5px;
}
.subtitle {
    text-align: center;
    font-size: 16px;
    color: #cbd5f5;
    margin-bottom: 30px;
}
textarea {
    border-radius: 12px !important;
}
.sentiment-box {
    padding: 25px;
    border-radius: 16px;
    text-align: center;
    font-size: 24px;
    font-weight: 700;
    margin-top: 20px;
}
.positive {
    background: linear-gradient(135deg, #16a34a, #22c55e);
}
.neutral {
    background: linear-gradient(135deg, #f59e0b, #facc15);
    color: black;
}
.negative {
    background: linear-gradient(135deg, #dc2626, #ef4444);
}
.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 13px;
    margin-top: 50px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="title">💬 Sentiment Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered text sentiment classification</div>', unsafe_allow_html=True)

# ---------------- INPUT ----------------
text = st.text_area(
    "Enter your text below 👇",
    height=150,
    placeholder="Type a sentence, review, or opinion..."
)

# ---------------- BUTTON ----------------
analyze = st.button("✨ Analyze Sentiment", use_container_width=True)

# ---------------- PREDICTION ----------------
if analyze:
    if text.strip() == "":
        st.warning("⚠️ Please enter some text first")
    else:
        pred = model.predict([text])[0]

        if pred == 2:
            st.markdown(
                '<div class="sentiment-box positive">😊 Positive Sentiment</div>',
                unsafe_allow_html=True
            )
        elif pred == 1:
            st.markdown(
                '<div class="sentiment-box neutral">😐 Neutral Sentiment</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                '<div class="sentiment-box negative">😠 Negative Sentiment</div>',
                unsafe_allow_html=True
            )

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
🚀 Built with Streamlit & Machine Learning <br>
by <b>Madhav Gupta</b>
</div>
""", unsafe_allow_html=True)

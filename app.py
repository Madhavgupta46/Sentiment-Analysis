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
/* App background */
.main {
    background-color: #F8FAFC;
    color: #1F2937;
}

/* Title */
.title {
    text-align: center;
    font-size: 40px;
    font-weight: 800;
    color: #1F2937;
    margin-bottom: 6px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 16px;
    color: #475569;
    margin-bottom: 30px;
}

/* Text input */
textarea {
    background-color: #FFFFFF !important;
    color: #1F2937 !important;
    border: 1px solid #CBD5E1 !important;
    border-radius: 14px !important;
}

/* Button */
.stButton > button {
    background-color: #CBD5E1;
    color: #1F2937;
    border: none;
    border-radius: 14px;
    padding: 0.6em 1.2em;
    font-size: 16px;
    font-weight: 700;
    transition: 0.3s ease;
}

.stButton > button:hover {
    background-color: #94A3B8;
    transform: scale(1.03);
}

/* Sentiment card */
.sentiment-box {
    padding: 24px;
    border-radius: 18px;
    text-align: center;
    font-size: 26px;
    font-weight: 800;
    margin-top: 22px;
    background-color: #E5E7EB;
    color: #1F2937;
}

/* Sentiment colors (soft & light) */
.positive {
    background: linear-gradient(135deg, #BBF7D0, #86EFAC);
}

.neutral {
    background: linear-gradient(135deg, #FEF3C7, #




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

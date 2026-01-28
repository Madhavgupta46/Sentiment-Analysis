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

/* ================= GLOBAL ================= */
.stApp {
    background-color: #F8FAFC;
    font-family: "Inter", sans-serif;
}

.block-container {
    padding-top: 2rem;
    max-width: 1100px;
}

/* FORCE HEADINGS VISIBILITY */
h1, h2, h3, h4 {
    color: #0F172A !important;
    font-weight: 700 !important;
    opacity: 1 !important;
    visibility: visible !important;
}

/* STREAMLIT TITLE FIX */
[data-testid="stMarkdownContainer"] h1 {
    color: #0F172A !important;
    font-size: 2.2rem !important;
}

/* REMOVE INVISIBLE HEADER BUG */
header {
    background: transparent !important;
}

/* ================= CARDS ================= */
.card {
    background: #FFFFFF;
    border-radius: 14px;
    padding: 20px;
    margin: 10px 0;
    box-shadow: 0 10px 25px rgba(15, 23, 42, 0.08);
    transition: transform 0.2s ease;
}

.card:hover {
    transform: translateY(-4px);
}

/* ================= METRIC CARDS ================= */
[data-testid="metric-container"] {
    background-color: #FFFFFF;
    border-radius: 14px;
    padding: 15px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
}

/* ================= SENTIMENT BADGES ================= */
.sentiment-positive {
    background: #DCFCE7;
    color: #166534;
    padding: 10px 16px;
    border-radius: 20px;
    font-weight: 600;
    display: inline-block;
}

.sentiment-neutral {
    background: #FEF9C3;
    color: #854D0E;
    padding: 10px 16px;
    border-radius: 20px;
    font-weight: 600;
    display: inline-block;
}

.sentiment-negative {
    background: #FEE2E2;
    color: #991B1B;
    padding: 10px 16px;
    border-radius: 20px;
    font-weight: 600;
    display: inline-block;
}

/* ================= INPUT ================= */
textarea {
    border-radius: 12px !important;
    border: 1px solid #CBD5E1 !important;
}

/* ================= BUTTON ================= */
.stButton > button {
    background: linear-gradient(135deg, #3B82F6, #2563EB);
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: 600;
    border: none;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #2563EB, #1D4ED8);
}

/* ================= INFO / SUCCESS ================= */
.stAlert {
    border-radius: 12px;
}

/* ================= FOOTER ================= */
.footer {
    text-align: center;
    color: #64748B;
    margin-top: 40px;
    font-size: 14px;
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

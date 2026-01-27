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
/* Main background */
.main {
    background-color: #020617;
    color: #E5E7EB;
}

/* Title */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: #38BDF8;
    margin-bottom: 6px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 16px;
    color: #E5E7EB;
    opacity: 0.85;
    margin-bottom: 30px;
}

/* Text area */
textarea {
    background-color: #020617 !important;
    color: #E5E7EB !important;
    border: 1px solid #38BDF8 !important;
    border-radius: 14px !important;
}

/* Button */
.stButton > button {
    background: linear-gradient(135deg, #38BDF8, #0EA5E9);
    color: #020617;
    border: none;
    border-radius: 14px;
    padding: 0.6em 1.2em;
    font-size: 16px;
    font-weight: 700;
    transition: 0.3s ease;
}

.stButton > button:hover {
    transform: scale(1.03);
    background: linear-gradient(135deg, #0EA5E9, #38BDF8);
}

/* Sentiment result box */
.sentiment-box {
    padding: 24px;
    border-radius: 18px;
    text-align: center;
    font-size: 26px;
    font-weight: 800;
    margin-top: 22px;
    color: #E5E7EB;
}

/* Sentiment colors */
.positive {
    background: linear-gradient(135deg, #16A34A, #22C55E);
}

.neutral {
    background: linear-gradient(135deg, #FB923C, #FDBA74);
    color: #020617;
}

.negative {
    background: linear-gradient(135deg, #DC2626, #EF4444);
}

/* Footer */
.footer {
    text-align: center;
    color: #E5E7EB;
    opacity: 0.7;
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

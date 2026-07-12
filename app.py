import streamlit as st

from ai import analyze_text, analyze_image
from styles import load_css
from ui import display_result


st.set_page_config(
    page_title="ScamShield",
    page_icon="🛡️",
    layout="wide"
)


load_css()


st.title("🛡️ ScamShield")

st.markdown(
    """
### AI-Powered Scam Detection Assistant

Protect yourself from phishing, fraud, and online scams using AI.

**Features**

📝 Text Scam Detection

🖼️ Screenshot Analysis (Coming Soon)
"""
)


st.divider()


text_tab, image_tab = st.tabs(
    [
        "📝 Text Analysis",
        "🖼️ Image Analysis"
    ]
)



# ====================================================
# TEXT TAB
# ====================================================

with text_tab:

    st.subheader("📝 Message Scam Detector")


    examples = {
        "🚨 Fake Bank SMS": 
        """Dear Customer,

Your bank account will be blocked today.

Verify your account immediately:
http://secure-bank-update.com

Share your OTP to complete verification.""",


        "🎁 Lottery Scam":
        """Congratulations!

You have won ₹50,000 Amazon lottery reward.

Click here to claim your prize:
http://amazon-free-reward.com""",


        "💸 UPI Fraud":
        """Your UPI transaction failed.

You are eligible for a refund.

Click this link and enter your UPI PIN:
http://upi-refund-help.com"""
    }


    st.write("Try a demo example:")


    cols = st.columns(3)


    if "user_input" not in st.session_state:
        st.session_state.user_input = ""


    for index, example in enumerate(examples):

        if cols[index].button(example):

            st.session_state.user_input = examples[example]


    user_input = st.text_area(
        "Paste suspicious message",
        height=250,
        placeholder="Paste SMS, email, WhatsApp message...",
        key="user_input"
    )


    if st.button(
        "🔍 Analyze Text",
        use_container_width=True
    ):

        if not user_input.strip():

            st.warning("Please enter some text.")

        else:

            with st.spinner("Analyzing..."):

                result = analyze_text(user_input)

                st.divider()

                display_result(result)



# ====================================================
# IMAGE TAB
# ====================================================

with image_tab:

    st.subheader("📸 Screenshot Analysis")


    uploaded_image = st.file_uploader(
        "Upload suspicious screenshot",
        type=[
            "png",
            "jpg",
            "jpeg"
        ]
    )


    if uploaded_image:

        st.image(
            uploaded_image,
            caption="Uploaded Image",
            use_container_width=True
        )


        if st.button(
            "🛡️ Analyze Image",
            use_container_width=True
        ):

            result = analyze_image(uploaded_image)

            display_result(result)



# ====================================================
# HOW IT WORKS
# ====================================================

st.divider()

st.subheader("⚙️ How ScamShield Works")

st.markdown(
    """
### 1️⃣ User Input

The user provides a suspicious message or content.

⬇️

### 2️⃣ AI Analysis

Gemini AI analyzes scam patterns, warning signs, and suspicious behaviour.

⬇️

### 3️⃣ Risk Assessment

ScamShield generates a risk evaluation and provides safety recommendations.
"""
)



st.divider()

st.caption(
    "🛡️ ScamShield • Powered by Gemini"
)
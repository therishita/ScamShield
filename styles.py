import streamlit as st


def load_css():

    st.markdown("""
    <style>

    /* Background */
    .stApp{
        background: linear-gradient(135deg, #F8FAFF 0%, #EEF4FF 100%);
    }

    /* Main Title */
    h1{
        color:#4F46E5;
        font-size:3rem;
        font-weight:800;
    }

    /* Headings */
    h2,h3{
        color:#1E293B;
        font-weight:700;
    }

    /* Caption */
    .stCaption{
        color:#64748B;
    }

    /* Text Area */
    .stTextArea textarea{
        border:2px solid #C7D2FE !important;
        border-radius:15px !important;
        background:#FFFFFF !important;
        color:#1E293B !important;
        font-size:16px !important;
        padding:12px !important;
    }

    .stTextArea textarea:focus{
        border:2px solid #6366F1 !important;
        box-shadow:0 0 10px rgba(99,102,241,.25);
    }

    /* Buttons */
    .stButton>button{
        width:100%;
        background:linear-gradient(90deg,#6366F1,#8B5CF6);
        color:white;
        border:none;
        border-radius:12px;
        height:52px;
        font-size:17px;
        font-weight:700;
        transition:0.3s;
    }

    .stButton>button:hover{
        transform:translateY(-2px);
        box-shadow:0 8px 18px rgba(99,102,241,.30);
    }

    /* Metric Cards */
    div[data-testid="stMetric"]{
        background:white;
        border-radius:18px;
        padding:18px;
        border:1px solid #E2E8F0;
        box-shadow:0 4px 14px rgba(0,0,0,.06);
    }

    /* Info Box */
    div[data-testid="stAlert"]{
        border-radius:15px;
    }

    /* Horizontal Divider */
    hr{
        border:1px solid #E0E7FF;
    }

    /* Sidebar cards */
    div[data-testid="stVerticalBlock"] div:has(>.stAlert){
        border-radius:15px;
    }

    </style>
    """, unsafe_allow_html=True)
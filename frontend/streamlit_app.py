import streamlit as st
import requests

st.set_page_config(page_title="SupplyMind AI OS", layout="centered")

st.title("📦 SupplyMind: AI Logistics OS")
st.write("Upload an inquiry file (txt) and let AI agents process it.")

uploaded_file = st.file_uploader("Choose a file...", type=["txt"])

if uploaded_file is not None:
    st.success(f"Uploaded: {uploaded_file.name}")
    
    if st.button("🚀 Process with AI Agents"):
        with st.spinner("Sending to orchestrator..."):
            files = {"file": uploaded_file.getvalue()}
            response = requests.post("http://localhost:8000/process", files={"file": (uploaded_file.name, uploaded_file.getvalue())})

            if response.status_code == 200:
                result = response.json().get("result", {})
                st.subheader("✅ Processed Result")
                st.json(result)
            else:
                st.error("❌ Failed to process file")

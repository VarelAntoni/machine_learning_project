import streamlit as st

st.title("Tes Tombol")

user_input = st.text_input("Tulis sesuatu")
if st.button("Kirim"):
    st.write(f"✅ Kamu mengetik: {user_input}")

import streamlit as st
import pandas as pd
from datetime import datetime
from io import StringIO
import time
import os

import numpy as np
import base64

# Atur layout wide
st.set_page_config(layout="wide", page_title="Informasi Dataset", initial_sidebar_state="auto")



# Fungsi tampilkan tanggal sekarang
def tampilkan_tanggal():
    now = datetime.now()
    tanggal = now.strftime("%A, %d-%m-%Y %H:%M:%S")
    st.markdown(f"""
        <div style='text-align: right; color: #1E3A8A; font-weight: bold; font-size: 0.9rem;'>
            {tanggal}
        </div>
    """, unsafe_allow_html=True)

# Tampilkan toast saat pertama kali halaman dibuka
if "toast_shown" not in st.session_state:
    st.toast("Silakan unggah file CSV atau klik tombol 'Lakukan Analisis Dataset'", icon="ℹ️")
    st.session_state.toast_shown = True

# Tampilkan tanggal dan judul dengan CSS
tampilkan_tanggal()


st.markdown(
    """
    <style>
    .custom-title {
        color: #11009E;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        margin-top: 30px;
        margin-bottom: 30px;
    }
    </style>
    <h1 class="custom-title">Analisis Dataset Program IP4T</h1>
    """,
    unsafe_allow_html=True
)


# Upload file
file = st.file_uploader("Unggah file CSV", type=["csv"])

# Tombol untuk memulai analisis
if st.button("📂 Lakukan Analisis Dataset"):
    progress = st.progress(0, text="⏳ Memulai analisis...")

    for i in range(1, 6):
        time.sleep(0.15)
        progress.progress(i * 20, text=f"⏳ Memproses langkah {i}/5...")

    # Baca file dari upload atau default
    if file:
        df = pd.read_csv(file)
        st.success("File berhasil diunggah!")
    else:
        df = pd.read_csv("27052025.csv", sep=",")
        st.info("Menggunakan dataset default")

    # Drop kolom NO jika ada
    if "NO" in df.columns:
        df.drop(columns=["NO"], inplace=True)

    progress.progress(100, text="✅ Analisis selesai!")

    # Tampilkan data awal
    st.subheader("📁 Data Awal")
    st.dataframe(df.head())

    # Informasi struktur
    st.subheader("🧾 Informasi Struktur DataFrame")
    buffer = StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

    
    

    st.success("✅ Analisis selesai!")

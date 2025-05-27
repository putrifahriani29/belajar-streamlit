import streamlit as st
st.title("Halo, Streamlit!")
st.write("Ini adalah aplikasi Streamlit pertama saya.")



# Informasi tambahan dengan st.info
st.info("Pastikan kamu mengisi nama dan memilih opsi yang sesuai untuk hasil yang maksimal!")

# Input teks dari pengguna
nama = st.text_input("Masukkan nama kamu:")

# Tombol
if st.button("Sapa"):
    st.write(f"Halo, {nama}! Selamat belajar Streamlit.")

# Slider input angka
umur = st.slider("Berapa umur kamu?", 0, 100, 25)
st.write(f"Umur kamu adalah {umur} tahun.")

# Checkbox
if st.checkbox("Tampilkan pesan rahasia"):
    st.write("Ini pesan rahasia!")

#
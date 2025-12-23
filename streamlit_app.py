import streamlit as st
import sympy as sp

st.set_page_config(page_title="Kalkulator Integral", layout="centered")

st.title("🧮 Kalkulator Integral Numerik")

st.write("""
Masukkan fungsi dan batas integral untuk menghitung
aproksimasi integral menggunakan metode pias titik tengah.
""")

# ======================
# INPUT USER
# ======================

b = st.number_input("Batas atas (b)", value=1.0)
n = st.number_input("Jumlah pias (n)", min_value=1, value=4, step=1)

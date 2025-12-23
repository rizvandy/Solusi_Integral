import streamlit as st
import sympy as sp

st.set_page(page_title="Kalkulator Integral", layout="centered")

st.title("🧮 Kalkulator Integral Numerik")


st.write("""
Masukkan fungsi dan batas integral untuk menghitung
aproksimasi integral menggunakan metode pias titik tengah.
""")

# ======================
# INPUT USER
# ======================

a = st.number_input("Batas bawah (a)", value=0.0)
b = st.number_input("Batas atas (b)", value=1.0)
n = st.number_input("Jumlah pias (n)", min_value=1, step=1)

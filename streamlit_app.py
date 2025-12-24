import streamlit as st
import sympy as sp
import numpy as np

if st.button("Hitung Integral"):
    x = sp.symbols('x')
    

    hasil_integral = h * sum(nilai_f)

    st.success(f"Hasil aproksimasi integral = {hasil_integral}")

st.set_page_config(page_title="Kalkulator Integral", layout="centered")

st.title("🧮 Kalkulator Integral Numerik")
st.subheader("Metode Pias Titik Tengah")

st.write("""
Masukkan fungsi dan batas integral untuk menghitung
aproksimasi integral menggunakan metode pias titik tengah.
""")

# ======================
# INPUT USER
# ======================
fungsi_input = st.text_input("Masukkan fungsi f(x)", value="x**2")
a = st.number_input("Batas bawah (a)", value=0.0)
b = st.number_input("Batas atas (b)", value=1.0)
n = st.number_input("Jumlah pias (n)", min_value=1, value=4, step=1)

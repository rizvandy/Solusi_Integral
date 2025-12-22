import streamlit as st
import numpy as np
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt

# Judul aplikasi
st.set_page_config(page_title="Kalkulator Integral - Pias Titik Tengah", layout="centered")
st.title("🧮 Kalkulator Integral Numerik")
st.subheader("Metode Pias Titik Tengah (Midpoint Rule)")

st.write("""
Website ini menghitung pendekatan nilai integral menggunakan **metode pias titik tengah**.
""")

# Input user
fungsi_input = st.text_input("Masukkan fungsi f(x)", value="x**2")
a = st.number_input("Batas bawah (a)", value=0.0)
b = st.number_input("Batas atas (b)", value=1.0)
n = st.number_input("Jumlah pias (n)", min_value=1, value=4, step=1)

# Tombol hitung
if st.button("Hitung Integral"):
    x = sp.symbols('x')
    fungsi = sp.sympify(fungsi_input)
    f = sp.lambdify(x, fungsi, "numpy")

    h = (b - a) / n
    titik_tengah = [a + (i + 0.5) * h for i in range(n)]
    nilai_f = [f(xi) for xi in titik_tengah]

    hasil_integral = h * sum(nilai_f)

    # Tabel hasil
    data = {
        "i": range(1, n + 1),
        "Titik Tengah": titik_tengah,
        "f(Titik Tengah)": nilai_f
    }
    df = pd.DataFrame(data)

    st.success(f"Hasil Aproksimasi Integral = **{hasil_integral:.6f}**")

    st.subheader("📋 Tabel Perhitungan")
    st.dataframe(df)

    # Grafik
    st.subheader("📈 Grafik Fungsi dan Pias")
    x_plot = np.linspace(a, b, 400)
    y_plot = f(x_plot)

    fig, ax = plt.subplots()
    ax.plot(x_plot, y_plot, label="f(x)")
    ax.bar(titik_tengah, nilai_f, width=h, alpha=0.3, edgecolor='black', label="Pias Titik Tengah")
    ax.legend()
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title("Metode Pias Titik Tengah")

    st.pyplot(fig)

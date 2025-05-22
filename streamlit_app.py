import streamlit as st

st.title("alisya ‼️")
st.image("20250515_110612.jpg",width=200)
st.subheader("nazlan naik meja tukang cimol")
st.write("jangan jadi kaya nazlan ya!")

#with col1:
st.header("Aplikasi Mengecek Nilai Genap/Ganjil)
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
  st.write(f"{angka} adalah Bilangan Genap")
else:
  st.write(f"{angka} adalah Bilangan Ganjil")

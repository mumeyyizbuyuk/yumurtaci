from functions import *
import streamlit as st

# YUMURTA SİL
st.subheader("Yumurta Sil")
liste = yumurtaturleri()
silyum = st.selectbox("Silmek İstediğiniz Yumurtayı Seçiniz", liste)
if st.button("Sil"):
    yumurtasil(silyum)
    st.success("Başarıyla Silindi")

# YUMURTA FİYATINI DÜZENLE
st.subheader("Yumurta Fiyat Düzenle")
liste = yumurtaturleri()
yumtur = st.selectbox("Fiyatını düzenlemek istediğiniz yumurtayı seçiniz", liste)
yenifiyat = st.number_input("Yeni fiyatı giriniz")
if st.button("Fiyatı Güncelle"):
    yumurtafiyatduzenle(yumtur, yenifiyat)
    st.success("Başarıyla güncellendi")

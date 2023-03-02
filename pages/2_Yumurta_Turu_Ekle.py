from functions import *
import streamlit as st

# YUMURTA TÜRÜ EKLE
yenitur = st.title("Eklemek istediğiniz yumurta türünü yazınız.")
fiyat = st.number_input("Adet fiyatı giriniz")
yeniyumtur = st.text_input("Elemek istediğiniz yumurta türünü yazınız.")
if st.button("Yumurta türü ekle"):
    tabloyap("yumurta_türleri", "(tür STRING, fiyat INTEGER)")
    veriekle("yumurta_türleri", yeniyumtur, fiyat)
    st.success("Başarılı Şekilde eklendi.")

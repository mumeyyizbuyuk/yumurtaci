from datetime import timedelta
from functions import *
import streamlit as st

# ÜYELİK EKLE
st.title("Lütfen Üyelik Oluşturunuz")

abonelikturulist = ["Haftalık", "Aylık"]
turlistesi = yumurtaturleri()

uyeismi = st.text_input("Lütfen üye isminizi giriniz")
abonelikturu = st.selectbox("Abonelik Türünü Seçiniz", abonelikturulist)
yumurturu = st.selectbox("Yumurta türünü seçiniz.", turlistesi)
teslimatgunu = st.date_input("Teslimat gününü seçiniz")
teslimatsaati = st.time_input("Teslimat saatini seçiniz.")
uyetelefon = st.text_input("Telefon numaranızı giriniz.")
yumurtafiyat = yumurtaturfiyatgetir(yumurturu)[0]*30
sonteslimattarihi = teslimatgunu + timedelta(days=365)
if st.button("Üyelik Ekle"):
    tabloyap("üyelik",
             "(isim STRING UNIQUE, abonelik_türü STRING, yumurta_türü STRING, fiyat INTEGER, teslimat_günü DATE, son_teslimat_günü DATE, teslimat_saati STRING, telefon STRING)")
    if uyeismi in uyeisimleri():
        st.error("Bu isimle kayıt bulunmaktadır. Başka bir isim giriniz")
    else:
        veriekle("üyelik", uyeismi, abonelikturu, yumurturu, yumurtafiyat, teslimatgunu, sonteslimattarihi, str(teslimatsaati), uyetelefon)
        st.success("Başarılı şekilde kayıt eklendi.")




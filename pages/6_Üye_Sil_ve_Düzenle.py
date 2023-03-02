
from datetime import timedelta
from functions import *
import streamlit as st

# ÜYE SİL (ÜYE İSİMLERİ UNIQUE OLDUĞU İÇİN İSİMDEN SİLİNMEYE GÖRE PLANLANMIŞTIR)
st.subheader("ÜYE Sil")
liste = uyeisimleri()
uyesilme = st.selectbox("Silmek İstediğiniz Üyeyi Seçiniz", liste)
if st.button("Sil"):
    uyesil(uyesilme)
    st.success("Başarıyla Silindi")

# ÜYE DÜZENLE (ÜYE İSİMLERİ UNIQUE OLDUĞU İÇİN İSİMDEN SİLİNMEYE GÖRE PLANLANMIŞTIR)
st.subheader("Üye Bilgileri Düzenle")
liste = uyeisimleri()
liste2 = yumurtaturleri()
liste3 = ["Haftalık", "Aylık"]

uyeisim = st.selectbox("Fiyatını bilgilerini düzenlemek istediğiniz Üyeyi seçiniz", liste)
yeniabonelik = st.selectbox("Yeni abonelik türünü seçiniz", liste3)
yeniyumurtatur = st.selectbox("Yeni yumurta türünü seçiniz", liste2)
yenitarih = st.date_input("Teslimat gününü seçiniz")
yenisaat = st.time_input("Teslimat saatini seçiniz.")
yumurtafiyat = yumurtaturfiyatgetir(yeniyumurtatur)[0] * 30
sonteslimat = yenitarih + timedelta(days=365)
if st.button("Bilgileri Güncelle"):
    uyebilgiduzenle(yeniabonelik, yeniyumurtatur, yumurtafiyat, yenitarih, sonteslimat, str(yenisaat), uyeisim)
    st.success("Başarıyla güncellendi")

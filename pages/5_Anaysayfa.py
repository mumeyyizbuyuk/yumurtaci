from functions import *
import streamlit as st
import datetime
import pandas as pd

# BUGÜN TESLİM EDİLECEKLER
st.title(":blue[Bugün teslim edilecekler]")
bugun = datetime.date.today()
tablo = pd.DataFrame(verigetir("üyelik"))
tablo.columns = ["İsim", "Abonelik Türü", "Yumurta Türü", "Fiyat", "Teslimat Günü", "Son Teslimat Günü",
                 "Teslimat Saati", "Telefon Numarası"]
tablo = tablo[tablo['Teslimat Günü'] == bugun.strftime("%Y-%m-%d")]
st.table(tablo)

# TOPLAM ÜYE SAYISI
st.title(":green[Toplam Üye Sayısı]")
st.subheader(f'Toplam Üye Sayısı {str(len(uyeisimleri()))}')

# BUGÜNÜN KAZANCI
st.title(":red[Bugünün Geliri]")
tablo = pd.DataFrame(verigetir("üyelik"))
tablo.columns = ["İsim", "Abonelik Türü", "Yumurta Türü", "Fiyat", "Teslimat Günü", "Son Teslimat Günü",
                 "Teslimat Saati", "Telefon Numarası"]
tablo = tablo[tablo['Teslimat Günü'] == bugun.strftime("%Y-%m-%d")]
gelir = tablo["Fiyat"].sum()
st.subheader(f'Bugün toplam kazanılacak miktar = {gelir} TL')

# BU AYIN KAZANÇLARI
st.title(":pink[Bu Ayın Kazancı]")
tablo1 = pd.DataFrame(verigetir("üyelik"))
tablo1.columns = ["İsim", "Abonelik Türü", "Yumurta Türü", "Fiyat", "Teslimat Günü", "Son Teslimat Günü",
                 "Teslimat Saati", "Telefon Numarası"]
st.table(tablo1)

from functions import *
import streamlit as st
import pandas as pd

# ÜYELERİ GÖSTER
st.subheader("Üyeler")
tablo = pd.DataFrame(verigetir("üyelik"))
tablo.columns = ["İsim", "Abonelik Türü", "Yumurta Türü", "Teslimat Günü", "Teslimat Saati", "Telefon Numarasu"]
st.table(tablo)

from functions import *
import streamlit as st

# YUMURTA TÜRLERİNİ GÖSTER
st.subheader("Yumurta Türleri")
tablo1 = yumurtaturleri()
st.table(tablo1)

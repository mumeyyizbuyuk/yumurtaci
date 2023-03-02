import sqlite3
import datetime

conn = sqlite3.connect("vt.db")
c = conn.cursor()


def tabloyap(tabloisim, sutunlar):
    conn = sqlite3.connect("vt.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS " + tabloisim + sutunlar)
    conn.commit()


def veriekle(tabloisim, *veriler):
    conn = sqlite3.connect("vt.db")
    c = conn.cursor()
    say = len(veriler)
    sor = "?," * say
    sor = sor[:-1]
    c.execute("INSERT INTO " + tabloisim + " VALUES(" + sor + ")", veriler)
    conn.commit()


def verigetir(tabloisim):
    conn = sqlite3.connect("vt.db")
    c = conn.cursor()
    c.execute("SELECT * FROM " + tabloisim)
    sonuc = c.fetchall()
    return sonuc


def yumurtaturleri():
    conn = sqlite3.connect("vt.db")
    c = conn.cursor()
    c.execute("SELECT tür FROM yumurta_türleri")
    sonuc = c.fetchall()
    liste = []
    for a in sonuc:
        liste.append(a[0])
    return liste


def yumurtaturfiyatgetir(yumurtaisim):
    conn = sqlite3.connect("vt.db")
    c = conn.cursor()
    c.execute("SELECT fiyat FROM yumurta_türleri WHERE tür=?", (yumurtaisim,))
    sonuc = c.fetchall()
    liste = []
    for a in sonuc:
        liste.append(a[0])
    return liste


def bugunteslimler():
    bugun = datetime.date.today()
    conn = sqlite3.connect("vt.db")
    c = conn.cursor()
    c.execute("SELECT fiyat FROM yumurta_türleri WHERE teslimat_günü=?", (bugun,))
    sonuc = c.fetchall()
    liste = []
    for a in sonuc:
        liste.append(a[0])
    return liste


def yumurtasil(yumurtaisim):
    conn = sqlite3.connect("vt.db")
    c = conn.cursor()
    c.execute("DELETE FROM yumurta_türleri WHERE tür=?", (yumurtaisim,))
    conn.commit()


def yumurtafiyatduzenle(tur, fiyat):
    conn = sqlite3.connect("vt.db")
    c = conn.cursor()
    c.execute("UPDATE yumurta_türleri SET fiyat=? WHERE tür=?", (fiyat, tur))
    conn.commit()


def uyesil(uyeisim):
    conn = sqlite3.connect("vt.db")
    c = conn.cursor()
    c.execute("DELETE FROM üyelik WHERE isim=?", (uyeisim,))
    conn.commit()


def uyeisimleri():
    conn = sqlite3.connect("vt.db")
    c = conn.cursor()
    c.execute("SELECT isim FROM üyelik")
    sonuc = c.fetchall()
    liste = []
    for a in sonuc:
        liste.append(a[0])
    return liste


def uyebilgiduzenle(aboneliktur, yenitur, yenifiyat, yenitarih, sonteslimat, yenisaat, uyeisim):
    conn = sqlite3.connect("vt.db")
    c = conn.cursor()
    c.execute(
        "UPDATE üyelik SET abonelik_türü=? , yumurta_türü=? , fiyat=? , teslimat_günü=? , son_teslimat_günü=? ,teslimat_saati=? WHERE isim=?",
        (aboneliktur, yenitur, yenifiyat, yenitarih, sonteslimat, yenisaat, uyeisim))
    conn.commit()

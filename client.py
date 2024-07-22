import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from biletiniAl import biletiniAl
from eventMagScraper import eventMagScraper


def sinema_verilerini_cek():
    
    try:
        selected_date = tarih_secici.get_date().strftime("%Y-%m-%d")[8:10]
        sinema_listesi.delete(0, tk.END) 
        global biletiniAl_instance 
        biletiniAl_instance = biletiniAl() 
        sinemalar = biletiniAl_instance.scrape_cinema(selected_date)
        for sinema in sinemalar:
            sinema_listesi.insert(tk.END, sinema)
    except Exception as e:
        film_detaylari["text"] = f"Hata: {e}"

def sinema_sec(event):
    """
    Sinema listesinde bir seçim yapıldığında filmleri gösterir.
    """
    try:
        global biletiniAl_instance
        selected_movie = sinema_listesi.get(sinema_listesi.curselection())
        descr , details = biletiniAl_instance.movie_descriptions(selected_movie)
        film_detaylari["text"] = f"Açıklama: {descr}\n\nDetaylar: {details}"
    except Exception as e:
        film_detaylari["text"] = f"Hata: {e}"

def etkinlik_verilerini_cek():
    """
    Etkinlik sekmesindeki butona tıklandığında çalışacak fonksiyon.
    eventmag.co'dan veri çeker ve arayüzde gösterir.
    """
    etkinlik_listesi.delete(0, tk.END) # Önceki listeyi temizle
    try:
        event_scraper = eventMagScraper() # Sınıf örneğini oluştur
        etkinlikler = event_scraper.scrape_all(5) # İlk 5 etkinliği çek
        for etkinlik in etkinlikler:
            etkinlik_listesi.insert(tk.END, f"{etkinlik[0]} ({etkinlik[1]}) - {etkinlik[2]} - {etkinlik[3]}")
    except Exception as e:
        etkinlik_detaylari["text"] = f"Hata: {e}"



pencere = tk.Tk()
pencere.title("Etkinlik ve Sinema Rehberi")
pencere.geometry("800x600")


sekmeler = ttk.Notebook(pencere)
sinema_sekmesi = ttk.Frame(sekmeler)
etkinlik_sekmesi = ttk.Frame(sekmeler)
sekmeler.add(sinema_sekmesi, text="Sinema")
sekmeler.add(etkinlik_sekmesi, text="Etkinlikler")
sekmeler.pack(expand=1, fill="both")


tarih_secici = DateEntry(sinema_sekmesi)
tarih_secici.pack()
sinema_listesi = tk.Listbox(sinema_sekmesi)
sinema_listesi.pack()
sinema_listesi.bind('<<ListboxSelect>>', sinema_sec) # Sinema seçme olayı
film_detaylari = tk.Label(sinema_sekmesi, text="")
film_detaylari.pack()
sinema_verilerini_cek_butonu = tk.Button(
    sinema_sekmesi, text="Verileri Çek", command=sinema_verilerini_cek
)
sinema_verilerini_cek_butonu.pack()

etkinlik_listesi = tk.Listbox(etkinlik_sekmesi)
etkinlik_listesi.pack()
etkinlik_detaylari = tk.Label(etkinlik_sekmesi, text="")
etkinlik_detaylari.pack()
etkinlik_verilerini_cek_butonu = tk.Button(
    etkinlik_sekmesi, text="Verileri Çek", command=etkinlik_verilerini_cek
)
etkinlik_verilerini_cek_butonu.pack()

pencere.mainloop()
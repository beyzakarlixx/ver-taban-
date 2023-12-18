from tkinter import *
from tkinter import ttk
import sqlite3

class EserUygulamasi:
    def __init__(self, veritabani_adi='beyzakarlı (1).db'):
        self.baglanti = sqlite3.connect(veritabani_adi)
        self.cursor = self.baglanti.cursor()
        self.pencere = Tk()
        self.pencere.title('Katalog: Eserleri Listele')
        self.pencere.geometry('800x300')
        self.pencere.resizable = True
        self.pencere['bg'] = '#FBE54E'

        self.eser_tablo_cercevesi = ttk.Frame(self.pencere, padding=25)
        self.eser_tablo_cercevesi.pack()

        self.eser_tablosu = ttk.Treeview(self.eser_tablo_cercevesi)

        self.eser_tablosu['columns'] = ('eserID', 'eserAdi', 'eserBasim', 'eserURL')

        self.eser_tablosu.column("#0", width=0, stretch=NO)
        self.eser_tablosu.column("eserID", anchor=CENTER, width=50)
        self.eser_tablosu.column("eserAdi", anchor=CENTER, width=250)
        self.eser_tablosu.column("eserBasim", anchor=CENTER, width=75)
        self.eser_tablosu.column("eserURL", anchor=CENTER, width=250)

        self.eser_tablosu.heading("#0", text="", anchor=CENTER)
        self.eser_tablosu.heading("eserID", text="Eser ID", anchor=CENTER)
        self.eser_tablosu.heading("eserAdi", text="Eser Adı", anchor=CENTER)
        self.eser_tablosu.heading("eserBasim", text="Eser Basım", anchor=CENTER)
        self.eser_tablosu.heading("eserURL", text="Eser URL", anchor=CENTER)

        self.veriyi_tabloya_ekle()

        self.eser_tablosu.pack()

        self.buton_cercevesi = ttk.Frame(self.pencere, padding=10)
        self.buton_cercevesi.pack()

        self.listele_butonu = Button(self.buton_cercevesi, text="Eserleri Listele", command=self.veriyi_tabloya_ekle)
        self.listele_butonu.grid(row=0, column=0, padx=5)

        self.ekle_butonu = Button(self.buton_cercevesi, text="Yeni Eser Ekle", command=self.yeni_eser_ekle_pencere)
        self.ekle_butonu.grid(row=0, column=1, padx=5)

        self.ara_butonu = Button(self.buton_cercevesi, text="Eserler İçinde Ara", command=self.eser_ara_pencere)
        self.ara_butonu.grid(row=0, column=2, padx=5)

        self.pencere.mainloop()

    def veriyi_tabloya_ekle(self):
        self.temizle_tablo()
        sorgu = self.cursor.execute("SELECT * FROM Eser")
        for index, eser in enumerate(sorgu.fetchall()):
            self.eser_tablosu.insert(parent='', index='end', iid=index, text='',
                                     values=(eser[0], eser[1], eser[2], eser[3]))

    def temizle_tablo(self):
        for item in self.eser_tablosu.get_children():
            self.eser_tablosu.delete(item)

    def yeni_eser_ekle_pencere(self):
        # Yeni eser ekleme penceresini açacak fonksiyonu buraya ekleyebilirsiniz.
        pass

    def eser_ara_pencere(self):
        # Eser arama penceresini açacak fonksiyonu buraya ekleyebilirsiniz.
        pass

if __name__ == "__main__":
    uygulama = EserUygulamasi()
import sys
import json
import hashlib
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel,
    QLineEdit, QTextEdit, QMessageBox, QScrollArea
)

class TarifUygulamasi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Yemek Tarifi Uygulaması")
        self.setGeometry(100, 100, 400, 500)
        self.kullanici = None  

        self.ana_layout = QVBoxLayout()
        self.setLayout(self.ana_layout)

        self.giris_ekrani()

    def giris_ekrani(self):
        self.temizle_layout()

        baslik = QLabel("Hoş Geldiniz!\nLütfen giriş yapın veya kayıt olun.")
        baslik.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.ana_layout.addWidget(baslik)

        btn_giris = QPushButton("Giriş Yap")
        btn_giris.clicked.connect(self.giris_sayfasi)
        self.ana_layout.addWidget(btn_giris)

        btn_kayit = QPushButton("Kayıt Ol")
        btn_kayit.clicked.connect(self.kayit_sayfasi)
        self.ana_layout.addWidget(btn_kayit)

    def kayit_sayfasi(self):
        self.temizle_layout()

        self.kayit_kadi = QLineEdit()
        self.kayit_kadi.setPlaceholderText("Kullanıcı adı")
        self.ana_layout.addWidget(self.kayit_kadi)

        self.kayit_sifre = QLineEdit()
        self.kayit_sifre.setPlaceholderText("Şifre")
        self.kayit_sifre.setEchoMode(QLineEdit.Password)
        self.ana_layout.addWidget(self.kayit_sifre)

        btn_kayit = QPushButton("Kayıt Ol")
        btn_kayit.clicked.connect(self.kayit_ol)
        self.ana_layout.addWidget(btn_kayit)

        btn_geri = QPushButton("Geri")
        btn_geri.clicked.connect(self.giris_ekrani)
        self.ana_layout.addWidget(btn_geri)

    def kayit_ol(self):
        kadi = self.kayit_kadi.text()
        sifre = self.kayit_sifre.text()

        if not kadi or not sifre:
            QMessageBox.warning(self, "Hata", "Kullanıcı adı ve şifre girin!")
            return

        try:
            with open("kullanicilar.json", "r", encoding="utf-8") as f:
                kullanicilar = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            kullanicilar = {}

        if kadi in kullanicilar:
            QMessageBox.warning(self, "Hata", "Bu kullanıcı adı zaten var!")
            return

        sifre_hash = hashlib.sha256(sifre.encode()).hexdigest()
        kullanicilar[kadi] = sifre_hash

        with open("kullanicilar.json", "w", encoding="utf-8") as f:
            json.dump(kullanicilar, f, ensure_ascii=False, indent=2)

        QMessageBox.information(self, "Başarılı", "Kayıt tamamlandı!")
        self.giris_ekrani()

    def giris_sayfasi(self):
        self.temizle_layout()

        self.giris_kadi = QLineEdit()
        self.giris_kadi.setPlaceholderText("Kullanıcı adı")
        self.ana_layout.addWidget(self.giris_kadi)

        self.giris_sifre = QLineEdit()
        self.giris_sifre.setPlaceholderText("Şifre")
        self.giris_sifre.setEchoMode(QLineEdit.Password)
        self.ana_layout.addWidget(self.giris_sifre)

        btn_giris = QPushButton("Giriş Yap")
        btn_giris.clicked.connect(self.giris_yap)
        self.ana_layout.addWidget(btn_giris)

        btn_geri = QPushButton("Geri")
        btn_geri.clicked.connect(self.giris_ekrani)
        self.ana_layout.addWidget(btn_geri)

    def giris_yap(self):
        kadi = self.giris_kadi.text()
        sifre = self.giris_sifre.text()

        try:
            with open("kullanicilar.json", "r", encoding="utf-8") as f:
                kullanicilar = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            kullanicilar = {}

        sifre_hash = hashlib.sha256(sifre.encode()).hexdigest()

        if kullanicilar.get(kadi) == sifre_hash:
            self.kullanici = kadi
            self.ana_menu()
        else:
            QMessageBox.warning(self, "Hata", "Geçersiz kullanıcı adı veya şifre!")

    def ana_menu(self):
        self.temizle_layout()

        hosgeldin = QLabel(f"Hoş geldin, {self.kullanici}!")
        hosgeldin.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.ana_layout.addWidget(hosgeldin)

        btn_tarif_ekle = QPushButton("Tarif Ekle")
        btn_tarif_ekle.clicked.connect(self.tarif_ekle_sayfasi)
        self.ana_layout.addWidget(btn_tarif_ekle)

        btn_tarifleri_listele = QPushButton("Tarifleri Listele")
        btn_tarifleri_listele.clicked.connect(self.tarifleri_listele)
        self.ana_layout.addWidget(btn_tarifleri_listele)

        btn_tarif_ara = QPushButton("Tarif Ara")
        btn_tarif_ara.clicked.connect(self.tarif_ara_sayfasi)
        self.ana_layout.addWidget(btn_tarif_ara)

        btn_cikis = QPushButton("Çıkış Yap")
        btn_cikis.clicked.connect(self.cikis_yap)
        self.ana_layout.addWidget(btn_cikis)

    def cikis_yap(self):
        self.kullanici = None
        self.giris_ekrani()

    def tarif_ekle_sayfasi(self):
        self.temizle_layout()

        self.ad_alani = QLineEdit()
        self.ad_alani.setPlaceholderText("Tarif adı")
        self.ana_layout.addWidget(self.ad_alani)

        self.malzeme_alani = QTextEdit()
        self.malzeme_alani.setPlaceholderText("Malzemeleri her satıra bir tane olacak şekilde yazın")
        self.ana_layout.addWidget(self.malzeme_alani)

        self.asama_layout = QVBoxLayout()
        self.asama_editorleri = []

        self.asama_widget = QWidget()
        self.asama_widget.setLayout(self.asama_layout)
        self.ana_layout.addWidget(self.asama_widget)

        self.asama_ekle()

        btn_asama_ekle = QPushButton("+ Aşama Ekle")
        btn_asama_ekle.clicked.connect(self.asama_ekle)
        self.ana_layout.addWidget(btn_asama_ekle)

        btn_kaydet = QPushButton("Kaydet")
        btn_kaydet.clicked.connect(self.tarif_kaydet)
        self.ana_layout.addWidget(btn_kaydet)

        btn_geri = QPushButton("Geri")
        btn_geri.clicked.connect(self.ana_menu)
        self.ana_layout.addWidget(btn_geri)

    def asama_ekle(self):
        yeni_asama = QLineEdit()
        yeni_asama.setPlaceholderText(f"Aşama {len(self.asama_editorleri)+1}")
        self.asama_layout.addWidget(yeni_asama)
        self.asama_editorleri.append(yeni_asama)

    def tarif_kaydet(self):
        ad = self.ad_alani.text()
        malzemeler = self.malzeme_alani.toPlainText().split('\n')
        asamalar = [a.text() for a in self.asama_editorleri if a.text().strip()]

        if not ad or not malzemeler or not asamalar:
            QMessageBox.warning(self, "Hata", "Tüm alanları doldurun!")
            return

        try:
            with open("tarifler.json", "r", encoding="utf-8") as dosya:
                tarifler = json.load(dosya)
        except (FileNotFoundError, json.JSONDecodeError):
            tarifler = []

        tarif = {
            "ad": ad,
            "malzemeler": malzemeler,
            "asamalar": asamalar,
            "ekleyen": self.kullanici
        }
        tarifler.append(tarif)

        with open("tarifler.json", "w", encoding="utf-8") as dosya:
            json.dump(tarifler, dosya, ensure_ascii=False, indent=2)

        QMessageBox.information(self, "Başarılı", "Tarif başarıyla kaydedildi!")
        self.ana_menu()

    def tarifleri_listele(self):
        self.temizle_layout()

        try:
            with open("tarifler.json", "r", encoding="utf-8") as dosya:
                tarifler = json.load(dosya)
        except:
            tarifler = []

        if not tarifler:
            self.ana_layout.addWidget(QLabel("Hiç tarif yok."))
        else:
            scroll = QScrollArea()
            scroll_widget = QWidget()
            scroll_layout = QVBoxLayout(scroll_widget)

            for tarif in tarifler:
                ad = tarif.get("ad", "Adsız")
                malzemeler = "\n".join(tarif.get("malzemeler", []))
                asamalar = "\n".join(tarif.get("asamalar", []))
                ekleyen = tarif.get("ekleyen", "Bilinmiyor")

                etiket = QLabel(f"🍽️ {ad}\n\nMalzemeler:\n{malzemeler}\n\nAşamalar:\n{asamalar}\n\n👤 Ekleyen: {ekleyen}")
                etiket.setStyleSheet("margin: 10px; padding: 10px; border: 1px solid gray;")
                scroll_layout.addWidget(etiket)

            scroll.setWidget(scroll_widget)
            scroll.setWidgetResizable(True)
            self.ana_layout.addWidget(scroll)

        btn_geri = QPushButton("Geri")
        btn_geri.clicked.connect(self.ana_menu)
        self.ana_layout.addWidget(btn_geri)

    def tarif_ara_sayfasi(self):
        self.temizle_layout()

        self.aranacak_kelime = QLineEdit()
        self.aranacak_kelime.setPlaceholderText("Aranacak tarif adı...")
        self.ana_layout.addWidget(self.aranacak_kelime)

        btn_ara = QPushButton("Ara")
        btn_ara.clicked.connect(self.tarif_ara)
        self.ana_layout.addWidget(btn_ara)

        btn_geri = QPushButton("Geri")
        btn_geri.clicked.connect(self.ana_menu)
        self.ana_layout.addWidget(btn_geri)

    def tarif_ara(self):
        kelime = self.aranacak_kelime.text().lower()
        self.temizle_layout()

        try:
            with open("tarifler.json", "r", encoding="utf-8") as dosya:
                tarifler = json.load(dosya)
        except:
            tarifler = []

        bulunanlar = [t for t in tarifler if kelime in t.get("ad", "").lower()]

        if not bulunanlar:
            self.ana_layout.addWidget(QLabel("Eşleşen tarif bulunamadı."))
        else:
            for tarif in bulunanlar:
                ad = tarif.get("ad", "Adsız")
                malzemeler = "\n".join(tarif.get("malzemeler", []))
                asamalar = "\n".join(tarif.get("asamalar", []))
                ekleyen = tarif.get("ekleyen", "Bilinmiyor")

                etiket = QLabel(f"🍽️ {ad}\n\nMalzemeler:\n{malzemeler}\n\nAşamalar:\n{asamalar}\n\n👤 Ekleyen: {ekleyen}")
                etiket.setStyleSheet("margin: 10px; padding: 10px; border: 1px solid gray;")
                self.ana_layout.addWidget(etiket)

        btn_geri = QPushButton("Geri")
        btn_geri.clicked.connect(self.ana_menu)
        self.ana_layout.addWidget(btn_geri)

    def temizle_layout(self):
        while self.ana_layout.count():
            item = self.ana_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = TarifUygulamasi()
    pencere.show()
    sys.exit(app.exec_())

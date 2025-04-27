from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import json
import os

class GirisEkrani(QWidget):
    def __init__(self, giris_basari_callback):
        super().__init__()

        self.giris_basari_callback = giris_basari_callback

        self.setWindowTitle("Giriş Yap")
        self.setGeometry(300, 300, 300, 200)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.kullanici_alani = QLineEdit()
        self.kullanici_alani.setPlaceholderText("Kullanıcı adı")
        self.layout.addWidget(self.kullanici_alani)

        self.sifre_alani = QLineEdit()
        self.sifre_alani.setPlaceholderText("Şifre")
        self.sifre_alani.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.sifre_alani)

        self.giris_buton = QPushButton("Giriş Yap")
        self.giris_buton.clicked.connect(self.giris_yap)
        self.layout.addWidget(self.giris_buton)

        self.kayit_buton = QPushButton("Yeni Kullanıcı Kaydı")
        self.kayit_buton.clicked.connect(self.kayit_ol)
        self.layout.addWidget(self.kayit_buton)

        if not os.path.exists("kullanicilar.json"):
            with open("kullanicilar.json", "w", encoding="utf-8") as f:
                json.dump([], f)

    def giris_yap(self):
        ad = self.kullanici_alani.text()
        sifre = self.sifre_alani.text()

        with open("kullanicilar.json", "r", encoding="utf-8") as f:
            kullanicilar = json.load(f)

        for k in kullanicilar:
            if k["ad"] == ad and k["sifre"] == sifre:
                self.giris_basari_callback(ad)
                self.close()
                return

        QMessageBox.warning(self, "Hata", "Kullanıcı adı veya şifre yanlış.")

    def kayit_ol(self):
        ad = self.kullanici_alani.text()
        sifre = self.sifre_alani.text()

        if not ad or not sifre:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")
            return

        with open("kullanicilar.json", "r", encoding="utf-8") as f:
            kullanicilar = json.load(f)

        for k in kullanicilar:
            if k["ad"] == ad:
                QMessageBox.warning(self, "Uyarı", "Bu kullanıcı adı zaten alınmış.")
                return

        kullanicilar.append({"ad": ad, "sifre": sifre})

        with open("kullanicilar.json", "w", encoding="utf-8") as f:
            json.dump(kullanicilar, f, ensure_ascii=False, indent=4)

        QMessageBox.information(self, "Başarılı", "Kayıt yapıldı, şimdi giriş yapabilirsiniz.")


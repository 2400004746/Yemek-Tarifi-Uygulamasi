# Yemek Tarifi Uygulaması - Kullanım Kılavuzu

Bu kılavuz, Yemek Tarifi Uygulaması'nın nasıl kullanılacağını adım adım açıklar.

## Başlangıç

1. Uygulama dosyalarını bilgisayarınıza indirin veya kopyalayın.
2. Bilgisayarınızda Python 3 ve PyQt5 kütüphanesinin kurulu olduğundan emin olun.
   - Kurulum için terminale/komut satırına şu komutu yazabilirsiniz:
     ```bash
     pip install PyQt5
     ```
3. `main_window.py` dosyasını çalıştırarak uygulamayı başlatın:
   ```bash
   python main_window.py
   ```

---

## Kullanıcı Girişi

- Uygulama açıldığında ilk olarak **kullanıcı giriş ekranı** karşınıza gelir.
- Var olan bir kullanıcı adınızı ve şifrenizi girerek giriş yapabilirsiniz.
- Şu anda uygulamada yeni kullanıcı kaydetme ekranı bulunmamaktadır. (İsterseniz `kullanicilar.json` dosyasına manuel olarak kullanıcı ekleyebilirsiniz.)

---

## Ana Sayfa

Giriş yaptıktan sonra ana sayfaya yönlendirilirsiniz.

Burada şunları yapabilirsiniz:

- 📋 **Tarifleri Görüntüle**:  
  - Var olan tüm yemek tariflerini listeleyebilirsiniz.
  
- 🔍 **Tarif Ara**:  
  - Belirli bir yemek tarifini adıyla arayabilirsiniz.

- ➕ **Tarif Ekle**:  
  - Yeni bir yemek tarifi eklemek için:
    - Yemek adını ve malzemeleri girin.
    - Aşamaları sırayla ekleyin.
    - "Tarifi Kaydet" butonuna tıklayın.

---

## Tarif Ekleme

1. "Tarif Ekle" sekmesine tıklayın.
2. Yemek adını yazın.
3. Malzeme listesini girin (her malzemeyi virgülle ayırabilirsiniz).
4. Aşamaları eklemek için "+" butonuna tıklayın. Her aşamayı ayrı ayrı girebilirsiniz.
5. Tüm bilgiler tamamlandığında **"Kaydet"** butonuna basın.
6. Tarifiniz `tarifler.json` dosyasına kaydedilecektir.

---

## Veriler

- **kullanicilar.json**:  
  Kayıtlı kullanıcı adları ve şifreler burada tutulur.

- **tarifler.json**:  
  Tüm yemek tarifleri burada saklanır. Uygulama kapatılsa bile tarifler burada korunur.

---

## Sıkça Sorulan Sorular (SSS)

> ❓ Tarifler kaybolur mu?  
> Hayır. Tarifler `tarifler.json` dosyasına kaydedilir ve uygulama her açıldığında buradan yüklenir.

> ❓ Uygulama neden çalışmıyor?  
> Python 3 ve PyQt5 yüklü mü kontrol edin. Hala sorun varsa hata mesajını kontrol ederek çözüm arayabilirsiniz.

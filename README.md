# 📰 Django Makale Uygulaması

Bu proje, Django framework'ü ile geliştirilmiş basit bir makale paylaşım sistemidir. Kullanıcılar kayıt olabilir, giriş yapabilir, makaleler oluşturabilir, güncelleyebilir, silebilir ve yorum yapabilir.

## 🚀 Özellikler

- ✅ Kullanıcı kayıt & giriş sistemi (Login/Logout)
- ✅ Makale ekleme
- ✅ Makale güncelleme
- ✅ Makale silme
- ✅ Yorum ekleme
- ✅ Yorumları görüntüleme
- ✅ Django admin paneli

## 🛠️ Kurulum Adımları

Aşağıdaki adımları izleyerek projeyi yerel bilgisayarınızda çalıştırabilirsiniz:

```bash
# 1. Depoyu klonlayın
git clone https://github.com/BarlasTR/article-project-django.git
cd article-project-django

# 2. Sanal ortam oluşturun ve aktif edin
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate

# 3. Gerekli paketleri yükleyin
pip install -r requirements.txt

# 4. Veritabanını migrate edin
python manage.py migrate

# 5. Süper kullanıcı oluşturun
python manage.py createsuperuser

# 6. Sunucuyu başlatın
python manage.py runserver
```

## 📰 Admin Hesabı Bilgileri

Kullanıcı Adı: test  
Şifre: test



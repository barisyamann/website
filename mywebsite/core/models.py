# core/models.py

from django.db import models

class Duyuru(models.Model):
    baslik = models.CharField(max_length=200)
    aciklama = models.TextField()
    tarih = models.DateTimeField(auto_now_add=True)
    resim = models.ImageField(upload_to='duyurular/', blank=True, null=True)  # İsteğe bağlı resim alanı

    def __str__(self):
        return self.baslik

# core/admin.py

from django.contrib import admin
from .models import Duyuru

class DuyuruAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'tarih')
    search_fields = ('baslik',)

admin.site.register(Duyuru, DuyuruAdmin)

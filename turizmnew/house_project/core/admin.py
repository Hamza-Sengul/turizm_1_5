# core/admin.py

from django.contrib import admin
from .models import Category, House, HouseImage, SiteSettings

class HouseImageInline(admin.TabularInline):
    model = HouseImage
    extra = 1  # Her ev için varsayılan ek resim sayısı

class HouseAdmin(admin.ModelAdmin):
    inlines = [HouseImageInline]

admin.site.register(Category)
admin.site.register(House, HouseAdmin)
admin.site.register(SiteSettings)

# core/models.py

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategori Adı")
    photo = models.ImageField(upload_to='category_photos/', verbose_name="Kategori Fotoğrafı")

    def __str__(self):
        return self.name

class House(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='houses', verbose_name="Kategori")
    name = models.CharField(max_length=100, verbose_name="Ev Adı")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Fiyat")
    description = models.TextField(verbose_name="Açıklama")

    def __str__(self):
        return self.name

class HouseImage(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='house_images/', verbose_name="Ev Resmi")

    def __str__(self):
        return f"{self.house.name} Resmi"

class SiteSettings(models.Model):
    navbar_logo = models.ImageField(upload_to='site_logos/', verbose_name="Navbar Logosu")
    footer_logo = models.ImageField(upload_to='site_logos/', verbose_name="Footer Logosu")

    def __str__(self):
        return "Site Ayarları"

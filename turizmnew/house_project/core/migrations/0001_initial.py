# Generated by Django 5.1.4 on 2025-03-17 22:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Kategori Adı')),
                ('photo', models.ImageField(upload_to='category_photos/', verbose_name='Kategori Fotoğrafı')),
            ],
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('navbar_logo', models.ImageField(upload_to='site_logos/', verbose_name='Navbar Logosu')),
                ('footer_logo', models.ImageField(upload_to='site_logos/', verbose_name='Footer Logosu')),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ev Adı')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Fiyat')),
                ('description', models.TextField(verbose_name='Açıklama')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='houses', to='core.category', verbose_name='Kategori')),
            ],
        ),
    ]

# Generated by Django 2.1.2 on 2018-12-03 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokopedia', '0025_auto_20181202_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='barang_diskon_harga_asli',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]

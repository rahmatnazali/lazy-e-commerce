# Generated by Django 2.1.2 on 2018-11-30 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tokopedia', '0010_auto_20181130_1315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='good',
            old_name='dilihat',
            new_name='barang_dilihat',
        ),
        migrations.RenameField(
            model_name='good',
            old_name='harga_asli',
            new_name='barang_harga_asli',
        ),
        migrations.RenameField(
            model_name='good',
            old_name='harga_jual',
            new_name='barang_harga_jual',
        ),
        migrations.RenameField(
            model_name='good',
            old_name='informasi_produk',
            new_name='barang_informasi_produk',
        ),
        migrations.RenameField(
            model_name='good',
            old_name='is_produk_unggulan',
            new_name='barang_is_unggulan',
        ),
        migrations.RenameField(
            model_name='good',
            old_name='nama_barang',
            new_name='barang_nama',
        ),
        migrations.RenameField(
            model_name='good',
            old_name='terjual',
            new_name='barang_terjual',
        ),
        migrations.RenameField(
            model_name='good',
            old_name='link_barang',
            new_name='barang_url',
        ),
    ]

# Generated by Django 3.0.6 on 2021-02-02 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20210201_1159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='name',
            new_name='product',
        ),
    ]
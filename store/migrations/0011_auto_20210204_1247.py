# Generated by Django 3.0.6 on 2021-02-04 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20210202_1451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='datetime',
            new_name='date',
        ),
    ]

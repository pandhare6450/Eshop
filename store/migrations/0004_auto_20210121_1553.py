# Generated by Django 3.0.6 on 2021-01-21 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
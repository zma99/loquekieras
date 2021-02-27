# Generated by Django 3.1.7 on 2021-02-27 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=10)),
                ('marca', models.CharField(max_length=15)),
                ('modelo', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
    ]

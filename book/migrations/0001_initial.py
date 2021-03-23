# Generated by Django 3.1.2 on 2021-03-23 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='Book Name')),
                ('cover_image', models.ImageField(upload_to='cover_images', verbose_name='Cover Image')),
                ('description', models.TextField(max_length=500, verbose_name='Description')),
                ('download', models.FileField(upload_to='downloads')),
            ],
        ),
    ]
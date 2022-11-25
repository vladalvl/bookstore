# Generated by Django 4.1.2 on 2022-10-22 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
    ]

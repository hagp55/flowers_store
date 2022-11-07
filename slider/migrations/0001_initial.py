# Generated by Django 4.1.2 on 2022-11-07 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True, verbose_name='Заголовок')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Текст')),
                ('photo', models.ImageField(upload_to='slider/photos/', verbose_name='Выбрать картинку')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайды',
                'ordering': ('pk',),
            },
        ),
    ]

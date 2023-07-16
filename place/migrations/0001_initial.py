# Generated by Django 3.2.20 on 2023-07-16 16:46

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('description_short', models.CharField(max_length=500, verbose_name='Short Description')),
                ('description_long', tinymce.models.HTMLField(blank=True, verbose_name='Полное описание')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('latitude', models.FloatField(verbose_name='Широта')),
            ],
            options={
                'verbose_name': 'place',
                'verbose_name_plural': 'places',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('position', models.IntegerField(db_index=True, default=1)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='place.place')),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
                'ordering': ('position',),
            },
        ),
    ]

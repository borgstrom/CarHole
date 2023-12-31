# Generated by Django 4.2.4 on 2023-08-19 17:55

import cars.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=100, verbose_name='Make')),
                ('model', models.CharField(max_length=100, verbose_name='Model')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Year')),
                ('vin', models.CharField(max_length=100, verbose_name='VIN')),
                ('license', models.CharField(max_length=32, verbose_name='License plate')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('picture', models.FileField(blank=True, upload_to=cars.models.car_picture_upload_to, verbose_name='Photo')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.SmallIntegerField(choices=[(0, 'Note'), (1, 'Ownership change'), (2, 'Gasoline'), (3, 'Maintenance')], verbose_name='Record Type')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='cars.car')),
            ],
        ),
        migrations.CreateModel(
            name='RecordFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=cars.models.record_file_upload_to, verbose_name='File')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Description')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='cars.record')),
            ],
        ),
    ]

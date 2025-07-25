# Generated by Django 4.2.21 on 2025-07-17 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_workerschedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalMaterials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('image', models.ImageField(blank=True, upload_to='additional_materials', verbose_name='Изображение')),
                ('note', models.TextField(blank=True, verbose_name='Примечание')),
            ],
            options={
                'verbose_name': 'Дополнительные материалы',
                'verbose_name_plural': 'Дополнительные материалы',
            },
        ),
    ]

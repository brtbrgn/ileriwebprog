# Generated by Django 5.0.1 on 2024-01-10 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spicy', '0002_item_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='test'),
            preserve_default=False,
        ),
    ]

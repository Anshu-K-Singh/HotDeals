# Generated by Django 5.0.7 on 2024-07-13 17:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='Category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='item.category'),
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='item_images'),
        ),
    ]
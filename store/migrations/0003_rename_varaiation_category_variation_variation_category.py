# Generated by Django 5.0.2 on 2024-02-25 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='varaiation_category',
            new_name='variation_category',
        ),
    ]

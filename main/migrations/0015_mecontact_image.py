# Generated by Django 5.0.1 on 2024-02-01 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_aboutme_image_alter_partner_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mecontact',
            name='image',
            field=models.ImageField(default=1, upload_to='main/contact'),
            preserve_default=False,
        ),
    ]

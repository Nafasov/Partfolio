# Generated by Django 5.0.1 on 2024-02-02 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_mecontact_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='cvv',
            field=models.FileField(default=1, upload_to='main/cvv'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mecontact',
            name='email_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='partner',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]

# Generated by Django 5.0.1 on 2024-02-02 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_aboutme_cvv_mecontact_email_link_partner_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mecontact',
            name='li_me',
            field=models.URLField(blank=True, null=True),
        ),
    ]
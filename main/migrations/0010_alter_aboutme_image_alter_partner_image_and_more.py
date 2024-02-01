# Generated by Django 5.0.1 on 2024-02-01 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_award_created_date_alter_contacts_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/about'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='image',
            field=models.ImageField(null=True, upload_to='images/partner/images'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(upload_to='images/project'),
        ),
        migrations.AlterField(
            model_name='services',
            name='icon',
            field=models.ImageField(upload_to='images/services'),
        ),
    ]

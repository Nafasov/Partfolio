# Generated by Django 5.0.1 on 2024-01-29 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_aboutme_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='address',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='date',
            field=models.DateField(verbose_name='1233'),
        ),
    ]
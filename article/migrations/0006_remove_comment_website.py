# Generated by Django 5.0.1 on 2024-02-03 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_comment_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='website',
        ),
    ]
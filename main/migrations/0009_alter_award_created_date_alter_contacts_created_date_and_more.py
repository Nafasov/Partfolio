# Generated by Django 5.0.1 on 2024-01-31 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_skills_last_month_skills_last_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='skills',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='skills',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

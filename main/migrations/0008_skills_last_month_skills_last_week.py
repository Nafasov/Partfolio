# Generated by Django 5.0.1 on 2024-01-31 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_award_contacts_done_education_experience_mecontact_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='Last_month',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='skills',
            name='Last_week',
            field=models.IntegerField(default=0),
        ),
    ]

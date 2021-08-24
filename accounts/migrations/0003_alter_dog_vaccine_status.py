# Generated by Django 3.2.6 on 2021-08-23 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_dog_breeder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='vaccine_status',
            field=models.CharField(blank=True, choices=[('Up-to-date', 'Up-to-date'), ('Not Up-to-date', 'Not Up-to-date'), ('Rabies', 'Rabies'), ('Parvo', 'Parvo'), ('Distemper', 'Distemper'), ('Bordetella', 'Bordetella'), ('Hepatitis', 'Hepatitis'), ('Influenza', 'Influenza'), ('Heartworm', 'Heartworm'), ('Leptospirosis', 'Leptospirosis'), ('Lyme Disease', 'Lyme Disease')], max_length=20, null=True),
        ),
    ]
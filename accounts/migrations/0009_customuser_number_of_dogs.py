# Generated by Django 3.2.6 on 2021-08-16 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_customuser_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='number_of_dogs',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
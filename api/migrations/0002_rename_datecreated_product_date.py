# Generated by Django 4.0.2 on 2022-04-13 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='datecreated',
            new_name='date',
        ),
    ]
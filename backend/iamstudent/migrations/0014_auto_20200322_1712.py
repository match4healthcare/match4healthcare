# Generated by Django 3.0.4 on 2020-03-22 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iamstudent', '0013_auto_20200322_1508'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='skill_beatmungsgerätebedienen',
            new_name='skill_beatmungsgeraetebedienen',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='skill_labortätigkeiten',
            new_name='skill_labortaetigkeiten',
        ),
    ]
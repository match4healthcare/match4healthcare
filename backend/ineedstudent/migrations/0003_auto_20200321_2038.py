# Generated by Django 3.0.4 on 2020-03-21 20:38

from django.db import migrations, models
import iamstudent.models


class Migration(migrations.Migration):

    dependencies = [
        ('ineedstudent', '0002_auto_20200321_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='plz',
            field=models.IntegerField(null=True, validators=[iamstudent.models.validate_plz]),
        ),
    ]
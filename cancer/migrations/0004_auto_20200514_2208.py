# Generated by Django 2.2 on 2020-05-14 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cancer', '0003_auto_20200514_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='Emergency',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
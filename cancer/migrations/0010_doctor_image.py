# Generated by Django 2.2 on 2020-05-16 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cancer', '0009_auto_20200516_0136'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='image',
            field=models.ImageField(default=0, upload_to='Images/'),
            preserve_default=False,
        ),
    ]
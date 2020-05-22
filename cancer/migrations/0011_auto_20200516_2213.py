# Generated by Django 2.2 on 2020-05-16 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cancer', '0010_doctor_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='patient_image',
            field=models.ImageField(null=True, upload_to='patientimages/'),
        ),
        migrations.AddField(
            model_name='staff',
            name='image',
            field=models.ImageField(default=0, upload_to='staffimage/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctor',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='designation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='doctorimages/'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='sex',
            field=models.CharField(blank=True, choices=[('Male', 'M'), ('Female', 'F'), ('Other', 'Other')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='Age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='designation',
            field=models.CharField(blank=True, choices=[('MLSS', 'MLSS'), ('peon', 'PEON'), ('sister', 'SISTER')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='machine',
            field=models.CharField(blank=True, choices=[('Teletherapy', 'Teletherapy'), ('Brachy Therapy', 'Brachy Therapy'), ('Medical Technologist', 'Medical technologist'), ('MLSS', 'MLSS'), ('N/A', 'N/A')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='sex',
            field=models.CharField(blank=True, choices=[('Male', 'M'), ('Female', 'F'), ('Other', 'Other')], max_length=100, null=True),
        ),
    ]
# Generated by Django 2.2 on 2020-05-15 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cancer', '0006_auto_20200515_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('sex', models.CharField(choices=[('Male', 'M'), ('Female', 'F'), ('Other', 'Other')], max_length=100)),
                ('designation', models.TextField()),
                ('number', models.IntegerField()),
                ('email', models.EmailField(max_length=200)),
                ('address', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Doctors',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='Visit',
        ),
        migrations.AddField(
            model_name='patient',
            name='additionalinformation',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='Height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='patient',
            name='NID',
            field=models.IntegerField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='patient',
            name='blood_groups',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O-'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=10),
        ),
    ]
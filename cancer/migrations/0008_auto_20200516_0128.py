# Generated by Django 2.2 on 2020-05-15 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cancer', '0007_auto_20200515_2207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='electryolye',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='folllowup',
        ),
        migrations.AddField(
            model_name='patient',
            name='electrolyte',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='followup',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='designation',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='sex',
            field=models.CharField(choices=[('Male', 'M'), ('Female', 'F'), ('Other', 'Other')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Bone_marrow_Study',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Bronchoscopy',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='COLONOSCOPY',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Cancer_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Casesummary',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Concomitant',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Contact',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Drughistory',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='ECG',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='ECHO_CARDIOgraphy',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='ENDOSCOPYofupperGIT',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Investigation',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='LDH',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Nasopharyngoscopy',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Physicalexamfindings',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='SERUM_PROTEIN_ELECTROPHORESIS',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='TSH',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Treatmentapproach',
            field=models.CharField(choices=[('Curative', (('surgery', 'surgery'), ('chemotherapy', 'Chemotherapy'), ('immunotherapy', 'Immunotherapy'), ('hormone', 'Hormone Therapy'), ('other', 'Other'))), ('Palliative', (('chemotherapy', 'Chemotherapy'), ('immunotherapy', 'Immunotherapy'), ('hormone', 'Hormone Therapy'), ('other', 'Other'))), ('Others', 'Others')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='additionalinformation',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='additionaltest',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='additionaltreatment',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='adjuvant',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='blood_groups',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O-'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='bonescan',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='cbc',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='ctscan',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='diagnosis',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='familyhistory',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='familyhistoryofmalignancy',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='father',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='fnac',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='fol',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='grading',
            field=models.CharField(choices=[('1', 'I'), ('2', 'II'), ('3', 'III')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='histopathology',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='ihc',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='lft',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='maritial_status',
            field=models.CharField(choices=[('Married', 'Married'), ('Unmarrried', 'Unmarried')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='mother',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='mri',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='new_adjuvant',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='occupation',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='papsmearcytology',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pasthistorydisease',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='personalhistory',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='petct',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pvf',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='rft',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.CharField(choices=[('Male', 'M'), ('Female', 'F'), ('Other', 'Other')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='staging',
            field=models.CharField(choices=[('1', 'I'), ('2', 'II'), ('3', 'III'), ('4', 'IV')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='tumourmarker',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='ultrasound',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='urineRE',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='xraychest',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='Age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='designation',
            field=models.CharField(choices=[('MLSS', 'MLSS'), ('peon', 'PEON'), ('sister', 'SISTER')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='machine',
            field=models.CharField(choices=[('Teletherapy', 'Teletherapy'), ('Brachy Therapy', 'Brachy Therapy'), ('Medical Technologist', 'Medical technologist'), ('MLSS', 'MLSS'), ('N/A', 'N/A')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='sex',
            field=models.CharField(choices=[('Male', 'M'), ('Female', 'F'), ('Other', 'Other')], max_length=100, null=True),
        ),
    ]
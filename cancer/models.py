from django.db import models

# Create your models here.
class Patient(models.Model):
    created=models.DateField(auto_now_add=True)
    registration=models.CharField(max_length=10,unique=True,null=False,blank=False)
    NID=models.IntegerField(unique=True,null=True,blank=True)
    Cancer_id=models.CharField(max_length=100,unique=True,blank=True,null=True)
    #Visit=models.IntegerField()
    fname=models.CharField(max_length=200,blank=False,null=False)
    lname=models.CharField(max_length=200,blank=False,null=False)
    mother=models.CharField(max_length=100,blank=True,null=True)
    father=models.CharField(max_length=100,blank=True,null=True)
    address=models.TextField(blank=False,null=False)

    patient_image=models.ImageField(upload_to='patientimages/',blank=True,null=True)
    Contact=models.IntegerField(blank=False,null=False)
    Emergency=models.IntegerField(blank=True,null=True)
    Age=models.IntegerField(blank=False,null=False)
    gender=[
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    ]
    sex=models.CharField(max_length=20,blank=False,choices=gender,null=False)
    status=[
        ('Married','Married'),
        ('Unmarried','Unmarried'),
    ]
    maritial_status=models.CharField(max_length=20,blank=False,choices=status,null=False)
    occupation=models.TextField(blank=True,null=True)
    bgroup=[
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('O+','O-'),
        ('O-','O-'),
        ('AB+','AB+'),
        ('AB-','AB-') 
    ]
    blood_groups=models.CharField(max_length=10,blank=True,choices=bgroup,null=True)
    Weight=models.DecimalField(decimal_places=2,max_digits=10,blank=True,null=True)
    Height=models.DecimalField(decimal_places=2,max_digits=10,blank=True,null=True)
    BMI=models.DecimalField(decimal_places=2,max_digits=10,blank=True,null=True)
    Concomitant=models.TextField(blank=True,null=True)
    historyfiles=models.FileField(upload_to='patienthistorydoc/',blank=True,null=True)

    familyhistory=models.TextField(blank=True,null=True)
    familyhistoryofmalignancy=models.TextField(blank=True,null=True)
    personalhistory=models.TextField(blank=True,null=True)
    pasthistorydisease=models.TextField(blank=True,null=True)
    Drughistory=models.TextField(blank=True,null=True)
    physicalexamfiles=models.FileField(upload_to='patientphysicalexamdoc/',blank=True,null=True)
    Physicalexamfindings=models.TextField(blank=True,null=True)
    Casesummary=models.TextField(blank=True,null=True)
    diagnosis=models.TextField(blank=True,null=True)
    Investigation=models.TextField(blank=True,null=True)
    investigationfiles=models.FileField(upload_to='investigationfilesdoc/',blank=True,null=True)
    #all under investigation
    fnac=models.TextField(blank=True,null=True)
    histopathology=models.TextField(blank=True,null=True)
    #under histopathology IHC
    ihc=models.TextField(blank=True,null=True)
    #out of histopathology but under investigation
    ctscan=models.TextField(blank=True,null=True)
    mri=models.TextField(blank=True,null=True)
    petct=models.TextField(blank=True,null=True)
    bonescan=models.TextField(blank=True,null=True)
    #CBC, urine R/E, SERUM CREATININE , RBS
    cbc=models.TextField(blank=True,null=True)
    pvf=models.TextField(blank=True,null=True)
    urineRE=models.TextField(blank=True,null=True)
    electrolyte=models.TextField(blank=True,null=True)
    rft=models.TextField(blank=True,null=True)
    lft=models.TextField(blank=True,null=True)
    xraychest=models.TextField(blank=True,null=True)
    ultrasound=models.TextField(blank=True,null=True)
    ENDOSCOPYofupperGIT=models.TextField(blank=True,null=True)
    COLONOSCOPY=models.TextField(blank=True,null=True)
    Nasopharyngoscopy=models.TextField(blank=True,null=True)
    Bronchoscopy=models.TextField(blank=True,null=True)
    fol=models.TextField(blank=True,null=True)
    papsmearcytology=models.TextField(blank=True,null=True)
    tumourmarker=models.TextField(blank=True,null=True)
    TSH=models.TextField(blank=True,null=True)
    ECG=models.TextField(blank=True,null=True)
    echo_cardiography=models.TextField(blank=True,null=True)
    Bone_marrow_Study=models.TextField(blank=True,null=True)
    LDH=models.TextField(blank=True,null=True)
    SERUM_PROTEIN_ELECTROPHORESIS=models.TextField(blank=True,null=True)
    additionaltest=models.TextField(blank=True,null=True)
    reportsfiles=models.FileField(upload_to='patientreportsdoc/',blank=True,null=True)
    #outside Investigation
    stage=[
        ('1','I'),
        ('2','II'),
        ('3','III'),
        ('4','IV')
    ]
    staging=models.CharField(max_length=20,choices=stage,blank=True,null=True)
    grades=[
        ('1','I'),
        ('2','II'),
        ('3','III'),
    ]
    grading=models.CharField(max_length=20,choices=grades,blank=True,null=True)
    Treatment=[
        ('Curative', (
            ('surgery', 'surgery'),
            ('chemotherapy', 'Chemotherapy'),
            ('immunotherapy','Immunotherapy'),
            ('hormone','Hormone Therapy'),
            ('other','Other'),
        )
    ),
    ('Palliative', (
            ('chemotherapy', 'Chemotherapy'),
            ('immunotherapy','Immunotherapy'),
            ('hormone','Hormone Therapy'),
            ('other','Other'),
        )
    ),
    ('Others', 'Others'),
    ]
    Treatmentapproach=models.CharField(max_length=100,choices=Treatment,blank=True,null=True)
    additionaltreatment=models.TextField(blank=True,null=True)
    adjuvant=models.TextField(blank=True,null=True)
    new_adjuvant=models.TextField(blank=True,null=True)
    followup=models.TextField(blank=True,null=True)
    additionalinformation=models.TextField(blank=True,null=True)
    additionalfiles=models.FileField(upload_to='patientadditionalfilesdoc/',blank=True,null=True)


class Doctor(models.Model):
    name=models.CharField(max_length=150,blank=False,null=False)
    image=models.ImageField(upload_to='doctorimages/',blank=True,null=True)
    gender=[
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    ]
    sex=models.CharField(max_length=100,choices=gender,blank=True,null=True)
    designation=models.TextField(blank=True,null=True)
    number=models.IntegerField(blank=True,null=True)
    email=models.EmailField(max_length=200,blank=True,null=True)
    address=models.TextField(blank=True,null=True)


class Staff(models.Model):
    image=models.ImageField(upload_to='staffimage/',blank=True,null=True)
    name=models.CharField(max_length=200,blank=False,null=False)
    Age=models.IntegerField(blank=True,null=True)
    number=models.IntegerField(blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    gender=[
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    ]
    sex=models.CharField(max_length=100,choices=gender,blank=True,null=True)
    duty=[
        ('MLSS','MLSS'),
        ('peon','PEON'),
        ('sister','SISTER')
    ]
    designation=models.CharField(max_length=100,choices=duty,blank=True,null=True)
    machine_room=[
        ('Teletherapy','Teletherapy'),
        ('Brachy Therapy','Brachy Therapy'),
        ('Medical Technologist','Medical technologist'),
        ('MLSS','MLSS'),
        ('N/A','N/A')

    ]
    machine=models.CharField(max_length=100,choices=machine_room,blank=True,null=True)

class Notice(models.Model):
    notice=models.TextField(null=True,blank=True)
    noticefiles=models.FileField(upload_to='noticefilesdoc/',blank=True,null=True)

class ward(models.Model):
    patientid=models.CharField(max_length=10,null=True,blank=True)
    wardnum=models.IntegerField(null=False,blank=False)
    bednum=models.IntegerField(null=False,blank=False)
    firstname=models.CharField(max_length=100,null=True,blank=True)
    lastname=models.CharField(max_length=100,null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
    gender=[
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    ]
    sex=models.CharField(max_length=100,choices=gender,null=True,blank=True)
    reg=models.CharField(max_length=100,null=True,blank=True)
    
class roster(models.Model):
    oncallsaturday=models.CharField(max_length=200,null=True,blank=True)
    oncallsunday=models.CharField(max_length=200,null=True,blank=True)
    oncallmonday=models.CharField(max_length=200,null=True,blank=True)
    oncalltuesday=models.CharField(max_length=200,null=True,blank=True)
    oncallwednesday=models.CharField(max_length=200,null=True,blank=True)
    oncallthursday=models.CharField(max_length=200,null=True,blank=True)
    roundsaturday=models.CharField(max_length=200,null=True,blank=True)
    roundsunday=models.CharField(max_length=200,null=True,blank=True)
    roundmonday=models.CharField(max_length=200,null=True,blank=True)
    roundtuesday=models.CharField(max_length=200,null=True,blank=True)
    roundwednesday=models.CharField(max_length=200,null=True,blank=True)
    roundthursday=models.CharField(max_length=200,null=True,blank=True)
    planningsaturday=models.CharField(max_length=200,null=True,blank=True)
    planningsunday=models.CharField(max_length=200,null=True,blank=True)
    planningmonday=models.CharField(max_length=200,null=True,blank=True)
    planningtuesday=models.CharField(max_length=200,null=True,blank=True)
    planningwednesday=models.CharField(max_length=200,null=True,blank=True)
    planningthursday=models.CharField(max_length=200,null=True,blank=True)
    outdoorsaturday=models.CharField(max_length=200,null=True,blank=True)
    outdoorsunday=models.CharField(max_length=200,null=True,blank=True)
    outdoormonday=models.CharField(max_length=200,null=True,blank=True)
    outdoortuesday=models.CharField(max_length=200,null=True,blank=True)
    outdoorwednesday=models.CharField(max_length=200,null=True,blank=True)
    outdoorthursday=models.CharField(max_length=200,null=True,blank=True)


    
   




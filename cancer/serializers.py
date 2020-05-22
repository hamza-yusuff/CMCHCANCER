from rest_framework import serializers
from . models import Patient,Doctor,Staff,ward,Notice,roster


class Patientserializer(serializers.ModelSerializer):
    patient_image=serializers.ImageField(max_length=None,use_url=True,allow_null=True,allow_empty_file=True,required=False)
    historyfiles=serializers.FileField(max_length=None,use_url=True,allow_null=True,allow_empty_file=True,required=False)
    physicalexamfiles=serializers.FileField(max_length=None,use_url=True,allow_null=True,allow_empty_file=True,required=False)
    investigationfiles=serializers.FileField(max_length=None,use_url=True,allow_null=True,allow_empty_file=True,required=False)
    reportsfiles=serializers.FileField(max_length=None,use_url=True,allow_null=True,allow_empty_file=True,required=False)
    additionalfiles=serializers.FileField(max_length=None,use_url=True,allow_null=True,allow_empty_file=True,required=False)
    class Meta:
        model=Patient
        fields='__all__'

class Doctorserializer(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None,use_url=True,allow_null=True,allow_empty_file=True,required=False)
    class Meta:
        model=Doctor
        fields=['id','name','image','sex','designation','number','email','address']

class Staffserializer(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None,use_url=True,allow_null=True,allow_empty_file=True,required=False)
    class Meta:
        model=Staff
        fields='__all__'

class Wardserializer(serializers.ModelSerializer):
    class Meta:
        model=ward
        fields='__all__'

class Noticeserializer(serializers.ModelSerializer):
    class Meta:
        model=Notice
        fields='__all__'

class Rosterserializer(serializers.ModelSerializer):
    class Meta:
        model=roster
        fields='__all__'


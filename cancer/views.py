from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import Patientserializer,Doctorserializer,Staffserializer,Wardserializer,Noticeserializer,Rosterserializer
from . models import Patient,Staff,Doctor,ward,Notice,roster
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
@api_view(['GET', ])
def patientlist(request):
    patients=Patient.objects.all().order_by('-created')
    serializer= Patientserializer(patients,many=True)
    return Response(serializer.data)
@csrf_exempt
@api_view(['GET', ])
def singlepatient(request,pk):
    try:
        patient=Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=Patientserializer(patient,many=False)
        return Response(serializer.data)
@csrf_exempt
@api_view(['PATCH', ])
def patientupdate(request,pk):
    try:
        patient=Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='PATCH':
        serializer = Patientserializer(patient,data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data['success']='update successful'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['DELETE', ])
def patientdelete(request,pk):
    try:
        patient=Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='DELETE':
        operation=patient.delete()
        data={}
        if operation:
            data['success']='delete successful'
        else:
            data['failure']='delete failed'
        return Response(data=data)
@csrf_exempt
@api_view(['POST' ])
def patientcreate(request):
    if request.method=='POST':
        serializer=Patientserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class PatientListView(ListAPIView):
    queryset=Patient.objects.all()
    serializer_class=Patientserializer
    pagination_class=PageNumberPagination
    filter_backends=(SearchFilter,OrderingFilter)
    search_fields=('fname','lname','Cancer_id','Age','registration','Contact')
@csrf_exempt    
@api_view(['GET', ])
def singledoctor(request,pk):
    try:
        doctor=Doctor.objects.get(pk=pk)
    except Doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=Doctorserializer(doctor,many=False)
        return Response(serializer.data)
@csrf_exempt
@api_view(['PATCH', ])
def doctorupdate(request,pk):
    try:
        doctor=Doctor.objects.get(pk=pk)
    except Doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='PATCH':
        serializer = Doctorserializer(doctor,data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data['success']='update successful'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['DELETE', ])
def doctordelete(request,pk):
    try:
        doctor=Doctor.objects.get(pk=pk)
    except Doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='DELETE':
        operation=doctor.delete()
        data={}
        if operation:
            data['success']='delete successful'
        else:
            data['failure']='delete failed'
        return Response(data=data)
@csrf_exempt
@api_view(['POST' ])
def doctorcreate(request):
    if request.method=='POST':
        serializer=Doctorserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DoctorListView(ListAPIView):
    queryset=Doctor.objects.all()
    serializer_class=Doctorserializer
    filter_backends=(SearchFilter,OrderingFilter)
    search_fields=('designation','name')

class StaffListView(ListAPIView):
    queryset=Staff.objects.all()
    serializer_class=Staffserializer
    filter_backends=(SearchFilter,OrderingFilter)
    search_fields=('name','designation')
@csrf_exempt
@api_view(['GET', ])
def singlestaff(request,pk):
    try:
        staff=Staff.objects.get(pk=pk)
    except Staff.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=Staffserializer(staff,many=False)
        return Response(serializer.data)
@csrf_exempt
@api_view(['PATCH', ])
def staffupdate(request,pk):
    try:
        staff=Staff.objects.get(pk=pk)
    except Staff.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='PATCH':
        serializer = Staffserializer(staff,data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data['success']='update successful'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['DELETE', ])
def staffdelete(request,pk):
    try:
        staff=Staff.objects.get(pk=pk)
    except Staff.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='DELETE':
        operation=staff.delete()
        data={}
        if operation:
            data['success']='delete successful'
        else:
            data['failure']='delete failed'
        return Response(data=data)
@csrf_exempt
@api_view(['POST' ])
def staffcreate(request):
    if request.method=='POST':
        serializer=Staffserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class WardListView(ListAPIView):
    queryset=ward.objects.all()
    serializer_class=Wardserializer
    filter_backends=(SearchFilter,OrderingFilter)
    search_fields=('firstname','lastname','wardnum','bednum')
@csrf_exempt
@api_view(['GET', ])
def singleward(request,pk):
    try:
        wardpatient=ward.objects.get(pk=pk)
    except ward.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=Wardserializer(wardpatient,many=False)
        return Response(serializer.data)
@csrf_exempt
@api_view(['PATCH', ])
def wardupdate(request,pk):
    try:
        wardpatient=ward.objects.get(pk=pk)
    except ward.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='PATCH':
        serializer = Wardserializer(wardpatient,data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data['success']='update successful'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['DELETE', ])
def warddelete(request,pk):
    try:
        wardpatient=ward.objects.get(pk=pk)
    except ward.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='DELETE':
        operation=wardpatient.delete()
        data={}
        if operation:
            data['success']='delete successful'
        else:
            data['failure']='delete failed'
        return Response(data=data)
@csrf_exempt
@api_view(['POST' ])
def wardcreate(request):
    if request.method=='POST':
        serializer=Wardserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class NoticeListView(ListAPIView):
    queryset=Notice.objects.all()
    serializer_class=Noticeserializer

class RosterListView(ListAPIView):
    queryset=roster.objects.all()
    serializer_class=Rosterserializer

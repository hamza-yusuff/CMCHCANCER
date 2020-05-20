from django.urls import path
from cancer.views import patientlist,singlepatient,patientupdate,patientdelete,patientcreate,PatientListView,DoctorListView,doctorcreate,doctordelete,doctorupdate,singledoctor, StaffListView,singlestaff,staffupdate,staffcreate,staffdelete,WardListView,wardcreate,warddelete,wardupdate,singleward,NoticeListView,RosterListView
 
urlpatterns=[
    path('new/',patientlist,name='patientlist'),
    path('<str:pk>/singlepatient/',singlepatient,name='singlepatient'),
    path('<str:pk>/patientupdate/',patientupdate,name='update_patient'),
    path('<str:pk>/patientdelete/',patientdelete,name='delete_patient'),
    path('patientcreate',patientcreate,name='patient_create'),
    path('patientlist', PatientListView.as_view(),name='patientlist'),
    #path('<str:pk>/update/',PatientUpdateAPIView.as_view(),name='update'),
    path('<str:pk>/singledoctor/',singledoctor,name='singledoctor'),
    path('<str:pk>/doctorupdate/',doctorupdate,name='update_doctor'),
    path('<str:pk>/doctordelete/',doctordelete,name='delete_doctor'),
    path('doctorcreate',doctorcreate,name='doctor_create'),
    path('stafflist',StaffListView.as_view(),name='stafflist'),
    path('doctorlist', DoctorListView.as_view(),name='doctorlist'),
    path('<str:pk>/singlestaff/',singlestaff,name='singlestaff'),
    path('<str:pk>/staffupdate/',staffupdate,name='update_staff'),
    path('<str:pk>/staffdelete/',staffdelete,name='delete_staff'),
    path('staffcreate',staffcreate,name='staff_create'),
    path('wardlist', WardListView.as_view(),name='wardlist'),
    path('<str:pk>/singleward/',singleward,name='singleward'),
    path('<str:pk>/wardupdate/',wardupdate,name='update_ward'),
    path('<str:pk>/warddelete/',warddelete,name='delete_ward'),
    path('wardcreate',wardcreate,name='ward_create'),
    path('noticelist',NoticeListView.as_view(),name='notice'),
    path('roster',RosterListView.as_view(),name='roster'),


]
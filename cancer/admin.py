from django.contrib import admin
from .models import Patient,Doctor,Staff,Notice,ward,roster
# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Staff)
admin.site.register(Notice)
admin.site.register(ward)
admin.site.register(roster)
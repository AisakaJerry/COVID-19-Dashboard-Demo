from django.contrib import admin

# Register your models here.
from .models import Takeout,DoctorVisit,Symptom,MedicineHistory,SurroundingSituation,Trip,State

admin.site.register(Takeout)
admin.site.register(DoctorVisit)
admin.site.register(Symptom)
admin.site.register(MedicineHistory)
admin.site.register(SurroundingSituation)
admin.site.register(Trip)
admin.site.register(State)
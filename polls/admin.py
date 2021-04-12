from django.contrib import admin

# Register your models here.
from .models import State, Takeout,DoctorVisit,Symptom,MedicineHistory,SurroundingSituation,Trip,Fitbit,Apple, localData

admin.site.register(Takeout)
admin.site.register(DoctorVisit)
admin.site.register(Symptom)
admin.site.register(MedicineHistory)
admin.site.register(SurroundingSituation)
admin.site.register(Trip)
admin.site.register(Fitbit)
admin.site.register(Apple)
admin.site.register(State)
admin.site.register(localData)
from django.urls import path

from django.conf.urls import url
from . import views

from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('syncdata/',views.syncdata,name='syncdata'),
    path('getsync/',views.getsync,name='getsync'),
    path('takeoutdata/',views.takeoutdata,name='takeoutdata'),
    path('addtakeout/',views.addtakeout,name='addtakeout'),
    path('doctorvisitdata/',views.doctorvisitdata,name='doctorvisitdata'),
    path('adddoctorvisit/',views.adddoctorvisit,name='adddoctorvisit'),
    path('symptomdata/',views.symptomdata,name='symptomdata'),
    path('addsymptom/',views.addsymptom,name='addsymptom'),
    path('medicinehistorydata/',views.medicinehistorydata,name='medicinehistorydata'),
    path('addmedicinehistory/',views.addmedicinehistory,name='addmedicinehistory'),
    path('surroundingsituationdata/',views.surroundingsituationdata,name='surroundingsituationdata'),
    path('addsurroundingsituation/',views.addsurroundingsituation,name='addsurroundingsituation'),
    path('tripdata/',views.tripdata,name='tripdata'),
    path('likelihood/',views.likelihood,name='likelihood'),
]
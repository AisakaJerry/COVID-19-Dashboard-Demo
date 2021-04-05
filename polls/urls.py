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
    #click hypertext 'more sync data' and then jump to syncdata.html
    path('syncdata/',views.syncdata,name='syncdata'),
    #click button 'get new sync data' and then jump to getsync.html
    path('getsync/',views.getsync,name='getsync'),
    #click hypertext 'more takeout data' and then jump to takeoutdata.html
    path('takeoutdata/',views.takeoutdata,name='takeoutdata'),
    #click button 'add new sync data' and then jump to addtakeout.html
    path('addtakeout/',views.addtakeout,name='addtakeout'),

    path('getLocalData/', views.getLocalData, name='getLocalData'),
]
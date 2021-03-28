from django.shortcuts import render
from django.http import HttpResponse

from .models import Post
from .models import PersonalInfo
# Create your views here.

def index(request):
    context = {'persons_list': PersonalInfo.objects.all()}
    return render(request, 'dashboard/index.html', context=context)
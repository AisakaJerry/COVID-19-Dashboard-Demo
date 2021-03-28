from django.shortcuts import render
from django.http import HttpResponse

from .models import Post
# Create your views here.

def index(request):
    context = {'news_list': Post.objects.all()}
    return render(request, 'dashboard/index.html', context=context)
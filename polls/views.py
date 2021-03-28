from django.shortcuts import render
from django.http import HttpResponse
from .models import Takeout
from .forms import TopicForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

#home page
def index(request):
    return render(request,'templates/index.html')

#sync data page
def syncdata(request):
    return render(request,'templates/syncdata.html')

#get sync data page
def getsync(request):
    return render(request,'templates/getsync.html')

#takeout data page
def takeoutdata(request):
    takeout_list=Takeout.objects.all()
    context={'takeoutdata_list':takeout_list}
    return render(request,'templates/takeoutdata.html',context=context)

#add takeout data page
def addtakeout(request):
    #if no data is added, build an empty form
    if request.method !='POST':
        form=TopicForm()
    else:
        form=TopicForm(request.POST)#add new data
        if form.is_valid():
            new_takeout=form.save(commit=False)
            new_takeout.owner=request.user
            new_takeout.save()
            return HttpResponseRedirect(reverse('takeoutdata'))

    context={'form':form}
    return render(request,'templates/addtakeout.html',context)
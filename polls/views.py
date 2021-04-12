from django.shortcuts import render
from django.http import HttpResponse
from .models import Takeout,DoctorVisit,Symptom,MedicineHistory,SurroundingSituation,Trip,Fitbit,Apple
from .forms import TopicFormTakeout,TopicFormDoctorVisit,TopicFormSymptom,TopicFormMedicineHistory,TopicFormSurroundingSituation,TopicFormTrip,TopicFormFitbit,TopicFormApple, localDataForm
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
import random
from django.views.generic import View
from .forms import SelectStateForm
import requests

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

#takeout data page
def takeoutdata(request):
    takeout_list=Takeout.objects.all()
    context={'takeout_list':takeout_list}
    return render(request,'templates/takeoutdata.html',context=context)

#add takeout data page
def addtakeout(request):
    #if no data is added, build an empty form
    if request.method !='POST':
        form=TopicFormTakeout()
    else:
        form=TopicFormTakeout(request.POST)#add new data
        if form.is_valid():
            new_takeout=form.save(commit=False)
            new_takeout.owner=request.user
            new_takeout.save()
            return HttpResponseRedirect(reverse('takeoutdata'))
    context={'form':form}
    return render(request,'templates/addtakeout.html',context=context)

#doctor visit data page
def doctorvisitdata(request):
    doctorvisit_list=DoctorVisit.objects.all()
    context={'doctorvisit_list':doctorvisit_list}
    return render(request,'templates/doctorvisitdata.html',context=context)

#add doctor visit data page
def adddoctorvisit(request):
    #if no data is added, build an empty form
    if request.method != 'POST':
        form=TopicFormDoctorVisit()
    else:
        form=TopicFormDoctorVisit(request.POST)#add new data
        if form.is_valid():
            new_doctorvisit=form.save(commit=False)
            new_doctorvisit.owner=request.user
            new_doctorvisit.save()
            return HttpResponseRedirect(reverse('doctorvisitdata'))
    context={'form':form}
    return render(request,'templates/adddoctorvisit.html',context=context)

#symptom data page
def symptomdata(request):
    symptom_list=Symptom.objects.all()
    context={'symptom_list':symptom_list}
    return render(request,'templates/symptomdata.html',context=context)

#add symptom data page
def addsymptom(request):
    #if no data is added, build an empty form
    if request.method != 'POST':
        form=TopicFormSymptom()
    else:
        form=TopicFormSymptom(request.POST)#add new data
        if form.is_valid():
            new_symptom=form.save(commit=False)
            new_symptom.owner=request.user
            new_symptom.save()
            return HttpResponseRedirect(reverse('symptomdata'))
    context={'form':form}
    return render(request,'templates/addsymptom.html',context)

#medicine history data page
def medicinehistorydata(request):
    medicinehistory_list=MedicineHistory.objects.all()
    context={'medicinehistory_list':medicinehistory_list}
    return render(request,'templates/medicinehistorydata.html',context=context)

#add medicine history data page
def addmedicinehistory(request):
    #if no data is added, build an empty form
    if request.method != 'POST':
        form=TopicFormMedicineHistory()
    else:
        form=TopicFormMedicineHistory(request.POST)#add new data
        if form.is_valid():
            new_symptom=form.save(commit=False)
            new_symptom.owner=request.user
            new_symptom.save()
            return HttpResponseRedirect(reverse('medicinehistorydata'))
    context={'form':form}
    return render(request,'templates/addmedicinehistory.html',context=context)

#surrounding situation data page
def surroundingsituationdata(request):
    surroundingsituation_list=SurroundingSituation.objects.all()
    context={'surroundingsituation_list':surroundingsituation_list}
    return render(request,'templates/surroundingsituationdata.html',context=context)

#add surrounding situation data page
def addsurroundingsituation(request):
    #if no data is added, build an empty form
    if request.method != 'POST':
        form=TopicFormSurroundingSituation()
    else:
        form=TopicFormSurroundingSituation(request.POST)#add new data
        if form.is_valid():
            new_symptom=form.save(commit=False)
            new_symptom.owner=request.user
            new_symptom.save()
            return HttpResponseRedirect(reverse('surroundingsituationdata'))
    context={'form':form}
    return render(request,'templates/addsurroundingsituation.html',context=context)

#trip data page
def tripdata(request):
    trip_list=Trip.objects.all()
    context={'trip_list':trip_list}
    return render(request,'templates/tripdata.html',context=context)

#add trip data page
def addtrip(request):
    #if no data is added, build an empty form
    if request.method != 'POST':
        form=TopicFormTrip()
    else:
        form=TopicFormTrip(request.POST)#add new data
        if form.is_valid():
            new_symptom=form.save(commit=False)
            new_symptom.owner=request.user
            new_symptom.save()
            return HttpResponseRedirect(reverse('tripdata'))
    context={'form':form}
    return render(request,'templates/addtrip.html',context=context)

def likelihood(request):
    #the initial likelihood is 20%
    COVID_likelihood=20
    #get the last symptom data
    numbers_symptom=Symptom.objects.count()
    last_symptom=Symptom.objects.all()[numbers_symptom-1]
    #get the body temperature and cough serverity of the last symptom data
    last_body_temperature=last_symptom.body_temperature
    last_cough_severity=last_symptom.cough_severity
    #if the body temperatrue is more than 38 AND the cough severity is almost always or always, the likelihood should be 60%
    if last_body_temperature>=38 and (last_cough_severity==4 or last_cough_severity==5):
        COVID_likelihood=60
    #if the body temperatrue is more than 38 OR the cough severity is almost always or always, the likelihood should be 40%
    elif last_body_temperature>=38 or (last_cough_severity==4 or last_cough_severity==5):
        COVID_likelihood=40
    #if the last surrounding situation data is not earlier than 14 days, add 10% to the likelihood
    numbers_surrounding_situation=SurroundingSituation.objects.count()
    last_surrounding_situation=SurroundingSituation.objects.all()[numbers_surrounding_situation-1]
    today=datetime.date.today()
    if today-datetime.timedelta(days=14)<=last_surrounding_situation.last_meet_date:
        COVID_likelihood+=10
    context={'COVID_likelihood':COVID_likelihood}
    return render(request,'templates/likelihood.html',context=context)

#sync data page
def syncdata(request):
    return render(request,'templates/syncdata.html')

#Fitbit data page
def Fitbitdata(request):
    Fitbit_list=Fitbit.objects.all()
    context={'Fitbit_list':Fitbit_list}
    return render(request,'templates/Fitbitdata.html',context=context)

#get Fitbit data page
def getFitbit(request):
    #use random number to initialise the form
    steps=random.randint(1000,30000)
    calories=random.randint(1000,3000)
    floors=random.randint(1,15)
    distance=round(random.uniform(1,15),2)
    weight=random.randint(100,200)
    date=datetime.date.today()
    #build a Fitbit form
    content={'steps':steps,'calories':calories,'floors':floors,'distance':distance,'weight':weight,'date':date}
    form=TopicFormFitbit(content)
    form.save()
    context={'form':form}
    return render(request,'templates/getFitbit.html',context=context)

#Apple data page
def Appledata(request):
    Apple_list=Apple.objects.all()
    context={'Apple_list':Apple_list}
    return render(request,'templates/Appledata.html',context=context)

#get Apple data page
def getApple(request):
    #use random number to initialise the form
    steps=random.randint(1000,30000)
    distance=round(random.uniform(1,15),2)
    floors=random.randint(1,15)
    calories=random.randint(1000,3000)
    heart_rate=random.randint(50,120)
    exercise_minutes=random.randint(30,180)
    date=datetime.date.today()
    #build a Fitbit form
    content={'steps':steps,'distance':distance,'floors':floors,'calories':calories,'heart_rate':heart_rate,'exercise_minutes':exercise_minutes,'date':date}
    form=TopicFormApple(content)
    form.save()
    context={'form':form}
    return render(request,'templates/getApple.html',context=context)

def getLocalData(request):
    select_form = SelectStateForm()
    return render(request, 'templates/getLocalData.html', {
        'select_form': select_form,
    })

def displayLocalData(request):
    select_form = SelectStateForm(request.POST)
    if select_form.is_valid():
        get_value = request.POST.get('sel_value', "")
        # other logic
        r = requests.get('https://api.covidactnow.org/v2/state/VA.json?apiKey=9fbed953db9f469badede64ddbb3e829', params=requests.get)
        jsonFile = r.json()
        population = jsonFile.population
        cases = jsonFile.acturals.cases
        death = jsonFile.acturals.deaths
        content = {'population':population, 'cases':cases, 'death':death}
        form = localDataForm(content)
        form.save()
        context = {'form':form}
        # context = {'get_value': get_value}
        # return render(request, 'templates/displaylocaldata.html',context=context)
        return render(request, 'templates/displayLocalData.html', context=context)

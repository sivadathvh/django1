from django.shortcuts import render
from django.http import HttpResponse
from .models import Event

# Create your views here.
def index(request):
    events = Event.objects.all()
    context = {
        'events' : events
    }
    return render(request,'eventapp/index.html',context)

def eventdetail(request,pk):
    if request.method=='POST':
        print('i got a post request')
    event_single=Event.objects.get(pk=pk)
    form=Applicantform(request.POST)
    if form.is_valid():
        applicant= form.save(commit=False)
        Applicant.event=event_single
        applicant.save()

    form=Applicantform()
    context = {
        'event' : event_single,
        'form' : form
    }
    
    
    return render(request,'eventapp/details.html',context)
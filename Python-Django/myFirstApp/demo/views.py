from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('Welcome to Demo App')
def welcome(request):
    return render(request,'demo/welcome.htm')
def details(request):
    data={
        'id':43934,
        'name':'Virat',
        'city':'Banglore'
    }
    return render(request,'demo/details.html',data)
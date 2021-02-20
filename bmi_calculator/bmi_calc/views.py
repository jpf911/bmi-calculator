from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request,'bmi_calc/home.html')

def bmi(request):

    weight=request.GET.get('weight')
    height=request.GET.get('height')

    weight=float(weight)
    height = float(height)
    bmi=(weight/(height**2))

    return render(request, 'bmi_calc/bmi.html',{'bmi':bmi})

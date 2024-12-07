# views.py
from django.shortcuts import render, redirect
from django.contrib import messages




def intro (request):
    return render(request,'intro.html')



def lang (request):
    return render(request,'lang.html')


def python (request):
    return render(request,'python.html')

def cpp (request):
    return render(request,'c_plus.html')

def java (request):
    return render(request,'java.html')

def js (request):
    return render(request,'java_script.html')
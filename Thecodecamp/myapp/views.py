# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

from git import Repo


def webhook (request):
    if request.method == 'POST':
        repo = Repo('.')
        git = repo.git
        git.checkout('master')
        git.stash()
        git.pull('origin', 'master', rebase=True)
        return HttpResponse("", content_type="text/plain", status=200)
    else:
        return HttpResponse("", content_type="text/plain", status=400)



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
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View, TemplateView

def choose_bullying(request):
    return render(request, 'home/home.html')

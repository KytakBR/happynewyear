from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "main/index.html")


def vlad(request):
    return render(request, "main/vlad.html")


def tema(request):
    return render(request, "main/tema.html")


def yasha(request):
    return render(request, "main/yasha.html")


def senya(request):
    return render(request, "main/senya.html")


def roma(request):
    return render(request, "main/roma.html")

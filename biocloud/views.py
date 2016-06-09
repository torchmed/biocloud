from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'biocloud/index.html', context)

def dashboard(request):
    context = {}
    return render(request, 'biocloud/dashboard.html', context)
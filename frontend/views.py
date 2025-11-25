from django.shortcuts import render

def home(request):
    return render(request, 'frontend/index.html')

def about(request):
    return render(request, 'frontend/about.html')

def service(request):
    return render(request, 'frontend/service.html')

def team(request):
    return render(request, 'frontend/team.html')

def contact(request):
    return render(request, 'frontend/contact.html')

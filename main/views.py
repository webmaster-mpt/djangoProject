from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def education(request):
    return render(request, 'education.html')

def experience(request):
    return render(request, 'experience.html')

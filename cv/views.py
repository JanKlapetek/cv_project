import requests
from django.shortcuts import render
from .models import Education, Experience, Skill

def cv_view(request):
    return render(request, 'cv/cv_view.html')

def about_view(request):
    education = Education.objects.all()
    experience = Experience.objects.all()
    skills = Skill.objects.all()
    return render(request, 'cv/about_view.html', {'education': education, 'experience': experience, 'skills': skills})

def hearthstone_view(request):
    page = request.GET.get("page", 1)
    url = "https://hearthstone11.p.rapidapi.com/cards"
    querystring = {"page": page, "pageSize": "10"}

    headers = {
	"x-rapidapi-key": "beb93bf793msh77b5301dcd31d58p146937jsnfe6abad73602",
	"x-rapidapi-host": "hearthstone11.p.rapidapi.com"
 }
    response = requests.get(url, headers=headers, params=querystring)
    cards = response.json() if response.status_code == 200 else []
    
    # Tento výpis by měl vracet seznam s kartami a jejich vlastnostmi.
    print(cards)
    
    # Předáváme seznam karet do šablony.
    return render(request, "cv/hearthstone_view.html", {"cards": cards, "page": int(page)})



    

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
    url = "https://hearthstone11.p.rapidapi.com/cards"
    headers = {
        "x-rapidapi-key": "beb93bf793msh77b5301dcd31d58p146937jsnfe6abad73602",
        "x-rapidapi-host": "hearthstone11.p.rapidapi.com"
    }
    params = {"page": request.GET.get("page", 1), "pageSize": 6}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        # Debug: Výpis do terminálu, abychom viděli strukturu dat
        print("Data structure:", data)
        
        # Získej konkrétní karty
        cards = data.get("cards", [])
        
        return render(request, "cv/hearthstone_view.html", {"cards": cards})
    else:
        return render(request, "cv/hearthstone_view.html", {"cards": []})

    

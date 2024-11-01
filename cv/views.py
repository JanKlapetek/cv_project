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
    querystring = {"page": "1", "pageSize": "10"}  # Změníme pageSize podle potřeby

    headers = {
        "x-rapidapi-key": "beb93bf793msh77b5301dcd31d58p146937jsnfe6abad73602",
        "x-rapidapi-host": "hearthstone11.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        cards = response.json()  # Získáme data karet
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        cards = []

    return render(request, 'cv/hearthstone_view.html', {"cards": cards})

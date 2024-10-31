# cv/views.py

from django.shortcuts import render
from .models import Education, Experience, Skill

def cv_view(request):
    education = Education.objects.all()
    experience = Experience.objects.all()
    skills = Skill.objects.all()
    return render(request, 'cv/cv_view.html', {'education': education, 'experience': experience, 'skills': skills})

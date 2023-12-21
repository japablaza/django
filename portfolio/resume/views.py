from django.shortcuts import render
from .models import Resume

def all_resume(request):
    resumes = Resume.objects.order_by('-date')[:3]
    return render(request, 'resume/all_resume.html', {'resumes':resumes })

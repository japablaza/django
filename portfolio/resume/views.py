from django.shortcuts import render

def all_resume(request):
    return render(request, 'resume/all_resume.html')

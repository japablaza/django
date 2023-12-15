
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_resume, name='all_resume'),
]
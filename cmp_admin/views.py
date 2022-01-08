from django.shortcuts import render
from . import views
# Create your views here.


def Home(request):
    return render('home',views.Home)
from django.shortcuts import render
from django.template import loader
from django.contrib.auth.decorators import login_required
@login_required
def home(request):
    context={'val':"Menu Acceuil"}
    return render(request,'home.html',context)

def accueil(request):
    return render(request,'accueil.html')
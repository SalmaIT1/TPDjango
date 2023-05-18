from django.http import HttpResponseRedirect
from .models import Produit
from .forms import ProduitForm,FournisseurForm , OrderForm
from django.shortcuts import render , redirect
from .forms import ProduitForm, FournisseurForm,UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from magasin.serializers import CategorySerializer,ProduitSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from magasin.models import Categorie , Produit , Fournisseur
from rest_framework import viewsets


def index(request):
    products= Produit.objects.all()
    context={'products':products}
    return render( request,'magasin/mesProduits.html',context )
def mag(request):
    if request.method == "POST" :
        form = ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
    else :
        form = ProduitForm() #créer formulaire vide
    return render(request,'magasin/majProduits.html',{'form':form})
def vitrine(request):
    list=Produit.objects.all()
    return render(request,'magasin/vitrine.html',{'list':list})

def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            # Rediriger l'utilisateur vers une page de confirmation ou une autre page
    else:
        form = OrderForm()
    return render(request, 'magasin/order.html', {'form': form})

def nouveauFournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listeFournisseurs')
    else:
        form = FournisseurForm()
    return render(request, 'magasin/Fournisseur.html', {'form': form})


def listeFournisseurs(request):
    fournisseurs = Fournisseur.objects.all()
    return render(request, 'magasin/liste_fournisseurs.html', {'fournisseurs': fournisseurs})

def register(request):
    if request.method == 'POST' :
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('index')
    else :
        form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form' : form})


class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)



class ProduitAPIView(APIView):
    def get(self, request):
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)


class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProduitSerializer
    def get_queryset(self):

        queryset = Produit.objects.filter()
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(categorie_id=category_id)
            return queryset
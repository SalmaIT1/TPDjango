from rest_framework import routers
from .views import CategoryAPIView,ProduitAPIView
from django.urls import path , include
from . import views
from magasin.views import ProductViewset, CategoryAPIView


router = routers.SimpleRouter()
router.register('produit', ProductViewset, basename='produit')

urlpatterns = [

   path('', views.index, name='index'),
   path('mag', views.mag, name='mag'),
   path('vitrine', views.vitrine, name='vitrine'),
   path('order', views.order, name='order'),
   path('nouveauFournisseur/', views.nouveauFournisseur, name='nouveauFournisseur'),
   path('listeFournisseurs/', views.listeFournisseurs, name='listeFournisseurs'),

   path('register/',views.register, name = 'register'),
   path('api/category/', CategoryAPIView.as_view()),
   path('api/produits/', ProduitAPIView.as_view(), name='produits-api'),
   path('api/', include(router.urls)),
 ]



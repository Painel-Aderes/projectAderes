from django.urls import path
from . import views

urlpatterns = [
    #Artesões
    path('', views.getArtesoes), #Puxa todos os dados
    path ('readUpdate/<str:pk>', views.GetPutDellArtesoes), #Puxa, Atualiza e Deleta dados.
    path ('create', views.GetPostArtesoes),#Puxa todos os dados e Cria
    path ('junta/', views.getJuntacomercial),
]
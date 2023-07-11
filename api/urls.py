from django.urls import path
from . import views

urlpatterns = [
    #Artesões
    path('artesoes/', views.getArtesoes), #Puxa todos os dados
    path ('artesoesUpdate/<str:pk>', views.GetPutDellArtesoes), #Puxa, Atualiza e Deleta dados.
    path ('create', views.GetPostArtesoes),#Puxa todos os dados e Cria
    ##JUNTA COMERCIAL
    path ('junta/', views.getJuntacomercial),
    path ('juntaCreate', views.getPostJuntacomercial),
    path ('juntaUpdate/<str:pk>', views.GetPutDeleteJuntacomercial),
    ##MICROCREDITO
    path('microcredito/', views.getMicroCredito),
    path('microcredito/read', views.getPostMicroCredito),
    path('microcredito/update/<str:pk>', views.GetPutDellMunicipio),
    ##MUNICIPIO
    path('municipio/', views.getMunicipio),
    path('municipio/read', views.getPostMunicipio),
    path('municipio/update/<str:pk>', views.GetPutDellMunicipio),
]

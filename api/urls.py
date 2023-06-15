from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import ArtesoesViewSet 
from .views import viewsets


app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(r'fundos', ArtesoesViewSet)

urlpatterns = router.urls

# urlpatterns = [
    
#     path('', views.getjunta),
#     path ('create', views.createjunta),
#     path ('read/<str:pk>', views.getjuntaid),
#     path ('update/<str:pk>', views.updatejunta),
#     path ('delete/<str:pk>', views.deletejunta),

# ]

# from django.urls import path
# from rest_framework.routers import DefaultRouter
# from api.views import ArtesoesViewSet, JunataComercialViewSet, MicroCreditoViewSet
# from .views import viewsets


# app_name = 'api'

# router = DefaultRouter(trailing_slash=False)
# router.register(r'fundos', ArtesoesViewSet)

# urlpatterns = router.urls

# app_name = 'api'

# router = DefaultRouter(trailing_slash=False)
# router.register(r'fundos', JunataComercialViewSet)

# urlpatterns = router.urls


# app_name = 'api'

# router = DefaultRouter(trailing_slash=False)
# router.register(r'fundos', MicroCreditoViewSet)

# urlpatterns = router.urls

from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path ('create', views.addUser),
    # path ('read/<str:pk>', views.getUser),
    # path ('update/<str:pk>', views.updateUser),
    # path ('delete/<str:pk>', views.deleteUser),
    path ('readUpdate/<str:pk>', views.GetPutDell),
    path ('readUpdate/', views.GetPutDell2)

]
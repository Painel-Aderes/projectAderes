from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from api.views import ArtesoesViewSet

app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(r'artesoes', ArtesoesViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     path('', views.getData),
#     path ('create', views.addUser),
#     path ('read/<str:pk>', views.getUser),
#     path ('update/<str:pk>', views.updateUser),
#     path ('delete/<str:pk>', views.deleteUser),
# ]
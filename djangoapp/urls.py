from django.urls import path
from djangoapp.views import ArtesoesViewSet
from rest_framework.routers import DefaultRouter


app_name = 'djangoapp'

router = DefaultRouter(trailing_slash=False)
router.register(r'artesao', ArtesoesViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     path('', views.getData),
#     path ('create', views.addUser),
#     path ('read/<str:pk>', views.getUser),
#     path ('update/<str:pk>', views.updateUser),
#     path ('delete/<str:pk>', views.deleteUser),
# ]
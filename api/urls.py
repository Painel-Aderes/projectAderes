from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from api.views import ArtesoesViewSet
from api.views import JuntaComercialViewSet
from api.views import MicrocreditoViewSet


app_name = 'artesoes'

router = DefaultRouter(trailing_slash=False)
router.register(r'artesoes', ArtesoesViewSet)

urlpatterns = router.urls


app_name = 'junta_comercial'

router = DefaultRouter(trailing_slash=False)
router.register(r'junta_comercial', JuntaComercialViewSet)
urlpatterns = router.urls

app_name = 'micro_credito'

router = DefaultRouter(trailing_slash=False)
router.register(r'micro_credito', MicrocreditoViewSet)
urlpatterns = router.urls


# urlpatterns = [
#     path('', views.getData),
#     path ('create', views.addUser),
#     path ('read/<str:pk>', views.getUser),
#     path ('update/<str:pk>', views.updateUser),
#     path ('delete/<str:pk>', views.deleteUser),
# ]
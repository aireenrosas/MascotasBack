from backend_api.views import MascotaViewSet
from rest_framework.routers import DefaultRouter
from backend_api import views

router = DefaultRouter()
router.register(r'mascotas', views.MascotaViewSet, basename='mascota')
urlpatterns = router.urls
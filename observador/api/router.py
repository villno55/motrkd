from rest_framework.routers import DefaultRouter
from .views import ObservacionViewSet

router_observador = DefaultRouter()
router_observador.register(
    prefix='observaciones',
    viewset=ObservacionViewSet,
    basename='observaciones'
)
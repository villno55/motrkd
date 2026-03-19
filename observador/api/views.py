from rest_framework.viewsets import ModelViewSet
from observador.models import Observacion
from .serializers import ObservacionSerializer

class ObservacionViewSet(ModelViewSet):
    serializer_class = ObservacionSerializer
    queryset = Observacion.objects.all()
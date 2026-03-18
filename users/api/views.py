from rest_framework.viewsets import ModelViewSet
from users.api import serializers
from users.models import User
from rest_framework.permissions import AllowAny
from users.api.serializers import UserSerializer


class UserApiViewSet(ModelViewSet):
    permission_classes = [AllowAny]  # define los permisos del CRUD
    serializer_class = UserSerializer  # manipulacion de datos como lo quiero yo
    queryset = User.objects.all()
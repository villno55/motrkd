from rest_framework import serializers
from observador.models import Observacion

class ObservacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observacion
        fields = '__all__'
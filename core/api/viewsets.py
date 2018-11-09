from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.api.BearerAuthentication import BearerAuthentication
from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BearerAuthentication,)

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        pass

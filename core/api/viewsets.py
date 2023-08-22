from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):

    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    # def list(self, request, *args, **kwargs):
    #     return Response({'teste': 123})
    
    # def create(self, request, *args, **kwargs):
    #     return Response({'Hello' : request.data['nome']})
    
    # def destroy(self, request, *args, **kwargs):
    #     return Response({'Deletado com sucesso' : 123})
    
    # def retrieve(self, request, *args, **kwargs):
    #     return Response({'opa' : 123})
    
    # def update(self, request, *args, **kwargs):
    #     return Response({'Atualizado com sucesso' : 123})
    
    # def partial_update(self, request, *args, **kwargs):
    #     return Response({'Foi parcialmente atualizado' : 123})

    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        return Response({'teste': 123})

    @action(methods=['get'], detail=False)
    def teste(self, request, pk=None):
        return Response({'teste': 123})
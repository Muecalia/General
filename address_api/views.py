from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from . import serializers as s
from . import models as m


# Create your views here.
class CountryView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = s.CountrySerializer
    queryset = m.Country.objects.all()
    
    def get(self, request):
        try:
            serializer = self.serializer_class(self.queryset.all(), many=True)
            return Response({'data': serializer.data, 'message':'Dados carregados com sucesso'}, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({'message': f'Erro ao listar os dados. Message: {ex}'}, status=status.HTTP_400_BAD_REQUEST)


class ProvinceView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = s.ProvinceSerializer
    queryset = m.Province.objects.all()
    
    def get(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(self.queryset.all(), many=True)
            return Response({'data': serializer.data, 'message':'Dados carregados com sucesso'}, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({'message': f'Erro ao carregar os dados. Mensagem: {ex}'}, status=status.HTTP_400_BAD_REQUEST)
    

class CountyView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = s.CountySerializer
    queryset = m.County.objects.all()
    
    def get(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(self.queryset.all(), many=True)
            return Response({'data':serializer.data, 'message':'Dados carregados com sucesso'}, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({'message': f'Erro ao carregar os dados. Mensagem: {ex}'}, status=status.HTTP_400_BAD_REQUEST)

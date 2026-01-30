from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import Funcionario
from .serializers import FuncionarioSerializer

# Create your views here.


class FuncionarioViewSet(ModelViewSet):
    serializer_class = FuncionarioSerializer

    def get_object(self):
        return get_object_or_404(Funcionario, funcionario_id=self.request.query_params.get("funcionario_id"))

    def get_queryset(self):
        return Funcionario.objects.filter(desligado=False).order_by('-nome')

    def perform_destroy(self, instance):
        instance.desligado = True
        instance.save()


def index(request):
    return HttpResponse("Oieee")

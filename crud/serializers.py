from rest_framework import serializers
from .models import Funcionario

class FuncionarioSerializer(serializers.ModelSerializer):
    desligado = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = Funcionario
        fields = ('funcionario_id', 'nome', 'idade', 'cpf', 'funcao', 'admin')
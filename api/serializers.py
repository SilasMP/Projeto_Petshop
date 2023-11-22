from rest_framework import serializers
from rest_framework.serializers import HyperlinkedRelatedField 
from rest_framework.relations import PrimaryKeyRelatedField
from reserva.models import Reserva, Petshop, Categoria
from datetime import date

class PetshopModelSerializer(serializers.ModelSerializer):
    reservas = HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name= 'api:reservas-detail'
    )
    class Meta:
        model = Petshop
        fields = '__all__'

class PetshopNestedModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Petshop
        fields = '__all__'

class PetshopRelatedFieldCustomSerializer(PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = PetshopNestedModelSerializer
        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False
    
    def to_representation(self, value):
        return self.serializer(value, context = self.context).data

class CategoriaModelSerializer(serializers.ModelSerializer):
    reservas = HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name= 'api:reservas-detail'
    )
    class Meta:
        model = Categoria
        fields = '__all__'

class CategoriaNestedModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Categoria
        fields = '__all__'

class CategoriaRelatedFieldCustomSerializer(PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = CategoriaNestedModelSerializer
        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False
    
    def to_representation(self, value):
        return self.serializer(value, context = self.context).data

class ReservaModelSerializer(serializers.ModelSerializer):
    petshop = PetshopRelatedFieldCustomSerializer(
        queryset = Petshop.objects.all(),
        read_only = False
    )
    categoria = CategoriaRelatedFieldCustomSerializer(
        queryset = Categoria.objects.all(),
        read_only = False
    )

    class Meta:
        model = Reserva
        fields = '__all__'

    def validate(self, data):
        data_agendamento = data.get('data')
        turno = data.get('turno')
        limite_agendamentos = 3

        agendamentos_no_turno = Reserva.objects.filter(data=data_agendamento, turno=turno).count()

        if data_agendamento < date.today():
            raise serializers.ValidationError('Não é possível agendar em uma data antiga')

        if agendamentos_no_turno >= limite_agendamentos:
            raise serializers.ValidationError('O limite de agendamentos para este turno ja foi atingido')

        return data

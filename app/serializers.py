from rest_framework import serializers

from .models import Bancos, Clientes, Deuda, Pagos


class BancosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bancos
        fields = "__all__"


class ClientesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = "__all__"


class DeudaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Deuda
        fields = "__all__"


class PagosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pagos
        fields = "__all__"
        # fields = ["valor_pago", "cuotas"]


class FilterDeudaSerializers(serializers.ModelSerializer):
    banco = serializers.StringRelatedField()
    cliente = serializers.StringRelatedField()

    class Meta:
        model = Deuda
        fields = ["id", "banco", "cliente", "total_deuda", "total_cuotas"]


class FilterPagosSerializers(serializers.ModelSerializer):
    deuda = FilterDeudaSerializers()

    class Meta:
        model = Pagos
        fields = ["id", "deuda", "valor_pago", "cuotas"]


class ResultFilterDeudaSerializers(serializers.ModelSerializer):
    banco = serializers.StringRelatedField()
    cliente = serializers.StringRelatedField()
    pagos = PagosSerializers(many=True)

    class Meta:
        model = Deuda
        fields = ["banco", "cliente", "total_deuda", "total_cuotas", "pagos"]

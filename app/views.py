from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .controller import Query
from .serializers import (
    BancosSerializers,
    ClientesSerializers,
    FilterDeudaSerializers,
    PagosSerializers,
)


# clase de bancos
class BancosViewSet(APIView):

    # listar Bancos
    def get(self, request, banco=""):
        return Response(BancosSerializers(Query.filtroBancos(banco), many=True).data)


# clase de clientes
class ClientesViewSet(APIView):
    # filtrar clientes
    def get(self, request, nombre=""):
        return Response(ClientesSerializers(Query.filtroCliente(nombre), many=True).data)


# clase para procesar las deudas
class DeudasClienteViewSet(APIView):

    # filtrar deudas
    def get(self, request, nombre="", banco=""):
        return Response(FilterDeudaSerializers(Query.filtroDeudas(nombre, banco), many=True).data)

    # filtrar deudas
    def post(self, request, pk="", bnc=""):

        serializer = PagosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# clase para procesar las pagos
class PagosViewSet(APIView):

    # filtrar clientes
    def get(self, request, nombre=""):
        return Response(Query.filtroPagos(nombre))

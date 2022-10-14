from .models import Bancos, Clientes, Deuda, Pagos
from .serializers import (
    BancosSerializers,
    ClientesSerializers,
    DeudaSerializers,
    FilterDeudaSerializers,
    FilterPagosSerializers,
    PagosSerializers,
    ResultFilterDeudaSerializers,
)


class Query:

    # filtro de clientes
    def filtroCliente(a):
        if a == "all":
            return Clientes.objects.all()
        else:
            return Clientes.objects.filter(nombreC=a)

    # filtro de bancos
    def filtroBancos(a):
        if a == "all":
            return Bancos.objects.all()
        else:
            return Bancos.objects.filter(nombreB=a)

    # filtro de deudas
    def filtroDeudas(a, b):
        if a == "all" and b == "all":
            return Deuda.objects.all()
        elif a != "all" and b == "all":
            return Deuda.objects.filter(cliente__nombreC=a)
        else:
            return Deuda.objects.filter(cliente__nombreC=a, banco__nombreB=b)

    # filtro de deudas
    def filtroPagos(a):
        if a == "all":
            return FilterPagosSerializers(Pagos.objects.all(), many=True).data
        else:
            data = ResultFilterDeudaSerializers(
                Deuda.objects.filter(cliente__nombreC=a).prefetch_related("pagos"), many=True
            ).data

            for x in range(len(data)):
                cf = data[x]["total_cuotas"]
                cft = 0
                for i in range(len(data[x]["pagos"])):
                    cft = cft + data[x]["pagos"][i]["cuotas"]
                cpp = cf - cft
                vc = data[x]["total_deuda"] / cf
                data[x]["Cuotas por pagar"] = cpp
                data[x]["credito por pagar"] = vc * cpp

            return data

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from app import views

router = DefaultRouter()

urlpatterns = [
    path("clientes/<str:nombre>", views.ClientesViewSet.as_view(), name="clientes"),
    path("deudas/<str:nombre>/<str:banco>", views.DeudasClienteViewSet.as_view(), name="deudas"),
    path("bancos/<str:banco>", views.BancosViewSet.as_view(), name="bancos"),
    path("pagos/<str:nombre>", views.PagosViewSet.as_view(), name="pagos"),
]

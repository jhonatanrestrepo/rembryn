from django.urls import path

from .views import (
    CotizacionProyecto
)

app_name="cotizaciones"


urlpatterns = [
    path('cotizacion/', CotizacionProyecto.as_view(), name="cotizacion"),

]
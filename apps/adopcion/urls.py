from django.conf.urls import url

from apps.adopcion.views import  index_adopcion,SolicitudList,SolicitudCreate

urlpatterns = [
    url(r'^$',index_adopcion,name='index'),
    url(r'^solicitud/listar$',SolicitudList.as_view(),name='solicitud_listar'),
    url(r'^solicitud/nueva$',SolicitudCreate.as_view(),name='solicitud_crear'),
]
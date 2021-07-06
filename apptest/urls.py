from django.conf.urls import url
from django.conf.urls import handler404, handler500
from django.urls import include, path
from . import views


urlpatterns = [
    path('getempresas', views.get_empresas),
    path('addempresa', views.add_empresa),
    path('updateempresa/<int:empresa_id>', views.update_empresa),
    path('deleteempresa/<int:empresa_id>', views.delete_empresa),
    path('generateregistrosempresas', views.generate_registros_empresas)
]
# handler404 = views.error_404
# handle    r500 = views.error_500
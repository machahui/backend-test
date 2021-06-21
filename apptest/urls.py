from django.conf.urls import url
from django.conf.urls import handler404, handler500
from django.urls import include, path
from . import views

urlpatterns = [
    path('getempresas', views.get_empresas),
    path('addempresa', views.add_empresa),
    path('updateempresa/<int:book_id>', views.update_empresa),
    path('deleteempresa/<int:book_id>', views.delete_empresa)
]

# handler404 = views.error_404
# handler500 = views.error_500
from django.conf.urls import url, include
from concurso.views import ListConcurso,ListRubro,ListConcursoTodo,PDFPrueba,mostrarFormulario
from . import views
from django.contrib.auth.decorators import login_required
from django.conf import settings

    #para restringuir la url login_required(nombre_vista)


urlpatterns = [

	url(r'^listar', ListConcurso.as_view(), name='concursos_listar'),
	url(r'^prueba', mostrarFormulario, name='prueba'),
	url(r'^general', ListConcursoTodo.as_view(), name='concursos_listartodo'),
	url(r'^listrubro', ListRubro.as_view(), name='rubro_listar'),
	url(r'^detalle/(?P<pk>\d+)$', views.ConcursosDetalleView.as_view(), name='concurso_detalle'),
	url(r'^eliminar/(?P<pk>\d+)$', views.ConcursosEliminarView.as_view(), name='concurso_eliminar'),
	url(r'^mi_pdf/(?P<pk>\d+)$', PDFPrueba.as_view(), name='mi_pdf'),

]


	# url(r'^listar', ListConcurso(), name='concursos_listar'),
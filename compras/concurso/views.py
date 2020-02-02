from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    DetailView,
    ListView,
    # UpdateView,
    # CreateView,
    DeleteView,
    # TemplateView,
)

from compras.utileria import render_pdf

from . import models
from .filters import ConcursoFilter
from .forms import ConsultaForm


def mostrarFormulario(request):
    context={'form':ConsultaForm(),}
    template='concurso/concurso_prueba.html'
    return render(request, template , context)


class ListConcurso(ListView):
    model = models.Concursos
    template_name = 'concurso/concurso_list.html'
    def get_queryset(self):
        queryset =super(ListConcurso,self).get_queryset()
        return queryset.filter(visible=False).filter(is_delete=False).filter(fecha_cad__gte =timezone.now())


class ListConcursoTodo(ListView):
    model = models.Concursos
    template_name = 'concurso/concurso_listtodo.html'
    
    def get_context_data(self, **kwargs):
        
        if self.request.GET.get('fecha_pub_0',) or self.request.GET.get('fecha_pub_1',):
            context = super().get_context_data(**kwargs)
            query = models.Concursos.objects.filter(is_delete=False)
            context.update({
                'filter': ConcursoFilter(self.request.GET, queryset=query),
                })
        else:
            context = super().get_context_data(**kwargs)
            query = models.Concursos.objects.none()
            context.update({
                'filter': ConcursoFilter(self.request.GET, queryset=query),
                })

        return context

    
class ConcursosDetalleView(DetailView):
    model = models.Concursos
    template_name = "concurso/concurso_detalle.html"


class ListRubro(ListView):
    model = models.Rubro
    template_name = "concurso/rubro_list.html"


class ConcursosEliminarView(DeleteView):
    model = models.Concursos
    template_name = 'concurso/concurso_eliminar.html'
    success_url = reverse_lazy('concurso:concursos_listar')


class PDFPrueba(DetailView):
    model = models.Concursos
    template_name ='concurso/mi_pdf.html'

    def get(self, request, *args, **kwargs):
        concursos = self.get_object()
        pdf = render_pdf("concurso/mi_pdf.html",  {"datos":concursos})
        return HttpResponse(pdf, content_type="application/pdf")

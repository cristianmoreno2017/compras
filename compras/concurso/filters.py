import django_filters

from . import models
from django_filters.filterset import FilterSet
from django_filters.widgets import RangeWidget
from django_filters.filters import Filter, RangeFilter


class ConcursoFilter(django_filters.FilterSet):

    fecha_pub = django_filters.DateFromToRangeFilter(name='fecha_pub', label='Fecha Publicación(rango)',widget=RangeWidget(attrs={'class': 'datepicker'}))

  #  fecha_pub=DateFromToRangeFilter(widget=RangeWidget(attrs={'placeholder': 'DD.MM.YYYY'}))
  
    class Meta:
        model = models.Concursos
        fields = ['fecha_pub', ]
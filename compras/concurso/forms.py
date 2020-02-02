from django import forms

class ConsultaForm(forms.Form):
	fecha_inicio= forms.DateField()
	
	
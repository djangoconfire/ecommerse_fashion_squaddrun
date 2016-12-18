from django import forms
from models import Ecommerse

class EcommerseForm(forms.ModelForm):
	class Meta:
		model=Ecommerse
		fields=['laptop']


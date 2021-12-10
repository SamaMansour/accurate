

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Medicine


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
class MedicineForm (forms.ModelForm):
    class Meta:
        fields = [
            'name', 
			'dosage', 
			'frequency'
        ]

class RawMedicineForm(forms.Form):
    name = forms.CharField(label = ' ', widget= forms.TextInput(attrs = {
        "placeholder" :"Name "
    }))
    dosage = forms.CharField(required=False, widget=forms.Textarea(attrs= {
        "class": "new-class-name two ",
        "id": "my-id-for -textarea",
        "rows": 100,
        "cols":120
    }
    ))
    frequency = forms.DecimalField(initial=199.99)
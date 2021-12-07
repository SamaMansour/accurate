from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import (authenticate
, get_user_model, 


)
User = get_user_model()
# class NewUserForm(UserCreationForm):
#     email = forms.EmailField(required = True)
#     class Meta:
#         model = User
#         fields = ("username", "email", "password1", "password2")

#     def save (self, commit=True):
#         user = super (NewUserForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user



class UserLoginForm (forms.Form):
    username = forms.CharField();
    password = forms.CharField(widget = forms.passwordInput);
    def clean (self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username= username, password=password)
            if not user:
                raise forms.ValidationError ('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError ('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError ('This user does not exist ')
        return super (UserLoginForm, self).clean (*args, **kwargs)





class UserRegisterationForm (form.ModelForm):
    username = forms.CharField(max_length=120)
    password = forms.CharField(widget=forms.PasswordInput)
    confirmPassword =password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model =User
        fields =[
            'username',
            'password',
            'confirmPassword'

            

        ]




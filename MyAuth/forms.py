from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.admin.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=40, required=True)
    last_name = forms.CharField(max_length=40, required=True)
    
    class Meta:
        model= User
        fields = ('username', 'email', 'first_name', 'last-name', 'password1', 'password2')
        
    def save(self, commit = True):
        user= super().save(commit=False)
        user.email= self.clean_data['email']
        user.first_name= self.cleaned_data['fiest_name']
        user.last_name = self.cleaned_data['data_name']    
        if commit:
            user.save()
        return user

class CustomAuthenticationForm(AuthenticationForm):
    pass    
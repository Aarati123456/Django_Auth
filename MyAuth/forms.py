from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.admin.models import User 


class customUserCreationform (UserCreationForm): 
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=40,required=True)
    last_name = forms.CharField(max_length=40,required=True)
    
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1','password2')
        
        def save(self, commit = True):
            user = super().save(commit=False)
            User.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            if commit:
                user.save()
                return user 
            
class CustomerAuthenticationForm(AuthenticationForm):
    pass

            
class CustomRegisterForm( forms.Form):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    first_name = forms.Charfield(max_length=50, required=True) 
    last_name = forms.CharField(max_length=50, required=True) 
    password1 = forms.CharField(label = 'password',widget = forms.passwordInput, required=True)  
    password2 = forms.CharField(label = 'password',widget = forms.passwordInput, required=True)      
    
    def clean_username(self):
         username= self.cleaned_data ['username']
         if  User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists') 
         return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')
        return email
    
    def clean(self):    
        cleaned_data= super(). clean()
        password1= cleaned_data.get('password1')
        password2= cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
           raise forms.ValidationError("password doesnot match")
        return cleaned_data
    
    class CustomLoginForm(forms.Form):
     username = forms.CharField (max_length=150, required=True)
    password = forms.CharField (widget=forms.PasswordInput, required=True)
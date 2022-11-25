from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User,policeModel,criminalModel



class policeReg(UserCreationForm):
    email = forms.EmailField(required=True)
    password = forms.PasswordInput()

    class Meta(UserCreationForm):
        model=User
        fields = ['id','email','username'] 
        
        
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_police = True
        user.save()
        plc = policeModel.objects.create(user=user)
        return user




class criminalReg(forms.ModelForm):
    class Meta:
        model=criminalModel
        fields= '__all__' 
        


        
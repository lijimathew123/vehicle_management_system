from django import forms
from .models import User,Vehicle

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
class VehicleUpdateForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicle_number', 'vehicle_type', 'vehicle_model', 'vehicle_description']

class VehicleAddForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicle_number', 'vehicle_type', 'vehicle_model', 'vehicle_description']

        
class AdminAddForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','username','password']
        widgets ={
            'password':forms.PasswordInput
        }
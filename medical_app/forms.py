from django import forms
from django.contrib.auth.forms import UserCreationForm
from medical_app.models import CustomUser,Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=CustomUser
        fields=('username','email','password1','password2','is_patient','is_doctor')
    def clean(self):
        cleaned_data=super().clean()
        password=cleaned_data.get('password1')
        confirm_password=cleaned_data.get('password2')
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password',"Passwords do not match")
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['is_patient'].widget = forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')])
        self.fields['is_doctor'].widget = forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')])
     

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['first_name','last_name','profile_picture','address_line1','city','state','pincode']
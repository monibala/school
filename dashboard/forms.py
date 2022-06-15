from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from myapp.models import Classes

from .models import Profile


class UpdateProfileForm(forms.ModelForm):
    class Meta :
        model = Profile
        fields = ('name','email','mobile_number')

class UpdateClassForm(forms.ModelForm):
	class Meta:
		model = Classes
		fields = ('name','images', 'description', 'seats','age', 'time', 'fee')

class adminform(forms.ModelForm):
	old_password = forms.CharField(label=("old_password"), required=True,
                                    widget=forms.PasswordInput)
	new_password = forms.CharField(label=("new_password"), required=True,
                                    widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ('old_password','new_password')
from django import forms

class PasswordResetRequestForm(forms.Form):
    email = forms.CharField(label=("Email"), max_length=254)	
		

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

class SetPasswordForm(forms.Form):
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
        }
    new_password1 = forms.CharField(label=("New password"), required=True,
                                    widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=("New password confirmation"), required=True,
                                    widget=forms.PasswordInput)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2
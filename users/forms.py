from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder":"Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password"}))

    class Meta:
        model = User
        fields = ['username', 'photo', 'email', 'phone', 'country', 'address', 'bio']

class UserUpdateForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder":"Email"}))

    class Meta:
        model = User
        fields = ['username', 'photo', 'email', 'phone', 'country', 'address', 'bio']

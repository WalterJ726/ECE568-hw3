from django import forms
from . import models
from catalog.utils.bootstrap import BootStrapForm, BootStrapModelForm
from catalog.utils.encrypt import md5
from django.core.exceptions import ValidationError

class LoginForm(BootStrapForm):
    username = forms.CharField(
        label="username",
        widget=forms.TextInput(),
        required=True,
    )

    password = forms.CharField(
        label="password",
        widget=forms.PasswordInput(render_value=True),
        required=True,
    )

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

class RegisterModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="confirm password",
        widget=forms.PasswordInput(render_value=True)
    )
    class Meta:
        model = models.User
        fields = ['username', 'password', 'confirm_password', 'email']
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }
    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("password does not match")
        return confirm
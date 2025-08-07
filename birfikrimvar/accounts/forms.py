from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm, UserChangeForm as BaseUserChangeForm
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from .models import User


class UserCreationForm(BaseUserCreationForm):
    """
    Form for creating a new user with all required fields
    """
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True


class UserChangeForm(BaseUserChangeForm):
    """
    Form for updating user information
    """
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class LoginForm(forms.Form):
    """
    Form for user login
    """
    username = forms.CharField(
        label=_('Kullanıcı Adı'),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label=_('Şifre'),
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    remember_me = forms.BooleanField(
        label=_('Beni hatırla'),
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            self.user = authenticate(username=username, password=password)
            if self.user is None:
                raise forms.ValidationError(_('Geçersiz kullanıcı adı veya şifre.'))
            elif not self.user.is_active:
                raise forms.ValidationError(_('Bu hesap aktif değil.'))
        return cleaned_data
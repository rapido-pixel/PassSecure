from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _
from pass_manager.models import Folder, PassCard


class CustomLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True,
                                                           'class': 'box-input',
                                                           'placeholder': 'Username'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',
                                          'class': 'box-input',
                                          'placeholder': 'Password'}),
    )


class CustomSignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(CustomSignUpForm, self).__init__(*args, **kwargs)

    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }

    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True,
                                                           'class': 'box-input',
                                                           'placeholder': 'Username'}))

    password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class': 'box-input',
                                          'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class': 'box-input',
                                          'placeholder': 'Password too'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )


class FolderForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'sidebar-item'
    }))

    class Meta:
        model = Folder
        fields = '__all__'


class PassCardForm(forms.ModelForm):
    name = forms.CharField(
        label='Название',
        widget=forms.TextInput(attrs={
            'class': 'card-input',
            'placeholder': 'Название'
        }))
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={
            'class': 'card-input',
            'placeholder': 'Имя пользователя'
        }))
    password = forms.CharField(
        label='Пароль',
        widget=forms.TextInput(attrs={
            'class': 'card-input',
            'placeholder': 'Пароль'
        }))
    site = forms.CharField(
        label='Сайт',
        widget=forms.TextInput(attrs={
            'class': 'card-input',
            'placeholder': 'Сайт'
        }))
    folder = forms.CharField(
        label='Папка',
        widget=forms.TextInput(attrs={
            'class': 'card-input',
            'placeholder': 'Папка'
        }))

    class Meta:
        model = PassCard
        fields = ('name', 'username', 'password', 'site')

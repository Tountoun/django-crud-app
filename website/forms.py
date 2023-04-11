from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'class': 'form-control fs-5', 'placeholder': 'Email Address'}
    ), help_text='<span class="form-text text-muted">Required. Email must contain @</span>', required=True)
    first_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control fs-5', 'placeholder': 'First Name'}
    ), help_text='<span class="form-text text-muted">Required. 150 characters or fewer. Letters, digits and @/./+/-/_ '
                 'only</span>', required=True)
    last_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control fs-5', 'placeholder': 'Last Name'}
    ), help_text='<span class="form-text text-muted">Required. 150 characters or fewer. Letters, digits and @/./+/-/_ '
                 'only</span>', required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control fs-5'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted">Required. 150 characters or fewer. ' \
                                            'Letters, digits and @/./+/-/_ only.</span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control fs-5'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<span class="form-text text-muted">Password can\'t be similar to ' \
                                             'personal informations. Mix of characters and numerics. At least 8 ' \
                                             'characters</span>'

        self.fields['password2'].widget.attrs['class'] = 'form-control fs-5'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted">Enter the same password as before, ' \
                                             'for verification.</span>'

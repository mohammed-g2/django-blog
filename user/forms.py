from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    agree_on_terms = forms.BooleanField(label=f"""agree on <a href="/blog/terms">terms</a>""")

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
            if user:
                raise forms.ValidationError('please use another email')
        except (User.DoesNotExist):
            return email
        
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
            if user:
                raise forms.ValidationError('please use another email')
        except (User.DoesNotExist):
            return email

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea,
        help_text='bio can\'t be longer than 256 characters')

    class Meta:
        model = Profile
        fields = ['image', 'bio']


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150, 
        error_messages={'required': 'username required'})
    password = forms.CharField(widget=forms.PasswordInput(),
        error_messages={'required': 'password required'})


class PasswordResetForm(forms.Form):
    email = forms.EmailField(required=True)
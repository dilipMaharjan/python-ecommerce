from django import forms
from django.contrib.auth import get_user_model


class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=
        forms.TextInput(attrs=
                        {"class": "form-control",
                         "placeholder": "Your Fullname"
                         }))
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control",
                   "placeholder": "Your Content"
                   }))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control",
                   "placeholder": "Your Email"
                   }))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not "gmail.com" in email:
            raise forms.ValidationError("Email should be gmail")
        return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        User = get_user_model()
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Username is already taken.')
        return username

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passowrd must match.")
        return data

from django import forms

class BlogForm(forms.Form):
    title = forms.CharField(max_length=255, required=True)
    content = forms.CharField(widget=forms.Textarea, required=True)
    date = forms.DateField(required=True)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
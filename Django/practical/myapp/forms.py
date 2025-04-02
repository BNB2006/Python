from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label="Username")
    email = forms.EmailField(max_length=50, label="Email")
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(max_length=50, widget=forms.PasswordInput, label="Confirm Password")
    first_name = forms.CharField(max_length=50, label="First Name")
    last_name = forms.CharField(max_length=50, label="Last Name")
    phone_number = forms.IntegerField(label="Phone Number")
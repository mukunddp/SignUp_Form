from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ImageUploadForm(forms.Form):
    profile_photo = forms.ImageField()


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    user_type = forms.CharField(max_length=20)
    address_line1 = forms.CharField(max_length=200)
    city = forms.CharField(max_length=50)
    state = forms.CharField( max_length=50)
    pincode = forms.IntegerField()

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'password1', 'password2','user_type',
                  'address_line1','city','state','pincode')
from django import forms
from django.contrib.auth.forms import UserCreationForm


from .models import User
from .models import BlogPost,Category
class LoginForm(forms.Form):
   username = forms.CharField(max_length=20)
   password = forms.CharField(widget=forms.PasswordInput,max_length=30)



class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=20, required=False)
    last_name = forms.CharField(max_length=20, required=False)
    profile_picture = forms.ImageField(required=False)
    address_line1 = forms.CharField(max_length=20,required=False)

    city = forms.CharField(max_length=20, required=False)
    state = forms.CharField(max_length=20, required=False)
    pincode = forms.IntegerField(required=False)



    class Meta:
        model = User
        fields = ( 'username','email','password1','password2','first_name','last_name','profile_picture','address_line1','city','state','pincode','is_doctor','is_patient')
       


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['Title','Image','Category','Summary','Content','is_draft']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
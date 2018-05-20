from django import forms

from .models import *

from django.contrib.auth.models import User

class ImagePostForm(forms.ModelForm):
    place = forms.CharField(max_length=120)
    mainimage = forms.FileField()

    class Meta:
        model = AddImage
        fields = ('place','mainimage', )

class MainImageForm(forms.ModelForm):
    place = forms.CharField(max_length=120)
    shortdescription = forms.CharField(max_length=80)
    image = forms.FileField()

    class Meta:
        model = MainImage
        fields = ('place','shortdescription','image', )


class ImageForm(forms.ModelForm):
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Images
        fields = ('image', )

class OrderForm(forms.ModelForm):
    Name = forms.CharField(max_length=120)
    Phone = forms.CharField(max_length=10)
    class Meta:
        model = Buyers
        fields = ('Name', 'Phone', )

class BlogForm(forms.ModelForm):
    place = forms.CharField(max_length=120)
    Description = forms.CharField(widget=forms.Textarea)
    mainimage = forms.FileField()


    class Meta:
        model = Blog
        fields = ('place', 'Description','mainimage',)

class BlogImageForm(forms.ModelForm):
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = BlogImages
        fields = ('image', )

class CaptionForm(forms.ModelForm):
    image_caption = forms.CharField()
    class Meta:
        model = Caption
        fields = ('image_caption',)

class ImageCaptionForm(forms.ModelForm):
    image_caption = forms.CharField()
    class Meta:
        model = ImageCaption
        fields = ('image_caption',)

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-solid placeholder-no-fix',
        'required': 'true',
        'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-solid placeholder-no-fix',
        'required': 'true',
        'placeholder': 'Password', }))

    class Meta:
        fields = [
            "username",
            "password",
        ]

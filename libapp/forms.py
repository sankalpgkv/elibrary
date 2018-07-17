from django.contrib.auth.models import User
from django import forms  
from .models import Review

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['book', 'user', 'review_text']
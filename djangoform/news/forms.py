from django import forms
from django.db.models import fields
from django.forms.widgets import Textarea
from .models import Post
from bootstrap_datepicker_plus import DatePickerInput

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'time_created']
        widgets = {
            'time_created': DatePickerInput(),
        }

class SendEmail(forms.Form):
    title = forms.CharField(max_length=100)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)
    cc =  forms.BooleanField()
    

from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, SendEmail
from django.views import View

# Create your views here.
def hello(request):
    return HttpResponse('Hello LHT')

# Class base view
class HelloClass(View):
    def get(self, request):
        return HttpResponse('Hello LHT')


def add_post(request):
    f = PostForm()
    return render(request, 'news/post_content.html', {'f' : f})

def send_email(request):
    f = SendEmail()
    return render(request, 'news/send_email.html', {'f' : f})

def save_post(request):
    if request.method == 'POST':
        # Catch form
        f = PostForm(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponse('saved')
        else:
            return HttpResponse('invalid post')
    else:
        HttpResponse('Kp POST request')

def save_email(request):
    if request.method == 'POST':
        # Catch form
        f = SendEmail(request.POST)
        if f.is_valid():
            context = {'t':f.cleaned_data['title'], 'e':f.cleaned_data['email'], 'c':f.cleaned_data['content'], 'cc':f.cleaned_data['cc']}
            return render(request, 'news/print_email.html', context)
        else:
            return HttpResponse('invalid email')
    else:
        HttpResponse('Kp POST request')
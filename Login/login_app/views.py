from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm

# Create your views here.
class hello(View):
    def get(self, request):
        return HttpResponse('<h1>Xin chao</h1>')

class login(View):
    def get(self, request):
        # context = {'login_info' : Login_info()}
        return render(request, 'login_app/login.html')
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            return HttpResponse('user valid')
        else:
            # No backend authenticated the credentials
            return HttpResponse('user invalid')

class viewUser(LoginRequiredMixin, View):
    login_url='login'
    def get(self, request):
        return HttpResponse('<h1> Day la view user </h1>')

@decorators.login_required(login_url='login')
def view_product(request):
    return HttpResponse('Product')


class AddPost(LoginRequiredMixin, View):
    login_url='login'
    def get(self, request):
        post_form = PostForm()
        return render(request, 'login_app/add_post.html', {'post_form':post_form})
    
    def post(self, request):
        f = PostForm(request.POST)
        if f.is_valid():
            if request.user.has_perm('login_app.add_post'):
                f.save
            else:
                HttpResponse('Khong co quyen')
            return HttpResponse('oke')

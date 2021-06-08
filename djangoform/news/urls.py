from django.urls import path
from . import views

urlpatterns = [
    path('', views.HelloClass.as_view(), name='hello'),
    path('add', views.add_post, name='add'),
    path('save', views.save_post, name='save'),
    path('email', views.send_email, name='email'),
    path('saveemail', views.save_email, name='saveemail'),
]

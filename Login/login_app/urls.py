from django.urls import path
from . import views

urlpatterns = [
    path('login1', views.login.as_view(), name='login'),
    path('view-user', views.viewUser.as_view()),
    path('view-pro', views.view_product),
    path('add-post', views.AddPost.as_view(), name='add_post'),
]

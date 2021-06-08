from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('list', views.view_db),
    path('detail/<int:qs_id>', views.detail_view, name='detail'),
    path('<int:qs_id>', views.votes, name='votes'),
]
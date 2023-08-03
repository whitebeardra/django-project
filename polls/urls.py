from django.urls import path
from polls import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
from django.urls import path
from . import views

urlpatterns = [
    # 127.0.01.:8000 it will take u too the post_list.html
    path('', views.post_list, name='post_list'), # it will go here post_list.html
]

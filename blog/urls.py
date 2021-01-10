from django.urls import path
from . import views

urlpatterns = [
    # 127.0.0.1:8000 --> local
    #mydjangosite.com -- > final app online

    # 127.0.01.:8000 it will take u too the post_list.html
    path('', views.post_list, name='post_list'),# it will go here post_list.html

    #127.0.0.1:8000/post/2 --> local for primary Key
    # mydangosite.com/post/2 === online

    #127.0.0.1:8000/post/2 <int:pk> <------taht replaced or passed by 2 = pk replaced ,which has primary key of it indicates in the post
    path('post/<int:pk>/', views.post_detail, name='post_detail')
]

from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    # 127.0.0.1:8000 --> local
    # mydjangosite.com -- > final app online

    # 127.0.01.:8000 it will take u too the post_list.html
    path('', views.post_list, name='post_list'),  # it will go here post_list.html

    # 127.0.0.1:8000/post/2 --> local for primary Key
    # mydangosite.com/post/2 === online

    # 127.0.0.1:8000/post/2 <int:pk> <------taht replaced or passed by 2 = pk replaced ,which has primary key of it indicates in the post
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    # 127.0.0.1:8000/post/new ---> local
    # mydangosite.com/post/new----> online
    path('post/new', views.post_new, name='post_new'),

    # 127.0.0.1:8000/post/2/edit ----> local
    # mydangosite.com/post/2/edit --> online
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    # 127.0.0.1:8000/post/2/delete ----> local
    # mydangosite.com/post/2/delete --> online
    path('post/<int:pk>/delete/', views.post_delete,name='post_delete'),

    # 127.0.0.1:8000/drafts ----> local
    # mydangosite.com/drafts --> online
    path('drafts/', views.post_draft_list, name='post_draft_list'),

    # 127.0.0.1:8000/post/2/publish ----> local
    # mydangosite.com/post/2/publish --> online pk=2
    path('post/<int:pk>/publish', views.post_publish, name='post_publish'),

    # 127.0.0.1:8000/post/2/comment ----> local
    # mydangosite.com/post/2/comment --> online pk=2
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),

    # 127.0.0.1:8000/comment/2/remove----> local
    # mydangosite.com/comment/2/remove --> online pk=2
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),

    # 127.0.0.1:8000/comment/2/approve----> local
    # mydangosite.com/comment/2/approve --> online pk=2
    path('comment/<int:pk>/approve', views.comment_approve, name='comment_approve'),

    # 127.0.0.1:8000/signup----> local
    # mydangosite.com/signup --> online
    path('signup/', views.signup, name='signup')

]


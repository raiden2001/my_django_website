from django.shortcuts import render
from django.utils import timezone
from .models import Post


# Create your views here.
# this refers post_lists links to the html file

def post_list(request):
    # this command is to make sure if the publication date is exiist when usig the boolean
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    stuff_for_frontend = {'posts': posts}  # posts is value where to u will store in the html in for loop
    return render(request, 'blog/post_list.html', stuff_for_frontend)

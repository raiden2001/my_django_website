from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


# Create your views here.
# this refers post_lists links to the html file

def post_list(request):
    # this command is to make sure if the publication date is exiist when usig the boolean
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    stuff_for_frontend = {'posts': posts}  # posts is value where to u will store in the html in for loop
    return render(request, 'blog/post_list.html', stuff_for_frontend)


    # from the urlspy the pk:2 is going to pass to this function here
def post_detail(request, pk):  # as soon as you click on page
    # u need the primary key to access the site
    post = get_object_or_404(Post, pk=pk)
    # Post will set as pk
    # if its ges post as primary key or else gives error 404
    stuff_for_frontend = {'post': post}
    return render(request, 'blog/post_detail.html', stuff_for_frontend)

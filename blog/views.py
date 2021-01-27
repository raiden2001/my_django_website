from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import PostForm, CommentForm
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


# brints from url
@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # this not comitt database yet
            post.author = request.user  # use superuser to put that in datbases
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)  # redirect refresh , not submit another form
        # oif somebody post request form and run all of this aobve code
        # takes me to the detial of the post  http://127.0.0.1:8000/post/2/
        # where 2 is the primary key(pk)
    else:
        # print(request.POST)  using git hub using this code below
        form = PostForm()
        stuff_for_frontend = {'form': form}
    return render(request, 'blog/post_edit.html', stuff_for_frontend)


@login_required
def post_edit(request, pk):  # we need the pk for the specific post
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':  # sends me to post of this page and sumbit a form

        # creat the form and update the exisitng form  from request
        # whereever the user has submitted
        form = PostForm(request.POST, instance=post)
        # if the form is valid then update the form then
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # gets superuser
            # post.published_date = timezone.now()
            post.save()
            # redirect to post detial once and use pk of actual post
            return redirect('post_detail', pk=post.pk)
        # oif somebody post request form and run all of this above code
        # after u hit save from edit.html to takes me to the detail of the post to  http://127.0.0.1:8000/post/2/
        # where /2 is the primary key(pk)
    else:
        form = PostForm(instance=post)  # show post form
        # use instane existing block post and render post and sendto front end
        stuff_for_frontend = {'form': form, 'post': post}
    return render(request, 'blog/post_edit.html', stuff_for_frontend)
    # gets back to edit post


@login_required
def post_draft_list(request):
    # want you to show all of my  draft by decending order
    # send them to the post_draft_list.html for review
    posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    stuff_for_frontend = {'posts': posts}
    return render(request, 'blog/post_draft_list.html', stuff_for_frontend)
    # takes u to front end to the post_draft_list


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()  # this was created in our models
    return redirect('post_detail', pk=pk)


# use block post must have primary key get to specific blog post
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user  # obtains the superuse
            comment.post = post  # gets the post from Post we got previously
            comment.save()  # saves comment
            return redirect('post_detail', pk=post.pk) # main page
            # goes to the post detials  use of the primray key
    else:
        form = CommentForm()
        stuff_for_frontend = {'form': form}

    return render(request, 'blog/add_comment_to_post.html', stuff_for_frontend )

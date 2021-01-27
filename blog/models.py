from django.db import models
from django.utils import timezone


class Post(models.Model):
    # post nees to do
    # each post is related to author
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=288)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # published the object
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # creates a string representation
    def __str__(self):
        return self.title
        # return str(self.title) + ' by ' + str(self.author)
        # u use that if u want more information by the string


# inhertance from Model
# a comment is needed with a post
class Comment(models.Model):
    # if comments gets deleted in the block post in CASCADE model
    # it will delete all of the comments
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)  # when u create comment , the comment create now

    def __str__(self):  # creates string for parenthesisi
        return self.text

# Post.objects.get(pk=2).comments.all() = one specfic post givers all oif that post  comments
# thanks to the related name

# from function comment : for example: hahah greate job.post --- >  which porgramming i should turn on

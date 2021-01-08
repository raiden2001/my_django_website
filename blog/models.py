from django.db import models
from django.utils import timezone

class Post(models.Model):
    # piost nees to do
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
        #return str(self.title) + ' by ' + str(self.author)
            #u use that if u want more information by the string
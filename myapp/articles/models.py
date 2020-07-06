from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length = 30)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body if len(self.body) <= 25 else self.body[0:25] + '...'
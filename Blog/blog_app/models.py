from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:300]+'...'
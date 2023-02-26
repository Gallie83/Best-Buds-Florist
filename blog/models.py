from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    intro = models.TextField()
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)


class Comments(models.Model):
    post = models.ForeignKey(
        BlogPost, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']

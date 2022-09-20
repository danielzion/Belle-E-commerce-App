from distutils.command.upload import upload
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Blog(models.Model):
    images = models.ImageField(upload_to='blog_images', blank=True, null=True)
    title = models.CharField(max_length=10000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=1000)
    category = models.ForeignKey('BlogCategory', on_delete=models.CASCADE)
    # likes= models.IntegerField(default=0)
    # dislikes= models.IntegerField(default=0)
      
    def __str__(self):
        return self.title

    @property
    def number_of_comments(self):
        return Comment.objects.filter(post_connected=self).count()

    def get_image(self):
        if self.images and hasattr(self.images, 'url'):
            return self.images.url
        else:
            return 'path/to/default/image'


class BlogCategory(models.Model):
    name = models.CharField(verbose_name='name', max_length=150)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child', on_delete=models.CASCADE)
    class Meta:
        unique_together = ('name', 'parent',)
        verbose_name_plural = "categories"

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])

class Comment(models.Model):
    content = models.TextField(max_length=150)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_connected = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_connected.title


class Preference(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    post= models.ForeignKey(Blog, on_delete=models.CASCADE)
    value= models.IntegerField()
    date= models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.user) + ':' + str(self.post) +':' + str(self.value)

    class Meta:
       unique_together = ("user", "post", "value")



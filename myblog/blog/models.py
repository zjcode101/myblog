from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# 文章分类


class Category(models.Model):
    name = models.CharField('博客分类', max_length=100)
    def __str__(self):
        return self.name


# 文章标签

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 推荐位


class Tui(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 文章


class Article(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag, blank=True)
    tui = models.ForeignKey(Tui, on_delete = models.DO_NOTHING, blank=True)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    img = models.ImageField(upload_to='article_img/%Y/%m/%d/', blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Banner


class Banner(models.Model):
    text_info = models.CharField(max_length=50, default='')
    img = models.ImageField(upload_to='banner/')
    link_url = models.URLField(max_length=100)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.text_info

# 友情链接


class Link(models.Model):
    name = models.CharField(max_length=50)
    linkurl = models.URLField(max_length=100)
    
    def __str__(self):
        return self.name
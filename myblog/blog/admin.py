from django.contrib import admin
from .models import Category, Tui, Tag, Article, Banner, Link

# Register your models here.

admin.site.register(Category)
admin.site.register(Tui)
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Link)
admin.site.register(Banner)
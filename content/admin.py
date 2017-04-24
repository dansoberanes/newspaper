from django.contrib import admin

from .models import Content, Article, Contributor

admin.site.register(Article)
admin.site.register(Contributor)

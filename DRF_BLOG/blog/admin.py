from django.contrib import admin

from blog.models import Category, Post

# Register your models here.

admin.site.register(Category)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
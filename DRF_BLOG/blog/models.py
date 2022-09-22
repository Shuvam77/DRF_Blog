from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status = 'publish')

    options =(
        ('draft', 'DRAFT'),
        ('publish', 'PUBLISH')
    )

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=2)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'blog_posts')
    status = models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager() #Default manager
    postobjects = PostObjects() #Custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     return super().save(*args, **kwargs)

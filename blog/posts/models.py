from django.db import models
from django.utils import timezone
from slugger import AutoSlugField
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

def upload_location(instance, filename):
    return "%s/%s" %(instance.slug, filename)
    
class Category(models.Model):
    title = models.CharField(max_length= 60)
    slug = AutoSlugField(populate_from='title')
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children',on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title
    
    def __str__(self):
        return self.title



class Post(models.Model):
    title = models.CharField(max_length=120)
    slug = AutoSlugField(populate_from='title')
    image = models.ImageField(
        upload_to=upload_location,
        null=True, 
        blank=True,
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    

    def get_absolute_url(self, slug=None):
        return reverse("posts-detail", kwargs={"slug": self.slug})
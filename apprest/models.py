import re
from django.db import models

class TVManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['titleOfShow'])<1:
            errors['titleOfShow'] = 'title cannot be empty'
        if len(post_data['networkName'])<1:
            errors['netWorkName'] = 'network cannot be empty'
        if len(post_data['showDesc'])<1:
            errors['showDesc'] = 'description cannot be empty'
        return errors

class TVShow(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = TVManager()
    
    
# TVShow.objects.create(title = 'Justified', network="Hulu", release = "2010-04-02",description="A show about us marshalls")
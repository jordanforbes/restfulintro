from django.db import models

class TVShow(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
# TVShow.objects.create(title = 'Justified', network="Hulu", release = "2010-04-02",description="A show about us marshalls")
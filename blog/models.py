from django.db import models
from django.conf import settings


class TimespamModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True

# Create your models here.
class Post(TimespamModel):
    #author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title= models.CharField(max_length=255)
    body= models.TextField()

    def __str__(self):
        return self.title
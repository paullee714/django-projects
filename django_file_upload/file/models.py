from django.db import models

# Create your models here.
class MyPost(models.Model):
    title = models.CharField(max_length=180)
    post = models.TextField()
    upload_user = models.CharField(max_length=100,default=None)
    file = models.FileField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('id'),)

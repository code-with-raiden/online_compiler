from django.db import models

class Submission(models.Model):
    code = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

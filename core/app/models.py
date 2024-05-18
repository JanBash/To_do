from django.db import models

class ToDO(models.Model):
    title = models.CharField(
        max_length=50
    )
    description = models.TextField()
    completed = models.BooleanField(
        default = False
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    updated_date = models.DateTimeField(
        auto_now = True
    )

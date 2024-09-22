from django.db import models
from django.contrib.auth.models import User 


class Todo(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)


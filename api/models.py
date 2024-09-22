from django.db import models
from django.contrib.auth.models import User 

class Category(models.Model):
	"""
		Model for Category of todos
	"""
	title = models.CharField(max_length=250)
	created_at = models.DateTimeField(auto_now_add=True)
	color = models.CharField(max_length=10)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")

	def __str__(self) -> str:
		return self.title

class Todo(models.Model):
	"""
		Model for todos
	"""
	title = models.CharField(max_length=500)
	created_at = models.DateTimeField(auto_now_add=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="todos")
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
	
	def __str__(self) -> str:
		return self.title


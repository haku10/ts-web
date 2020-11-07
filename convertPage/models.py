from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
  id = models.AutoField(primary_key=True)
  author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
  full_name = models.TextField(max_length=100)
  email = models.TextField(max_length=100)
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.title

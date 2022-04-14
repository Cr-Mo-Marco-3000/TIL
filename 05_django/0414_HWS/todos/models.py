from email.policy import default
from django.db import models
from django.conf import settings
# Create your models here.

class Todo(models.Model):
    # models.py에서 User를 부르는 경우 요렇게 부른다.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
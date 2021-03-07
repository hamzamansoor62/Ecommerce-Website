from django.db import models
from django.contrib.auth.models import auth, User

# Create your models here.
class user(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
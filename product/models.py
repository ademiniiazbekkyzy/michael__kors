from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Category(models.Model):
    slug = Modelgos.SlugField(max_length=30, primary_key=True)
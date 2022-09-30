from django.db import models

# Create your models here.
# todo  IMPORTANT: Apply makemigrations and migrate anytime models are modified

#todo NOTES: mapped this class to databases using "models"
# Remember add the app in settings.py INSTALLED_APPS
class Product(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.TextField()
    summary = models.TextField(default='this is cool!')

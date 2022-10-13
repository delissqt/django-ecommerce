from django.db import models

# Create your models here.
# todo  IMPORTANT: Apply makemigrations and migrate anytime models are modified

#todo NOTES: mapped this class to databases using "models"
# Remember add the app in settings.py INSTALLED_APPS


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    summary = models.TextField(blank=False, null=False)
    feature = models.BooleanField(default=False)


    def get_absolute_url(self):
        return f"/products/{self.id}/"

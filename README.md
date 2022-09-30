# NOTES

## Create elements in the python shell

example existing Product Model

````commandline
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.TextField()
    summary = models.TextField(default='this is cool!')
````

Command for open python shell project

``python manage.py shell``

Create Product from python shell

``````commandline
 from products.models import Product
>>> Product.objects.all()
<QuerySet [<Product: Product object (1)>]>
>>> Product.objects.create( title='mytitle', description='mydescription', price='123', summary='mysummary') 
<Product: Product object (2)>
``````

Go to Admin panel in order to view the new product created

``127.0.0.1/admin``
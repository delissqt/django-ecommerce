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


## Views 

Think of views as a place that handle your various web pages.

## ULR in Django project
 There are two ways to import and use urls.py

Way 1 
``````commandline
from django.contrib import admin
from django.urls import path

from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home')
]
``````

Way 2
``````commandline
from django.contrib import admin
from django.urls import path

from pages.views import home_view 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
]
``````


## Overwrite default widget in forms

TODO is possible to overwrite the default widget putting  the word "widget=" see the next example

````commandline
class RawProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField()
````

2:48.39
you´re noticing is that if a commentd this out (class Meta) and Change the form, to the form itself
will render the exact same, all of the validation will render the same, all of that.
But of course, the one caveat is how the actual form would work. In the view, it is slightly different

````commandline
class ProductForm(forms.Form):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            "placeholder": "Title place holder"
        })
    )

    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "new-class-name two",
                "id": "id-for-textarea",
                "rows": "5",
                "cols": "6",
                "placeholder": "description is here"
            }
        ))
    price = forms.DecimalField(initial=199.99)

    email = forms.EmailField()

    #class Meta:
     #   model = Product
    #    fields = [
    #        'title',
     #       'description',
     #       'price',
            # 'summary',
            # 'feature',
     #   ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("This is not a valid title")

        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")
        return email
````


Dynamic url
NOTE: in dynamic_lookup_view funtion by default we have "request" parameter,
is important to call the other one how was definied in urls.py file, in this case 
was called as "my_id"
In other words in bout places the paramater have the same name 

`views.py`
````commandline
def dynamic_lookup_view (request, my_id):
    obj = Product.objects.get(id=my_id)
    context = {
        "objects": obj
    }
    return render(request, "products/product_detail.html", context)
````


`urls.py`
````commandline
from products.views import  dynamic_lookup_view

urlpatterns = [
    path('products/<int:my_id>/', dynamic_lookup_view, name='product'),
]
````
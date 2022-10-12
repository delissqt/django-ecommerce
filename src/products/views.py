from django.shortcuts import render

from django.shortcuts import Http404
from django.shortcuts import render, get_object_or_404

from .models import Product

from .forms import ProductForm, RawProductForm


# Create your views here.

def render_initial_data(request):
    initial_data = {
        'title': "My awesome title",
    }

    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, initial=initial_data, instance=obj)
    # form = RawProductForm(request.POST or None, initial=initial_data, instance=obj)

    print('form valid', form.is_valid())
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    return render(request, "product/product_create.html", context)


# dynamic URL
def dynamic_lookup_view(request, my_id):
    # obj = Product.objects.get(id=my_id) # display the exception error
    # obj = get_object_or_404(Product, id=id)
    try:
        obj = Product.objects.get(id=my_id)
    except Product.DoesNotExist:
        raise Http404

    context = {
        'object': obj
    }
    return render(request, "product/detail.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    #     'price': obj.price,
    # }

    context = {
        'object': obj
    }
    return render(request, "product/detail.html", context)


def product_create_view(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = ProductForm() # rerender the form (clean the form)

    context = {
        'form': form
    }
    return render(request, 'product/product_create.html', context)


# def product_form_view(request):
#     # print(f'get, {request.GET}')
#     # print(f'post, {request.POST}')
#
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#
#     context = {}
#     return render(request, 'product/product_create.html', context)


# def product_form_view(request):
#     my_form = RawProductForm(request.GET)
#
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#
#         if my_form.is_valid():
#             #the data is good
#             print("--", my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#
#     context = {
#         "form": my_form
#     }
#     return render(request, 'product/product_create.html', context)

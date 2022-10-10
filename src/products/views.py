from django.shortcuts import render

from .models import Product

from .forms import ProductForm, RawProductForm


# Create your views here.
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


# def product_form_view(request):
#     form = ProductForm(request.POST or None)
#
#     if form.is_valid():
#         form.save()
#         form = ProductForm() # rerender the form (clean the form)
#
#     context = {
#         'form': form
#     }
#     return render(request, 'product/product_create.html', context)


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


def product_form_view(request):
    form = RawProductForm(request.GET)

    if request.method == "POST":
        my_form = RawProductForm(request.POST)

        if my_form.is_valid():
            #the data is good
            print("--", my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)

    context = {
        "form": my_form
    }
    return render(request, 'product/product_create.html', context)

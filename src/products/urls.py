from django.urls import path
from .views import (
    product_create_view,
    product_detail_view,
    product_delete_view,
    product_list_view,
    dynamic_lookup_view,
    render_initial_data,
)

urlpatterns = [
    path('', product_list_view, name='products_list'),
    path('create/', product_create_view),
    path('product/', product_detail_view),

    # path('ps/<int:my_id>/', dynamic_lookup_view, name='product'), # todo try changing pd by products/ this will keep working
    path('<int:id>/delete/', product_delete_view, name='product-delete'),

    path('<int:my_id>/', dynamic_lookup_view, name='product'),
    path('initial/', render_initial_data),
]
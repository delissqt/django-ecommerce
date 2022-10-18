from django.urls import path
from .views import (
    CourseView,
    CourseListView,
    # MyListView,
    my_function_base_view
)

app_name = 'courses'

urlpatterns = [
    path('', CourseListView.as_view(), name='courses-list'),
    # TODO RENDER ONY ONE PRODUCT WITH ID=1
    # path('', MyListView.as_view(), name='courses-list'),

    # path('', my_function_base_view, name='course-list'),
    path('<int:id>/', CourseView.as_view(), name="courses-detail"),
]

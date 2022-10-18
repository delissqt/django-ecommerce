from django.urls import path
from .views import (
    CourseView,
    my_function_base_view
)

app_name = 'courses'

urlpatterns = [
    path('', CourseView.as_view(template_name='contact.html'), name='courses-list'),
    # path('', my_function_base_view, name='course-list'),
]
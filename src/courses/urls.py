from django.urls import path
from .views import (
    CourseView,
    my_function_base_view,
)

app_name = 'courses'

url_patterns = [
    path('', CourseView.as_view(template_name='contact.html'), name='courses-list'),
    path('<int:id>/', CourseView.as_view(), name='courses-detail'),
    # path('', my_function_base_view, name='course-list'),
]
from django.shortcuts import render, get_object_or_404
from django.views import View


from .models import Course

# Create your views here.


#BASE VIEW CLASS = VIEW
class CourseView(View):
    template_name = "courses/course_detail.html" # Detail View

    def get(self, request, id=None, *args, **kwargs):
        # get is the default
        context = {}

        if id is not None:
            obj = get_object_or_404(Course, id=id)
            context['object'] = obj
        return render(request, self.template_name, context)

    # def post => that´s actually how you´d handle a form
    # def post(self, request, *args, **kwargs):
    #     return render(request, 'about.html', {})


#HTTP METHODS
def my_function_base_view(request, *args, **kwargs):
    print(request.method)
    return render(request, 'about.html', {})

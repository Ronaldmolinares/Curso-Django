from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from my_first_app.models import Car


# Create your views here.
def my_view(request):
    cars = [
        {"name": "Toyota"},
        {"name": "Honda"},
        {"name": "Ford"},
    ]

    context = {"cars": cars}

    return render(request, "my_first_app/car_list.html", context)


class CarListView(TemplateView):
    template_name = "my_first_app/car_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['cars'] = Car.objects.all()
        
        return context



def my_test_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("ok")

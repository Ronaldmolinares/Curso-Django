from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def my_view(request):
    cars = [
        {"name": "Toyota"},
        {"name": "Honda"},
        {"name": "Ford"},
    ]

    context = {"cars": cars}

    return render(request, "my_first_app/car_list.html", context)


def my_test_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("ok")

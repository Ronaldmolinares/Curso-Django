from profile import Profile

from django.http import HttpResponse
from django.urls import path

from my_first_app.models import Author

from .views import CarListView, my_test_view


def author_view(request, *args, **kwargs):
    print(args)
    print(kwargs)

    author = Author.objects.get(id=kwargs["id"])
    profile = Profile.objects.get(author_id=kwargs["id"])
    return HttpResponse(
        f"Author: {author.name} - Website: {profile.website} - Biografia: {profile.biography} "
    )


urlpatterns = [
    # path("listado", my_view),
    path("listado", CarListView.as_view()),
    path("detalle/<int:car_id>", my_test_view),
    path("marcas/<str:brand_name>", my_test_view),
    path("autor/<int:author_id>", author_view),
]

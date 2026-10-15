from django.urls import path

from .views import ProductFormView, SuccessView

urlpatterns = [
    path("", SuccessView.as_view(), name="success"),
    path("agregar/", ProductFormView.as_view(), name="add_product"),
]

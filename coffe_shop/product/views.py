from django.urls import reverse_lazy
from django.views import generic

from .forms import ProductForm
from .models import Product


# Create your views here.
class ProductFormView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("success")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class SuccessView(generic.TemplateView):
    template_name = "products/success.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        return context

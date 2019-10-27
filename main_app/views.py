from django.views.generic import ListView,TemplateView

from . models import Quote
from . models import QuoteCategory

# class HomeView(TemplateView):
#     template_name = "index.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['Name'] = "Munim"
#         context['Country'] = "Bangladesh"

#         list = [1,2,3,4,45,6]
#         context['list'] = list


#         return context

class HomeView(ListView):
    template_name = "home.html"
    model = Quote

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related
        ('quote_category')  

# class AboutView(TemplateView):
#     template_name = "about.html"


# Create your views here.

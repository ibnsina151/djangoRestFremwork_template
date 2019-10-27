from rest_framework import generics

from main_app.models import Quote
from main_app.models import QuoteCategory

from . serializers import QuoteSerializer
from . serializers import QuoteCategorySerializer

class QuoteAPIView(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

class QuoteCategoryAPIView(generics.ListAPIView):
    queryset = QuoteCategory.objects.all()
    serializer_class = QuoteCategorySerializer

class QuoteAPINewView(generics.ListCreateAPIView):
    queryset = Quote.objects.all().order_by('-id')[:1] # latest quote
    serializer_class = QuoteSerializer

class QuoteAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
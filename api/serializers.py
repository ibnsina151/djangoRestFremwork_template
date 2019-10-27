from rest_framework import serializers

from main_app.models import Quote
from main_app.models import QuoteCategory 

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote 
        # ('__all__')  for all fields
        # ['quote', 'author']
        # fields = ['quote', 'author']
        fields = ('__all__')

class QuoteCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteCategory 
        # ('__all__')  for all fields
        # ['title']
        fields = ('__all__')
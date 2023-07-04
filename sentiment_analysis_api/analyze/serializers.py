from rest_framework import serializers
from rest_framework.fields import empty
from .models import Analysis


# Serializer for the model 'Analysis' to work with REST API
class AnalysisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Analysis
        fields = '__all__'

    def __init__(self, instance=None, data=..., **kwargs):
        super().__init__(instance, data, **kwargs)
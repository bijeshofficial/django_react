from rest_framework import serializers
from .models import Lead

#Lead Serializers
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
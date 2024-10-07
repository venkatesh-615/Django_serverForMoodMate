# analysis/serializers.py
from rest_framework import serializers

class EmotionSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=512)
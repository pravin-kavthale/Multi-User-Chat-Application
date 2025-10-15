from rest_framework import serializers
from .models import Messages

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Messages
        fields=['id','room','content','role','timestamp']
        
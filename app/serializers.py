from rest_framework import serializers
from app.models import Agreement

class agreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = "__all__"

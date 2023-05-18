from rest_framework import serializers
from app.models import Agreement, Review

class agreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = ["title", "content", "creator"]


class reviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
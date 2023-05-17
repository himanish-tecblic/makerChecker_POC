from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import *
import json
from app.serializers import agreementSerializer, reviewSerializer
# Create your views here.
# def home(request):
#     return HttpResponse("hello")


class Maker(APIView):
    
    def post(self, request):
        if request.data:
                serializer = agreementSerializer(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    aggrement = serializer.save()
                    user = aggrement.creator
                    creater = User.objects.get(name=user)   
                    
        response = {
            "status": "success",
        }
        return Response(response, status=status.HTTP_200_OK)
    
    
class Reviwer(APIView):
    
    def post(self, request):
        if request.data:
                serializer = reviewSerializer(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    review = serializer.save()
                    user = review.reviewer
                    print("---------------",user)
                    creater = User.objects.get(name=user)   
                    print(creater)
                    
        response = {
            "status": "success",
        }
        return Response(response, status=status.HTTP_200_OK)
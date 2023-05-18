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
                    # review = serializer.save()
                    # print("------------------------------",request.data)
                    a = (request.data)['reviewer']
                    b = (request.data)['agreement']
                    print("------------",a, b)
                    # user = review#.reviewer
                    # print(user)
                    # agr = review.agreement


                    queryset = Agreement.objects.filter(pk = b).values_list('creator', flat=True)
                    creater_pk = queryset[0]
                    # print("creater_pk----->>",creater_pk)
                    creater_name = User.objects.filter(pk = creater_pk).values_list('name', flat=True)
                    # print("creater_name----->>",creater_name)
                    name = creater_name[0]
                    # print(name)
                    reviwer = User.objects.get(pk=a)   
                    # print("reviwer----->>",reviwer)
                    if str(name) == str(reviwer):
                        print("---------------------")
                        response = {
                            "status": "creater and reviewer can not be same",
                        
                        }
                        return Response(response, status=status.HTTP_400_BAD_REQUEST)

                    else:
                        serializer.save()
        response = {
            "status": "success",
        }
        return Response(response, status=status.HTTP_200_OK)
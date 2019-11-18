from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.http import HttpResponse
from django.views import View
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from .models import myclients

from.serializer import addclientSerializer

from.serializer import clientserializer

from rest_framework.parsers import JSONParser

class addclient(GenericViewSet):



    @action(methods=['post'],detail=False)
    def post(self,request):
        try:
            data=request.data
            data=myclients(**data)
            data.save()
            return HttpResponse('Registration succesfull')
        except:
            return HttpResponse('client aredy exist')


    
    @action(methods=['post'], detail=False)
    def Reg_client(self,request):
        serialized = addclientSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data,)
        else:
            return Response(serialized._errors,)



    @action(methods=['get'], detail=False)
    def listclient(self,request):
        client1=myclients.objects.all()
        serializer=clientserializer(client1,many=True)
        return Response(serializer.data)



    @action(methods=['get'],detail=False)
    def getclient(self,request):
        client_id=request.GET["client_id"]
        client1=myclients.objects.get(client_id = client_id)
        serializer=clientserializer(client1)
        return Response(serializer.data)

    

    @action(methods=['put'],detail=False)
    def putclient(self,request):
        try:
            data=request.data
            client_id=data['client_id']
            client_obj=myclients.objects.get(client_id=client_id)
            serializer = addclientSerializer(client_obj,data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except:
            return Response({"status":"Bad request"})










    
    
"""docstring for addclient"f __init__(self, arg):
        super(addclient,.__init__()
        self.arg = arg"""
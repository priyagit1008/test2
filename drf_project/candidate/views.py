from django.shortcuts import render

# Create your views here.



# django imports
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views import View

# rest_framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from.serializer import addcandidateserializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser

# database imports
from.models import mycandidates


class addcandidate(GenericViewSet):

	@action(methods=['post'],detail=False)
	def postcandidate(self,request):
		serialized=addcandidateserializer(data=request.data)
		if serialized.is_valid():
			serialized.save()
			return Response(serialized.data,)
		else:
			return Response(serialized._errors,)

	@action(methods=['get'], detail=False)
	def listcandidate(self,request):
		candidate_object=mycandidates.objects.all()
		serializer=addcandidateserializer(candidate_object,many=True)
		return Response(serializer.data)

	
	@action(methods=['get'],detail=False)
	def getcandidate(self,request):
		candidate_id=request.GET["candidate_id"]
		candidate_object=mycandidates.objects.get(candidate_id = candidate_id)
		serializer=addcandidateserializer(candidate_object)
		return Response(serializer.data)

		

	@action(methods=['put'],detail=False)
	def putcandidate(self,request):
		try:
			data=request.data
			candidate_id=data['candidate_id']
			candidate_object=mycandidates.objects.get(candidate_id=candidate_id)
			serializer = addcandidateserializer(candidate_object,data=data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			else:
				return Response(serializer.errors)
		except:
			return Response({"status":"Bad request"})

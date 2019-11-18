# Create your views here.
from django.http import HttpResponse
from django.views import View


from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from.serializer import managerserializer



# from.rest_framework import adduserSerializer

from.serializer import adduserSerializer
# from.serializer import updateuserserilizer
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action

from .models import manager_table

from rest_framework.parsers import JSONParser



class GreetingView(View):
	greeting = "Good Day"

	def get(self, request):
		return HttpResponse(self.greeting)

	def post(self, request):
		print (request.POST)
		email = request.POST["email"]
		password = request.POST["password"]
		manager_table(email = email)
		return HttpResponse(self.greeting)

class managerlist(GenericViewSet):


	@action(methods=['post'], detail=False)
	def createuser(self,request):
		serialized = adduserSerializer(data=request.data)
		if serialized.is_valid():
			# print (serialized)
			serialized.save()
			print ("sdf")
			return Response(serialized.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


	@action(methods=['get'], detail=False)
	def listuser(self,request):
		manager_table1=manager_table.objects.all()
		serializer=managerserializer(manager_table1,many=True)
		return Response(serializer.data)



	@action(methods=['get'], detail=False)
	def getuser(self,request):
		manager_table_id = request.GET["manager_table_id"]
		manager_table1=manager_table.objects.get(manager_table_id = manager_table_id)
		serializer=managerserializer(manager_table1)
		return Response(serializer.data)



	@action(methods=['put'],detail=False)
	def putuser(self,request):
		# data = JSONParser().parse(request)
		try:
			data=request.data
			# print(data)
			# manager_table_id=data.manager_table_id
			manager_table_onject=manager_table.objects.get(manager_table_id=manager_table_id)
			serializer = adduserSerializer(manager_table_onject,data=data)
			if serializer.is_valid():
				print(serializer.errors)
				serializer.save()
				return Response(serializer.data,status=status.HTTP_201_CREATED)
			else:
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			print(str(e))
			return Response("bad request")
   
	








































  #     manager_table.objects.create_user(
		#     serialized.init_data['Name'],
		#     serialized.init_data['email'],
		#     serialized.init_data['password'],
		#     serialized.init_data['mobile'],
		#     serialized.init_data['address'],
		# )





	# @action(methods=['post'], detail=False)
	# def postuser(self,request):
	#     manager_table1=manager_table.objects.all()
	#     serializer=adduserSerializer(manager_table1,many=True)
	#     return Response(serializer.data)

















		# class GreetingView(View):
#   greeting = "Good Day"

#   def get(self, request):
#       return HttpResponse(self.greeting)

# class MyView(View):
#   def get(self, request):
#       # <view logic>
#       return HttpResponse('hi python')


# def my_view(request):
#   if request.method == 'GET':
#       # <view logic>
#       return HttpResponse('result')

# class manager_table2(View):
#   feedback = "successful registered"

	
			# data = manager_table(Name=Name,email=email,password=password,mobile=mobile,address=address)
			# data.save()
			# return HttpResponse('Registration succesfull')
		# except:
		#   return HttpResponse('not registared')
 

# class login(View):

#   def get(self,request):
#       try:
#           print(request.POST)
#           email=request.POST["email"]
#           password=request.POST["password"]
#           data=manager_table.objects.get(email=email,password=password)
#           return HttpResponse('succesfull loged in')
#       except:
#           return HttpResponse('not loged in')


# class manager_tablelist(APIView):



#   def post(self,request):
#       try:
#           # print(request.POST)
#           # Name=request.POST["Name"]
#           # email=request.POST["email"]
#           # password=request.POST["password"]
#           # mobile=request.POST["mobile"]
#           # address=request.POST["address"]
#           data = request.data
#           data = manager_table(**data)
#           data.save()
#           return HttpResponse('Registration succesfull')
			
#       except:

#           return HttpResponse('user alredy exist')

#   def get(self,request):
#       manager_table1=manager_table.objects.all()
#       serializer=managerserializer(manager_table1,many=True)
#       return Response(serializer.data)

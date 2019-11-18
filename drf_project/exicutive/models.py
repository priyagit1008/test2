from django.db import models

import uuid
from libs.models import DefaultModels

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser




# App Level Import 
from .usermanager import usermanager

# Create your models here.

class manager_table(AbstractBaseUser):
	manager_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	Name=models.CharField(max_length=20)
	email=models.EmailField(unique=True,max_length=50)
	password=models.CharField(max_length=8)
	mobile=models.CharField(max_length=10)
	address=models.CharField(max_length=20)
	# is_active = models.BooleanField(default=True)
	# create_at = models.DateTimeField(auto_now_add=True)
	# updated_at= models.DateTimeField(auto_now = True)   
	object = usermanager()

	USERNAME_FIELD = 'email'    
	REQUIRED_FIELDS = []

   
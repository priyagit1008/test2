from django.db import models
import uuid
# import uuid
# Create your models here.
from libs.models import DefaultModels
# from datetime import datetime
# import datetime
# from django.utils.timezone import now


class myclients(models.Model):
    client_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client_name=models.CharField(max_length=20)
    contact_email=models.EmailField(unique=True,max_length=50)
    number=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    # is_active = models.BooleanField(default=True)
    # create_at = models.DateTimeField(auto_now_add=True)
    # updated_at= models.DateTimeField(auto_now = True) 
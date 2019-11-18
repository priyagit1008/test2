from django.db import models
import uuid
# import datetime
# from django.utils.timezone import now


# Project Level Imports
from libs.models import DefaultModels


class mycandidates(DefaultModels):
	candidate_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	Name=models.CharField(max_length=50)
	email=models.EmailField(max_length=20)
	number=models.IntegerField()
	address=models.CharField(max_length=50)
	# is_active = models.BooleanField(default=True)
	current_ctc=models.IntegerField()
	expected_ctc=models.IntegerField()
	notice_days=models.IntegerField()
	is_alredy_on_notice=models.BooleanField()
	tech_skills=models.CharField(max_length=20)
	preferable_location=models.CharField(max_length=20)
	# create_at = models.DateTimeField(auto_now_add=True)
	# updated_at= models.DateTimeField(auto_now = True)



	
   
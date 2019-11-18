from django.db import models

# Create your models here.
class DefaultModels(models.Model):
	
	is_active = models.BooleanField(default=True)

	create_at = models.DateTimeField(auto_now_add=True)

	updated_at = models.DateTimeField(auto_now = True)

	class Meta:
		abstract = True
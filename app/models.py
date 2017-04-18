from django.db import models
import datetime
#from datetime import datetime
from django.utils import timezone

class GenericData (models.Model):
	pubdate = models.DateTimeField(auto_now_add=True)
	jsondata = models.CharField(max_length=500)

	def recent_published(self):
		now = timezone.now()
		return now - datetime.timedelta(minutes=2) <= self.pubdate <= now
		recent_published.admin_order_field = 'pubdate'
		recent_published.boolean = True
		recent_published.short_description = 'Recent Data'
#a new model for each data snapshot can be created
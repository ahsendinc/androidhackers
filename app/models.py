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
class Data (models.Model):
	pubdate = models.DateTimeField(auto_now_add=True)
	# battery_status = models.IntegerField()
	# battery_health = models.IntegerField()
	# battery_level = models.IntegerField()
	# battery_temperature = models.IntegerField()
	# cpu_total = models.IntegerField()
	# cpu_load1
	# cpu_load2
	# cpu_load3
	# cpu_app1
	# cpu_app2
	# cpu_app3
	# meminfo_totalRAM
	# meminfo_total_freeRAM
	# meminfo_total_usedRAM

class BatteryStatus(models.Model):
	time = models.DateTimeField()
	value = models.CharField(max_length=500)

class BatteryHealth(models.Model):
	time = models.DateTimeField()
	value = models.CharField(max_length=500)

class BatteryLevel(models.Model):
	time = models.DateTimeField()
	value = models.IntegerField()

class BatteryTemperature(models.Model):
	time = models.DateTimeField()
	value = models.IntegerField()
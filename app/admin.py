from django.contrib import admin
from .models import GenericData, TestInfo, BatteryStatus, BatteryHealth, BatteryLevel, BatteryTemperature, CPUUser, CPUTotal, CPULoad1, CPULoad2, CPULoad3, CPUHog1New, CPUHog2New , CPUHog3New, CPUHog4New, CPUHog5New, MemInfoTotalRam, MemInfoFreeRam, MemInfoUsedRam
# Register your models here.

class GenericDataAdmin (admin.ModelAdmin):
	list_display = ('pubdate', 'jsondata', 'recent_published')
	list_filter = ['pubdate']
	search_fields = ['pubdate']

class TestInfoAdmin (admin.ModelAdmin):
	list_display = ('idnum', 'name', 'status', 'message')
	list_filter = ['name','status']
	search_fields = ['name','idnum','status']

class BatteryStatusAdmin (admin.ModelAdmin):
	list_display = ('time', 'value')
	list_filter = ['value']
	search_fields = ['value']

class BatteryHealthAdmin (admin.ModelAdmin):
	list_display = ('time', 'value')
	list_filter = ['value']
	search_fields = ['value']

class BatteryTemperatureAdmin (admin.ModelAdmin):
	list_display = ('time', 'value')
	list_filter = ['value']
	search_fields = ['value']

class BatteryLevelAdmin (admin.ModelAdmin):
	list_display = ('time', 'value')
	list_filter = ['value']
	search_fields = ['value']

class CPUUserAdmin (admin.ModelAdmin):
	list_display = ('time', 'value')
	list_filter = ['value']
	search_fields = ['value']

class CPUTotalAdmin (admin.ModelAdmin):
	list_display = ('time', 'value')
	list_filter = ['value']
	search_fields = ['value']

class CPULoad1Admin (admin.ModelAdmin):
	list_display = ('time', 'value')
	list_filter = ['value']
	search_fields = ['value']

class CPULoad2Admin (admin.ModelAdmin):
	list_display = ('time', 'value')
	list_filter = ['value']
	search_fields = ['value']

class CPULoad3Admin (admin.ModelAdmin):
	list_display = ('time', 'value')
	list_filter = ['value']
	search_fields = ['value']

class MemInfoTotalRamAdmin (admin.ModelAdmin):
	list_display = ('time', 'value')
	list_filter = ['value']
	search_fields = ['value']

class MemInfoFreeRamAdmin (admin.ModelAdmin):
	list_display = ('time', 'value')
	list_filter = ['value']
	search_fields = ['value']

class MemInfoUsedRamAdmin (admin.ModelAdmin):
	list_display = ('time', 'value')
	list_filter = ['value']
	search_fields = ['value']

class CPUHog1Admin (admin.ModelAdmin):
	list_display = ('time', 'value','name')
	list_filter = ['value','name']
	search_fields = ['value','name']

class CPUHog2Admin (admin.ModelAdmin):
	list_display = ('time', 'value','name')
	list_filter = ['value','name']
	search_fields = ['value','name']

class CPUHog3Admin (admin.ModelAdmin):
	list_display = ('time', 'value','name')
	list_filter = ['value','name']
	search_fields = ['value','name']

class CPUHog4Admin (admin.ModelAdmin):
	list_display = ('time', 'value','name')
	list_filter = ['value','name']
	search_fields = ['value','name']

class CPUHog5Admin (admin.ModelAdmin):
	list_display = ('time', 'value','name')
	list_filter = ['value','name']
	search_fields = ['value','name']


admin.site.register(TestInfo, TestInfoAdmin)
admin.site.register(BatteryStatus, BatteryStatusAdmin)
admin.site.register(BatteryHealth, BatteryHealthAdmin)
admin.site.register(BatteryLevel, BatteryLevelAdmin)
admin.site.register(BatteryTemperature, BatteryTemperatureAdmin)
admin.site.register(CPUTotal, CPUTotalAdmin)
admin.site.register(CPUUser, CPUUserAdmin)
admin.site.register(CPULoad1, CPULoad1Admin)
admin.site.register(CPULoad2, CPULoad2Admin)
admin.site.register(CPULoad3, CPULoad3Admin)
admin.site.register(CPUHog1New, CPUHog1Admin)
admin.site.register(CPUHog2New, CPUHog2Admin)
admin.site.register(CPUHog3New, CPUHog3Admin)
admin.site.register(CPUHog4New, CPUHog4Admin)
admin.site.register(CPUHog5New, CPUHog5Admin)
admin.site.register(MemInfoUsedRam, MemInfoUsedRamAdmin)
admin.site.register(MemInfoFreeRam, MemInfoFreeRamAdmin)
admin.site.register(MemInfoTotalRam, MemInfoTotalRamAdmin)




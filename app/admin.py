from django.contrib import admin
from .models import GenericData, TestInfo
# Register your models here.

class GenericDataAdmin (admin.ModelAdmin):
	list_display = ('pubdate', 'jsondata', 'recent_published')
	list_filter = ['pubdate']
	search_fields = ['pubdate']

class TestInfoAdmin (admin.ModelAdmin):
	list_display = ('idnum', 'name', 'status', 'message')
	list_filter = ['name','status']
	search_fields = ['name','idnum','status']
admin.site.register(TestInfo, TestInfoAdmin)
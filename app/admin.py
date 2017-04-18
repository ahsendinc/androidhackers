from django.contrib import admin
from .models import GenericData
# Register your models here.

class GenericDataAdmin (admin.ModelAdmin):
	list_display = ('pubdate', 'jsondata', 'recent_published')
	list_filter = ['pubdate']
	search_fields = ['pubdate']

admin.site.register(GenericData, GenericDataAdmin)
from django.contrib import admin

from .models import *

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
	list_display = ('id', 'price', 'price_type', 'active')
	search_list = ['id', 'price', 'price_type']

@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
	list_display = ('id', 'serie', 'consecutive', 'active')
	search_list = ['id', 'serie', 'consecutive']

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'business_name', 'city', 'town')
	search_list = ['id', 'name', 'city', 'town']

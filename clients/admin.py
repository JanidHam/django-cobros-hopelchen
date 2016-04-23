from django.contrib import admin

from .models import *

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'lastname', 'curp', 'rfc', 'town', 'created')
	search_fields = ['id', 'name', 'lastname', 'curp', 'town']

@admin.register(Paid)
class PaidAdmin(admin.ModelAdmin):
	list_display = ('id', 'client', 'total', 'created', 'canceled')
	search_fields = ['id', 'client__name', 'client__lastname', 'total', 'created']

@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):
	list_display = ('id', 'client', 'total', 'paid_date')
	search_fields = ['id', 'client__name', 'client__lastname', 'total', 'paid_date']


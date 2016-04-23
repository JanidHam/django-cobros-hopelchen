# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from users.models import UserProfile

from cobros.helpers.statics import CITIES, TOWNS

class Client(models.Model):
	name = models.CharField(max_length=80, verbose_name='Nombre')
	lastname = models.CharField(max_length=80, verbose_name='Apellidos')
	curp = models.CharField(max_length=17, verbose_name='CURP')
	rfc = models.CharField(max_length=17, verbose_name='RFC')
	address = models.CharField(max_length=150, verbose_name='Dirección')
	zip_code = models.IntegerField(verbose_name='Código Postal')
	city = models.IntegerField(verbose_name='Ciudad', choices=CITIES)
	town = models.IntegerField(verbose_name='Municipio', choices=TOWNS)
	created_by = models.ForeignKey(UserProfile, verbose_name='Creado por')
	deleted = models.BooleanField(verbose_name='Activo', default=False)
	created = models.DateTimeField(auto_now=True, verbose_name='Creado')
	updated = models.DateTimeField(auto_now_add=True, verbose_name='Actualizado')
	

	def __str__(self):
		return "{} {}".format(self.name, self.lastname)

class Paid(models.Model):
	client = models.ForeignKey(Client, verbose_name='Cliente', related_name='paid_client')
	consecutive = models.IntegerField(verbose_name='Consecutivo de folio')
	folio = models.CharField(max_length=50, verbose_name='Folio del pago')
	paid_month = models.IntegerField(verbose_name='Mes del pago')
	paid_year = models.IntegerField(verbose_name='Año del pago')
	amount = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Importe de pago')
	tax = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='IVA')
	total = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Total')
	partial = models.BooleanField(verbose_name='Pago parcial', default=False)
	canceled = models.BooleanField(verbose_name='Activo', default=False)
	created = models.DateTimeField(auto_now=True, verbose_name='Creado')
	updated = models.DateTimeField(auto_now_add=True, verbose_name='Actualizado')

	def __str__(self):
		return "{} - {}".format(self.client.name, self.folio)

class Debt(models.Model):
	client = models.ForeignKey(Client, verbose_name='Cliente', related_name='debt_client')
	amount = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Importe de pago')
	tax = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='IVA')
	total = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Total')
	debt_month = models.IntegerField(verbose_name='Mes que se adeuda')
	debt_year = models.IntegerField(verbose_name='Año de la deuda')
	paid_date = models.DateTimeField(null=True, blank=True, verbose_name='Día que se paga la deuda')
	deleted = models.BooleanField(verbose_name='Activo', default=False)
	created = models.DateTimeField(auto_now=True, verbose_name='Creado')
	updated = models.DateTimeField(auto_now_add=True, verbose_name='Actualizado')

	def __str__(self):
		return "{}".format(self.client.name)





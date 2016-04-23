# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from cobros.helpers.statics import PRICE_TYPE, CITIES, TOWNS

class Price(models.Model):
	price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Precio')
	price_type = models.IntegerField(verbose_name='Tipo precio', choices=PRICE_TYPE)
	active = models.BooleanField(verbose_name='Activo', default=True)
	created = models.DateTimeField(auto_now=True, verbose_name='Creado')
	updated = models.DateTimeField(auto_now_add=True, verbose_name='Actualizado')


class Serie(models.Model):
	serie = models.CharField(max_length=10, verbose_name='Serie')
	consecutive = models.IntegerField(verbose_name='Consecutivo')
	active = models.BooleanField(default=True, verbose_name='Activo')
	created = models.DateTimeField(auto_now=True, verbose_name='Creado')
	updated = models.DateTimeField(auto_now_add=True, verbose_name='Actualizado')	

class Company(models.Model):
	name = models.CharField(max_length=80, verbose_name='Nombre')
	business_name = models.CharField(max_length=80, verbose_name='Razón Social')
	rfc = models.CharField(max_length=17, verbose_name='RFC')
	address = models.CharField(max_length=255, verbose_name='Dirección')
	zip_code = models.IntegerField(verbose_name='Código Postal')
	city = models.IntegerField(verbose_name='Ciudad', choices=CITIES)
	town = models.IntegerField(verbose_name='Municipio', choices=TOWNS)

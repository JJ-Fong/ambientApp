from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.db import models
from django import forms
# Create your models here.

# Create your models here.
class UserFields(models.Model):
	alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

	username = models.CharField(max_length = 120)
	password = models.CharField(max_length=12, blank=True, null=True, validators=[alphanumeric])
	email = models.EmailField(max_length=120)	

	#MUESTRA EL TITULO EN LA TABLA DEL APP ADMIN
	def __unicode__(self):
		return self.username

class UserFieldsTest5(models.Model):
	alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

	username = models.CharField(max_length = 120)
	password = models.CharField(max_length=12, validators=[alphanumeric])
	email = models.EmailField(max_length=120, blank=True, null=True)	

	#MUESTRA EL TITULO EN LA TABLA DEL APP ADMIN
	def __unicode__(self):
		return self.username	

class HDCFields(models.Model):
	zona = models.IntegerField()
	personasxcasa = models.IntegerField()
	tiempoxbano = models.IntegerField()
	apagarluz = models.IntegerField()
	vehiculosxcasa = models.IntegerField()
	transporte = models.IntegerField()
	frutasyverduras = models.IntegerField()
	comidarapida = models.IntegerField()
	comidaenlatada = models.IntegerField()
	bolsasplasticas = models.IntegerField()
	hojas2uso = models.IntegerField()

	


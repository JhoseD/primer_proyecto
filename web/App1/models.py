# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Cliente (models.Model):
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	direccion = models.CharField(max_length=50)
	telefono = models.CharField(max_length=8)
	 
 	def __unicode__(self):
		return self.nombre
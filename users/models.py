from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, Group

class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name='user_profile')
	#foto_perfil = models.ImageField(upload_to='userprofiles/imagesProfiles', verbose_name='Foto Perfil', blank=True)
	
	def __str__(self):
		return self.user.username
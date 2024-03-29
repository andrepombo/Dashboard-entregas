from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import Cliente

def customer_profile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='cliente')
		instance.groups.add(group)
		Cliente.objects.create(
			user=instance,
			nome=instance.username,
			)
		print('Profile created!')

post_save.connect(customer_profile, sender=User)
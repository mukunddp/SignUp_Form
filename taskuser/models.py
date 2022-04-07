from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    avatar = models.ImageField(upload_to='student_profile/', null=True, blank=True)

    def __str__(self):
        return self.user.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    CHOICES = (('Doctor', 'Doctor'), ('Patient', 'Patient'),)
    user_type = models.CharField(null=True, max_length=20, choices=CHOICES)
    address_line1 = models.CharField(null=True, max_length=200)
    city = models.CharField(null=True, max_length=50)
    state = models.CharField(null=True, max_length=50)
    pincode = models.IntegerField(null=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
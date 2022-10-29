from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    content = models.TextField(max_length=500)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f"{self.name}' profile"


@receiver(post_save, sender=User)
def created_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

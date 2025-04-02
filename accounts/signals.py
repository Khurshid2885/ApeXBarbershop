from django.contrib.auth.models import Group
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

from accounts.models import CustomUser, BarberProfile
from accounts.service import send_congratulations_email



# @receiver(post_save, sender=CustomUser)
# def send_welcome_email(sender, instance, created, **kwargs):
#     if created:
#         send_congratulations_email(
#             receiver_email=instance.email,
#             first_name=instance.first_name,
#         )


@receiver(m2m_changed, sender=CustomUser.groups.through)
def auto_create_barber_profile(sender, instance, action, pk_set, **kwargs):
    if action == "post_add":
        barber_group = Group.objects.get(name="barber")
        if barber_group.id in pk_set:  # Check if the barber group is in the added groups
            BarberProfile.objects.get_or_create(user=instance)

from django.db.models.signals import post_save,pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from . models import Profile,Relationship

@receiver(post_save,sender=User)
def post_save_created_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=Relationship)
def post_save_created_relationship(sender,instance,created,**kwargs):
    sender_=instance.sender
    receiver_=instance.reciever
    if instance.state == 'accepted':
        sender_.friends.add(receiver_.user)
        receiver_.friends.add(sender_.user)
        sender_.save()
        receiver_.save()

@receiver(pre_delete,sender=Relationship)
def pre_delete_remove_friend(sender,instance,**kwargs):
    sender_=instance.sender
    receiver_=instance.reciever
    sender_.friends.remove(receiver_.user)
    receiver_.friends.remove(sender_.user)
    sender_.save()
    receiver_.save()


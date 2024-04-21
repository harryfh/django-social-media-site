from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
            "self",
            related_name="followed_by",
            symmetrical=False,
            blank=True
        )
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User) # Signal to create a profile when a user is created
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.profile) # Foloow yourself
        user_profile.save()

class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="blogs")
    title = models.CharField(max_length=50)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    
    @property
    def description(self):
        return self.content[:100]


    def __str__(self):
        return self.title
    

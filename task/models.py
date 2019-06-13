from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from task_creator.utils import get_dot_env

# Create your models here.
class Task(models.Model):
    """Tasks Model"""

    title = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


@receiver(post_save, sender=Task)
def task_post_save(sender, instance, **kwargs):
    """Send mail to task.user with task detials post save"""
    send_mail(
        subject=instance.title,
        message=f"""
    description: {instance.description}
    due date: {instance.due_date}
    """,
        from_email=settings.FROM_EMAIL,
        recipient_list=[instance.user.email],
        fail_silently=True,
    )

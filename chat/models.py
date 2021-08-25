from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class Message(models.Model):
    author = models.ForeignKey(CustomUser, related_name='message', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact.user.username

    def last_10_messages(self):
        return Message.objects.order_by('-timestamp').all()[:10]
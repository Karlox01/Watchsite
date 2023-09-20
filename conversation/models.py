from django.contrib.auth.models import User
from django.db import models

from watches.models import Item

class Conversation(models.Model):
    item = models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)

    def __str__(self):
        return f'Conversation about {self.item.name}'

class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)
    is_offer = models.BooleanField(default=False)

    def __str__(self):
        return self.content[:50]
    
    MESSAGE_TYPE_CHOICES = [
        ('message', 'Message'),
        ('offer', 'Offer'),
    ]
    
    message_type = models.CharField(max_length=7, choices=MESSAGE_TYPE_CHOICES, default='message')
    
    @classmethod
    def create_offer(cls, conversation, content, created_by):
        return cls.objects.create(
            conversation=conversation,
            content=content,
            created_by=created_by,
            message_type='offer'  # Set the message type to 'offer'
        )














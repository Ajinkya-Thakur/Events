from django.db import models
from django.contrib.auth.models import User
import uuid

class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='members'
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE, 
        related_name='members'
    )
    amount_pledged = models.PositiveIntegerField(default=0)
    balance_amount = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'event')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.balance_amount = self.amount_pledged
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.event.name}"
  

class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    heading = models.CharField(max_length=200)
    expense = models.PositiveIntegerField()
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='transactions'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.heading} - {self.event.name}"

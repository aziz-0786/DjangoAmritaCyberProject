from django.db import models
from django.utils import timezone

class EvaluationRequest(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("completed", "Completed"),
    ]

    input_prompt = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    result = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
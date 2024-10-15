from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = (
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    )
    STATUS_CHOICES = (
        ('P', 'Pending'),
        ('C', 'Completed'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    priority_level = models.CharField(max_length=1, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    completion_timestamp = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.status == 'C' and self.completion_timestamp is None:
            self.completion_timestamp = timezone.now()
        elif self.status == 'P':
            self.completion_timestamp = None
        super().save(*args, **kwargs)

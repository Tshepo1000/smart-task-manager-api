from django.db import models

# Create your models here.
class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    RECURRENCE_CHOICES = [
        ('none', 'None'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='medium')
    recurrence = models.CharField(max_length=7, choices=RECURRENCE_CHOICES, default='none')

    def __str__(self):
        return self.title

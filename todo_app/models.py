from django.db import models
# Create your models here.

class Task(models.Model):
    PRIORITY = [
        (0, "Null"),
        (1, "High"),
        (2, "Medium"),
        (3, "Low")
    ]
    COMPLETION_CHOICES = [
        (True, "Completed"),
        (False, "Incomplete")
    ]

    title = models.CharField(max_length=50)
    description = models.TextField()
    priority = models.IntegerField(choices=PRIORITY, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(choices=COMPLETION_CHOICES, default=False)
    is_delete = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):

        return f'{self.title}'

    class Meta:
        verbose_name = 'Task'

from django.db import models

# Create your models here.
from django.utils import timezone

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100, blank=True)
    image_url = models.URLField(blank=True)
    date_generated = models.DateField(default=timezone.now)
    theme = models.CharField(max_length=50, blank=True)  # E.g., "motivation", "focus"
    
    def __str__(self):
        return f"{self.text} - {self.author} (Generated on {self.date_generated})"

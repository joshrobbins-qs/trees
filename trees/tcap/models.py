from django.db import models

# Create your models here.
class TerroristGroup(models.Model):
    """Database of content-sharing groups - e.g. Taliban."""

    # Name of the group
    name = models.CharField(max_length=255)

    # Description of group
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.name}"
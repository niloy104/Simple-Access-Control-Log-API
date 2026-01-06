from django.db import models

# Create your models here.
class AccessLog(models.Model):
    card_id = models.CharField(max_length=20)
    door_name = models.CharField(max_length=50)
    access_granted = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.card_id} - {self.door_name} - {'GRANTED' if self.access_granted else 'DENIED'}"

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import AccessLog
from datetime import datetime
import os

# Absolute path for log file inside the app
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, 'system_events.log')

@receiver(post_save, sender=AccessLog)
def log_creation(sender, instance, created, **kwargs):
    if created:
        line = f"[{datetime.now()}] - CREATE: Access log created for card {instance.card_id}. Status: {'GRANTED' if instance.access_granted else 'DENIED'}\n"
        with open(LOG_FILE, 'a') as f:
            f.write(line)

@receiver(post_delete, sender=AccessLog)
def log_deletion(sender, instance, **kwargs):
    line = f"[{datetime.now()}] - DELETE: Access log (ID: {instance.id}) for card {instance.card_id} was deleted.\n"
    with open(LOG_FILE, 'a') as f:
        f.write(line)

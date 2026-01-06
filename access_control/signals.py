from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import AccessLog
from datetime import datetime
import os
import subprocess

# Absolute path for log file inside the app
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, 'system_events.log')

def append_to_log(line: str):
    """
    Use subprocess to append a line to the log file.
    """
    # The shell command: echo "line" >> log_file
    subprocess.run(f'echo "{line.strip()}" >> "{LOG_FILE}"', shell=True)

@receiver(post_save, sender=AccessLog)
def log_creation(sender, instance, created, **kwargs):
    if created:
        line = f"[{datetime.now()}] - CREATE: Access log created for card {instance.card_id}. Status: {'GRANTED' if instance.access_granted else 'DENIED'}"
        append_to_log(line)

@receiver(post_delete, sender=AccessLog)
def log_deletion(sender, instance, **kwargs):
    line = f"[{datetime.now()}] - DELETE: Access log (ID: {instance.id}) for card {instance.card_id} was deleted."
    append_to_log(line)

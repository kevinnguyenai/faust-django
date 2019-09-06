from django.db.models import signals
from django.dispatch import receiver
from .models import Account
import asyncio
import logging
logger = logging.getLogger(__name__)


@receiver(signals.post_save, sender=Account)
def create_event_accounts(sender, instance, created, **kwargs):
    if created:
        logger.warn('123')


@receiver(signals.post_save, sender=Account)
def save_event_accounts(sender, instance, **kwargs):
    logger.warn('345')

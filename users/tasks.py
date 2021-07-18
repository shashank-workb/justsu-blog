from celery import shared_task
from celery.utils.log import get_task_logger

from .models import Location
from .utils import weather, update_location_weather

logger = get_task_logger(__name__)

@shared_task
def update_weather_data():
    """
    updates the weather of all city models
    """
    All_locations = Location.objects.all()
    for location in All_locations:
        update_location_weather(location)
        logger.info(f'{location.city} updated')

    
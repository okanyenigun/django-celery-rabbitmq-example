from celery import shared_task
from celery.utils.log import get_task_logger
from myapp2.domain import real_job_doer

logger = get_task_logger(__name__)

@shared_task(name="create_json_task")
def create_json_task(name, message):
    logger.info("Sent message")
    return real_job_doer(name, message)
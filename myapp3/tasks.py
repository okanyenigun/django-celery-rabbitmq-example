from __future__ import absolute_import, unicode_literals
import os
from celery import shared_task
from datetime import datetime
from django.conf import settings

@shared_task
def write_to_txt(val1, val2):
    path = os.path.join(settings.STATICFILES_DIRS[0],"sample.txt")
    with open(path, 'a') as f:
        text = f"Result: {val1+val2} @ {datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}\n"
        f.write(text)
        f.close()
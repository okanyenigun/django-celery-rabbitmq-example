from __future__ import absolute_import, unicode_literals

from celery import shared_task

@shared_task(name="foo")
def foo(x,y):
    return x * y
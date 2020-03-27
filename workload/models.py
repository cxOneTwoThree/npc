import datetime

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Worker(models.Model):
    fullname = models.CharField(_('Fullname'), max_length=100)
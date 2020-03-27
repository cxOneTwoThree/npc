from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class WorkloadConfig(AppConfig):
    name = 'workload'
    class Meta:
        verbose_name = _('Workload')
        verbose_name_plural = _('Workload')

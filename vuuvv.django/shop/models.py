from django.db import models
from django.utils.translation import ugettext_lazy as _

class Shop(models.Model):
    site = models.ForeignKey(Site, related_name='shops', verbose_name='Site')
    name = models.CharField(_('Name'), max_length=100)


from django.core.urlresolvers import reverse
from django.contrib.auth.models import  User
from django.utils.translation import ugettext_lazy as _
from django.db import models

from groups_ng.base import Group

class BasicGroup(Group):
    members = models.ManyToManyField(User, verbose_name=_('members'))

    def get_absolute_url(self):
        return reverse('group_detail', args=[self.slug])
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

__all__ = ['Account']


class Account(AbstractUser):
    followers = models.ManyToManyField(
        to='self',
        related_name='followed',
        blank=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')

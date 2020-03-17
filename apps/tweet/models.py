from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

__all__ = ['Tweet']


class Tweet(models.Model):
    text = models.CharField(max_length=255, verbose_name=_('text'))
    sender = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tweets')

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = _('tweet')
        verbose_name_plural = _('tweets')


class ReTweet(models.Model):
    tweet = models.ForeignKey(to=Tweet, on_delete=models.CASCADE, related_name='retweets')
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='retweets')

    def __str__(self):
        return f'{self.user_id}'

    class Meta:
        verbose_name = _('retweet')
        verbose_name_plural = ('retweets')


class Favorite(models.Model):
    tweet = models.ForeignKey(to=Tweet, on_delete=models.CASCADE, related_name='favorites')
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorites')

    def __str__(self):
        return f'{self.user_id}'

    class Meta:
        verbose_name = _('favorite')
        verbose_name_plural = _('favorites')

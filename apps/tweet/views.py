from django.http import JsonResponse
from django.views import View
from django.db.models import Avg, Count

from apps.account.models import Account

__all__ = ['AverageNumberOfTweetsPerUser']


class AverageNumberOfTweetsPerUser(View):
    def get(self, request):
        results = Account.objects.annotate(tweets_per_user=Count('tweets'))\
            .only('tweets_per_user')\
            .aggregate(average_number=Avg('tweets_per_user'))

        average_number = results.get('average_number')
        return JsonResponse({'average_number':  0 if average_number is None else average_number}, safe=False)

from django.http import JsonResponse
from django.views import View
from django.db.models import Avg, Count

from apps.account.models import Account

__all__ = ['NumberOfUsersWithoutAnyFollowersView', 'AverageNumberOfFollowersPerUserView']


class NumberOfUsersWithoutAnyFollowersView(View):
    def get(self, request):
        the_number = Account.objects.filter(followers=None).count()
        return JsonResponse({'number': the_number}, safe=False)


class AverageNumberOfFollowersPerUserView(View):
    def get(self, request):
        result = Account.objects \
            .annotate(followers_count=Count('followers')) \
            .aggregate(average_number=Avg('followers_count'))
        average_number = result.get('average_number')
        return JsonResponse(
            {'average_number': 0 if average_number is None else average_number},
            safe=False)

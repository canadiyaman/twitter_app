from django.test import TestCase
from django.urls import reverse

from apps.account.models import Account


class TestViewsTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        for i in range(10):
            Account.objects.create(
                username=f'user_{i}',
                email=f'user_{i}@test.com'
            )

    def test_number_of_user_without_any_followers(self):
        response = self.client.get(reverse('account:number_of_user_without_any_followers'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('number'), 10)

        someone = Account.objects.first()
        another_one = Account.objects.last()
        someone.followers.add(another_one)

        response = self.client.get(reverse('account:number_of_user_without_any_followers'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('number'), 8)

    def test_average_number_of_followers_per_user(self):
        response = self.client.get(reverse('account:average_number_of_followers_per_user'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('average_number'), 0)
        someone = Account.objects.first()
        for account in Account.objects.all():
            account.followers.add(someone)

        response = self.client.get(reverse('account:average_number_of_followers_per_user'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('average_number'), 1.9)

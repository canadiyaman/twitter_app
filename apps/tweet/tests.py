from django.test import TestCase
from django.urls import reverse

from apps.account.models import Account
from apps.tweet.models import Tweet


class TestTweetViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        for i in range(10):
            sender = Account.objects.create(
                username=f'user_{i}',
                email=f'user_{i}@test.com'
            )

            Tweet.objects.create(text=f'Example Tweet {i}', sender=sender)

    def test_average_number_of_tweets_per_user(self):
        response = self.client.get(reverse('tweet:average_number_of_tweet_per_user'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('average_number'), 1.0)

        someone = Account.objects.first()
        Tweet.objects.create(sender=someone, text='New Tweet')
        response = self.client.get(reverse('tweet:average_number_of_tweet_per_user'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('average_number'), 1.1)

from django.urls import path

from apps.tweet.views import AverageNumberOfTweetsPerUser

urlpatterns = [
    path(
        'average-number-of-tweet-per-user',
        AverageNumberOfTweetsPerUser.as_view(),
        name='average_number_of_tweet_per_user'
    ),
]

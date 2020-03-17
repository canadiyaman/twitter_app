from django.urls import path

from apps.account.views import NumberOfUsersWithoutAnyFollowersView, AverageNumberOfFollowersPerUserView

urlpatterns = [
    path(
        'number-of-user-without-any-followers',
        NumberOfUsersWithoutAnyFollowersView.as_view(),
        name='number_of_user_without_any_followers'),
    path(
        'average-number-of-followers-per-user',
        AverageNumberOfFollowersPerUserView.as_view(),
        name='average_number_of_followers_per_user'),
]

# Tweetter App


- number of users without any followers
 ```
 curl -X GET http://127.0.0.1:8000/account/number-of-user-without-any-followers
 ```

- average number of tweets per user
 ```
 curl -X GET http://127.0.0.1:8000/tweet/average-number-of-tweet-per-user
 ```
 
- average number of followers per user

 ```
 curl -X GET http://127.0.0.1:8000/account/average-number-of-followers-per-user 
 ```


## For Testing run command below

 ```
    python manage.py test account  tweet
 ```

Created By Can ADIYAMAN


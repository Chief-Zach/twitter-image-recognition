import tweepy
from decouple import config

consumer_key = config("consumer_key")
access_token = config("access_token")
access_token_secret = config("access_token_secret")
consumer_secret = config("consumer_secret")

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)


class InvalidEntry(Exception):
    min_f = 32
    max_f = 212

    def __init__(self, username, user_id, *args):
        super().__init__(args)
        self.username = username
        self.user_id = user_id

    def __str__(self):
        return f'The values:\nDisplay Name: {self.username}\nUser_ID: {self.user_id}\nAre not valid'


def fetch_image(username=None, user_id=None):
    if username is None and user_id is None:
        raise ValueError('Did not provide value for image search')
    elif user_id is not None:
        try:
            user = api.get_user(user_id=user_id)
        except tweepy.errors.NotFound:
            print("USERID")
            raise InvalidEntry(username, user_id)
    elif username is not None:
        try:
            user = api.get_user(screen_name=username)
        except tweepy.errors.NotFound:
            print("USERNAME")
            raise InvalidEntry(username, user_id)

    else:
        raise BrokenCode(BrokenCode.text)
    profileOG = user.profile_image_url

    final_image = profileOG.replace("_normal", "")
    print(f"Image Found: {final_image}")
    return final_image


fetch_image(user_id=1517894403758641152)

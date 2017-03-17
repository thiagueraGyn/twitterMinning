import twitter

from auth import access_token_key, access_token_secret, consumer_key, consumer_secret

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token_key,
                  access_token_secret=access_token_secret)

api.VerifyCredentials()

status_list = api.GetSearch(
    geocode=None, term=u'Globo', since_id=None,
    lang='pt', count=10, result_type='recent'
)

for s in status_list:
    print(s.text)

# help(twitter.Status)

# status_list[0].GetText()

# hashtags = dict()
#
# for status in status_list:
#     status_hashtags = status.hashtags
#     for hash in status_hashtags:
#         if hashtags.get(hash.text) is None:
#             hashtags[hash] = 1
#         else:
#             hashtags[hash] += 1
#
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(hashtags)

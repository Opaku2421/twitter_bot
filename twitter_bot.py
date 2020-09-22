import tweepy
import os # operating system library

def create_api():
  consumer_key = 'iHc80IFPd2sUUWNgkedCoaUY1' #API key
  consumer_secret = 'jUqOcAd4hsei5Te7IHwvmgsCG1yN0OQt55gQifNG5h4PRwHoVj' #API secret key
  access_token = '1301492837033205760-aLMAbgUMVk08Xxmd4QILHSQukiSXFC'
  access_token_secret = 'zcDNlvWCz7hvkPIphnZUDyTt0FFf7K0fPysL30EsKP1oC'

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
  api.verify_credentials()
  print('API Created')
  return api
  
# Complete code
import time

def follower_count(user):
  emoji_numbers =  {0: "0️⃣", 1: "1️⃣", 2: "2️⃣", 3: "3️⃣",
                      4: "4️⃣", 5: "5️⃣", 6: "6️⃣", 7: "7️⃣", 8: "8️⃣", 9: "9️⃣"}

  uf_split = [int(i) for i in str(user.followers_count)]# Used to seperate 

  emoji_followers = ''.join([emoji_numbers[j] for j in uf_split if j in emoji_numbers.keys()]) 
  return emoji_followers

api = create_api()

while True:
    user = api.get_user('HolesomeD')
    api.update_profile(name=f'Holesome|{follower_count(user)} Doughnut')
    print(f'Updating Twitter Name : Holesome|{follower_count(user)} Doughnut')
    print('Waiting to refresh')
    time.sleep(60)

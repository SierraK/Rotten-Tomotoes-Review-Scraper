# Tool for scraping reviews from Rotten Tomatoes

## Gathering reviews
from bs4 import BeautifulSoup
import requests
import pickle
from time import sleep
from IPython.display import clear_output
from random import randint
from time import time

user_agent = {'User-agent': "Chrome"}
pages = [str(i) for i in range(1,617)]
review = []
review_text = []

start_time = time()
num_requests = 0

for page in pages:
   r = requests.get("https://www.rottentomatoes.com/m/captain_marvel/reviews/?page=" + str(pages) + "&type=user&sort=", headers= user_agent)
   sleep(randint(10,25))
   
   num_requests += 1
   elapsed_time = time() - start_time
   print('Request:{}; Frequency: {} requests/s'.format(num_requests, num_requests/elapsed_time))
   clear_output(wait = True)
   
   soup = BeautifulSoup(r.text, 'html5lib')
   review += soup.find_all('div',{"class": "user_review"})
for i in review:
   review_text.append(i.text)
with open('reviews.pkl', 'wb') as f:
   pickle.dump(review_text, f)
   
## Loading pickel
with open('reviews.pkl', 'rb') as f:
    reviews = pickle.load(f)
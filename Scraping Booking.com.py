#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
import re
import requests
from selenium.webdriver.common.by import By


# In[1]:


driver = webdriver.Chrome()


# In[4]:


driver.get('https://www.booking.com/searchresults.en-gb.html?ss=New+York%2C+New+York+State%2C+United+States&ssne=Singapore&ssne_untouched=Singapore&label=gen173nr-1BCAEoggI46AdIM1gEaMkBiAEBmAEJuAEHyAEN2AEB6AEBiAIBqAIDuAKQnaalBsACAdICJDkxOGJlOTZkLTExYWEtNDZiZS1hNjM0LWVhYTA1ZGY1NGIzZdgCBeACAQ&sid=748ef600edae81b0c93ae093daa3ecb1&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=20088325&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=a3716cafc68c016d&ac_meta=GhBhMzcxNmNhZmM2OGMwMTZkIAAoATICZW46CE5ldyBZb3JrQABKAFAA&checkin=2023-08-26&checkout=2023-08-27&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD')


# In[5]:


#Actual run multiple scrape page using the offset
number_of_reviews = []
location = []
rating = []
distance_from_centre = []
hotel_name = []
hotel_price = []

for page in range (1, 16):
    offset = page*25
    url = 'https://www.booking.com/searchresults.en-gb.html?label=gen173nr-1BCAEoggI46AdIM1gEaMkBiAEBmAEJuAEHyAEN2AEB6AEBiAIBqAIDuAKQnaalBsACAdICJDkxOGJlOTZkLTExYWEtNDZiZS1hNjM0LWVhYTA1ZGY1NGIzZdgCBeACAQ&sid=748ef600edae81b0c93ae093daa3ecb1&aid=304142&ss=New+York%2C+New+York+State%2C+United+States&ssne=Singapore&ssne_untouched=Singapore&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=20088325&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=a3716cafc68c016d&ac_meta=GhBhMzcxNmNhZmM2OGMwMTZkIAAoATICZW46CE5ldyBZb3JrQABKAFAA&checkin=2023-08-26&checkout=2023-08-27&group_adults=2&no_rooms=1&group_children=0&selected_currency=USD&offset=' + str(offset)
    print(url)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    for review in soup.find_all('div', {'class': 'd8eab2cf7f c90c0a70d3 db63693c62'}):
        review = review.text
        number_of_reviews.append(review)
    for places in soup.find_all('span', {'class': 'f4bd0794db b4273d69aa'}): 
        places = places.text 
        location.append(places)

    
    for rate in soup.find_all('div', {'class': 'b5cd09854e d10a6220b4'}):
        rate = rate.text
        rating.append(rate) 
        
    for distance in soup.find_all('span', {'data-testid': 'distance'}):
        distance = distance.text
        distance_from_centre.append(distance)
        
    for name in soup.find_all('div', {'class': 'fcab3ed991 a23c043802'}):
        name = name.text
        hotel_name.append(name)
        
    for price in soup.find_all('span', {'class': 'fcab3ed991 fbd1d3018c e729ed5ab6'}):
        price = price.text
        hotel_price.append(price)


x = 'Show on map' 
while x in location:
    location.remove(x)


print(hotel_price)
print(hotel_name)


# In[6]:


df = pd.DataFrame(list(zip(hotel_name, hotel_price, location, rating, distance_from_centre, rating, number_of_reviews)), columns =['Hotel Names', 'Hotel Prices', 'Location', 'Hotel Rating', 'Distance From City Centre', 'Hotel Rating', 'Number of Reviews']) 

display(df)


# In[7]:


df.to_csv('/Users/declansaw/Documents/Bookingdotcom.csv')


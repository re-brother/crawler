# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# import webdriver
from selenium import webdriver
import urllib.parse
import urllib.request
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import time
import pandas as pd



# Setting about chromedriver
# input a chromedriver path
chromedriver = 'chromedriver.exe'

# Option Setting about chromedriver
options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')

# Apply Options about ChromeDriver
driver = webdriver.Chrome(chromedriver, options=options)

# Set URL to crawling
url = 'https://www.ilbe.com/'

# Calling URL for Crawling
driver.get(url)

# Click Daily Best -> more
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[1]/a').click()

# Posts Title array
post_title = []

# Create Comment Array
comment_array = []

# Scroll Down Function
def scroll_down():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# Include ad case
'''
def comment_crawling_ad():
    for n in range(1, 50):
	print(driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div[3]/div[4]/div/div[' + str(n) + ']/div[1]/div/span/span').text)
'''
# Not Include ad case
def comment_crawling_noad():
    for n in range(1, 50):
        try:
            print(driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div[3]/div[3]/div/div[' + str(n) + ']/div[1]/div/span/span').text)
            comment_array.append(driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div[3]/div[3]/div/div[' + str(n) + ']/div[1]/div/span/span').text)
        except:
            break
            
# Checking Ad
'''
def check_ad():
    current_url = driver.current_url
    print(current_url)
    with urllib.request.urlopen(current_url) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
'''        
    

# loop Click Posts
# i --> 1 page [i]post
def page_scraper():
    try:
        for i in range(0, 29):
            time.sleep(2)
            ''' -- Removed
            #Get scroll height
                height = driver.execute_script("return document.body.scrollHeight")
            '''
            #Scroll down to bottom and wait
            scroll_down()
            time.sleep(1)
            
            # title_temp => post title
            title_temp = driver.find_element_by_xpath('//html/body/div[1]/div[2]/div[1]/div[1]/div[3]/ul/li['+ str(i+8) +']/span[2]/a').text
            
            # If there is title_temp in array post_title, processed normally
            if ((title_temp in post_title) == False):
                post_title.append(title_temp)
                driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div[3]/ul/li['+ str(i+8) +']/span[2]/a').click()
                time.sleep(3)
                scroll_down()
                        
                #print(post_title)
                comment_crawling_noad()
                # Go to Back-Page
                driver.back()
            # Case Overlap
            else:
                print('overlap!', title_temp)
                pass
            i = i + 1
    except:
        print("Error")

def scraper_run():
    for num in range(0, 149):
        page = 24432 - num
        driver.get("https://www.ilbe.com/list/ilbe?page=" + str(page) + "&listStyle=list")
        page_scraper()

def save_csv():
    comment_frame = pd.DataFrame(comment_array)
    comment_frame.to_csv("D:/dev/AttackComments24432.csv", header=False, index=False)

scraper_run()

save_csv()
# End to current page --> Go to Next page


# Create Data Frame
# ilbe_df = pd.DataFrame()
# /html/body/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[2]/a[1]

# Comment ID
# /html/body/div[1]/div[2]/div[1]/div[1]/div[3]/div[4]/div/div[1]/div[1]/span[1]/a

# Comment Date
# /html/body/div[1]/div[2]/div[1]/div[1]/div[3]/div[4]/div/div[1]/div[1]/span[2]
# /html/body/div[1]/div[2]/div[1]/div[1]/div[3]/div[4]/div/div[1]/div[1]/span[2]/strong
# /html/body/div[1]/div[2]/div[1]/div[1]/div[3]/div[4]/div/div[1]/div[1]/span[2]/text()

# Comment source
# /html/body/div[1]/div[2]/div[1]/div[1]/div[3]/div[4]/div/div[1]/div[1]/div/span/span

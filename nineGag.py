"""
Need to install bs4 module in order to make it work.
"""

from bs4 import BeautifulSoup
import requests

class nine_gag:

    def __init__(self):
        #Potentially you can decide to scan any 9gag section with these tool, i guess
        self.url = 'www.9gag.com'
        self.r  = requests.get("http://" +self.url)
        self.data = self.r.text
        self.soup = BeautifulSoup(self.data,"html.parser")
        # DEBUG: print (soup.prettify())

    #givePost() will return post's title and is refer (E.g.: '9xv92'), in order
    #to fetcht that post you need to use 'http://www.9gag.com'+outRef
    
    def givePosts(self):
        outTitle=[]
        outRef=[]
        for link in self.soup.find_all('a',text=True,class_='badge-evt badge-track'):
         #print(link)
         outRef.append(link.get('href'))
         outTitle.append(link.find_all(text=True)[0].strip())

        return outTitle,outRef

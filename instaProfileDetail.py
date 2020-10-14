#Getting instagram Profile detail Using python

from bs4 import BeautifulSoup
import requests

URL = "https://www.instagram.com/{}/"

#parse function
def parse_data(s):
    #creating a dictionary
    data = {}
    #splitting the content
    #then taking the first part
    s = s.split("-")[0]
    #again spliting the content
    s = s.split(" ")

    data['Followers'] = s[0]
    data['Following'] = s[2]
    data['Posts'] = s[4]

    return data

#scrap function
def scrape_data(username):
    r = requests.get(URL.format(username)) #getting the request from url
    s = BeautifulSoup(r.text, 'html.parser') #converting the text
    meta = s.find('meta', property='og:description') #finding the meta data

    return parse_data(meta.attrs['content'])


#main function
if __name__ == "__main__":
    #username
    username = input("Enter username: ")
    data = scrape_data(username)
    print(data)

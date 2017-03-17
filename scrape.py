import requests
from bs4 import BeautifulSoup

def scrape():
    url = "http://www.straitstimes.com/singapore"
    r = requests.get(url)
    page = BeautifulSoup(r.text,'html.parser')
    headlines = page.find_all(class_="story-headline")
    imgs = page.find_all('img',class_='image-style-retina_large')
    #get all the headline
    for headline in headlines:
        print (headline.get_text())
        #get all headlineurl
        headlineurl = headline.find('a')
        print ("http://straitstimes.com/{0}".format(headlineurl.get('href')))

    #get all imgurl of the headlines
    i = 0
    for img in imgs:
        #only get img with odd array position, even array position are thumbnails
        if i%2==1:
            print (img)
            imglink = img['src']
            #imglink
        i=i+1

scrape()

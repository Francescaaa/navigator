from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('id')[:3]
    data = {
        'posts':posts,
    }
    return render(request,'mainpage/mainpage.html',data)

def scrape(request):
    url = "http://www.straitstimes.com/singapore"
    r = requests.get(url)
    page = BeautifulSoup(r.text,'html.parser')
    headlines = page.find_all(class_="story-headline")
    imgs = page.find_all('img',class_='image-style-retina_large')
    #get all the headline
    for headline in headlines:
        #if it is a new headline, create new post
        if not Post.objects.filter(headline=headline.get_text()):
            new_post = Post()
            new_post.headline = headline.get_text()
            headlineurl = headline.find('a')
            new_post.headlineurl = "http://straitstimes.com/{0}".format(headlineurl.get('href'))
            new_post.save()
        #else just ignore

    #get all imgurl of the headlines
    i = 0
    for img in imgs:
        #only get img with odd array position, even array position are thumbnails
        if i%2==1:
            new_post = Post.objects.get(id=(i/2+1))
            imglink = img['src']
            new_post.imgurl = imglink
            new_post.save()
            #print ((i+2)/2+1)
        i=i+1
    return redirect("/mainpage")

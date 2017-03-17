from django.db import models

# you'll need to create your instances and then save the
from django.utils import timezone

class Post(models.Model):
    headline = models.CharField(max_length=140)
    headlineurl = models.CharField(max_length=140)
    imgurl = models.CharField(max_length=140)

    def __str__(self):
        return self.headline




# """
#     def StorageData(self,data):
#         for post in data:
#             post = Post(headline=post.headline, headlineurl=post.headlineurl, imgurl=post.imgurl)
#             post.save()
#
#         data = []
#
#         for object in scrape:
#             object = {
#                 'headline': scrape.headline,
#                 'headlineurl': scrape.headlineurl,
#                 'imgurl': scrape.imgurl,
#             }
#             data.append(object)
#
# class Post(models.Model):
#     headline = models.CharField(max_length=140)
#     headlineurl = models.URLField()
#     imgurl = models.URLField()
#
# #lists out all posts
#     def __str__(self):
#         return self.title
# """

from django.db import models
import os
import random
import string
# Create your models here.
counter = 0

list_of_objects_short = dict()
list_of_objects_long = dict()

class UrlModel(object):

    '''
    this class will store the url's mapping and works as db
    '''
    global list_of_objects_short

    def mapper(self, long_url, short_url):
        list_of_objects_short[long_url] = short_url
        list_of_objects_long[short_url] = long_url

    def retrun_short_url(self, url):
        return list_of_objects_short[url]

    def __str__(self):
        return list_of_objects_short[url]


def create_random_encode():

    '''
    function returns three random char for context route
    '''

    # choices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # choice_of_caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'Q', 'R', 'S', 'T']
    # context = ''
    # context = random.choice(choices)
    # context+=random.choice(choice_of_caps)
    # return context

    # improved logic
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters = random.choices(letters, k=3)
        rand_letters = "".join(rand_letters)
        if rand_letters not in list_of_objects_short.keys():
            return rand_letters


def create_short_url(url):
    #print("fucntion call")
    main_url = 'http://127.0.0.1:8000/'
    short_url = main_url+create_random_encode()
    obj = UrlModel()
    obj.mapper(url, short_url)
    return list_of_objects_short[url]
    

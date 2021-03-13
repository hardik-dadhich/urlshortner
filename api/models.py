from django.db import models
import os
import random

# Create your models here.
counter = 0

class UrlModel(object):

    '''
    this class will store the url's mapping and works as db
    '''

    list_of_objects = {}

    def __init__(self, long_url):
        self._id = counter+1
        self.long_url = long_url
        self.short_url = None

    def mapper(self, long_url, short_url):
        self.list_of_objects[long_url] = short_url

    
    def retrun_short_url(self):
        return self.short_url

    def return_long_url(self):
        return self.long_url

def create_random_encode():

    '''
    function returns three random char for context route
    '''

    choices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    choice_of_caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'Q', 'R', 'S', 'T']
    context = ''
    context = random.choice(choices)
    context+=random.choice(choice_of_caps)
    return context

    

def main_method():
    db = UrlModel(long_url)


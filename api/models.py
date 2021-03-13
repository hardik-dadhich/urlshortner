from django.db import models
#from tinydb import TinyDB
import os
import random

# Create your models here.

class Userinput():

    '''
    this class will take user input
    '''

    def create_random(self):
        '''
        function returns thee random context
        '''
        
        choices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        choice_of_caps = ['A', 'B', 'C', 'D', 'E' ]
        context = ''
        context = random.choice(choices)
        context+=random.choice(choice_of_caps)
        return context

    def tackle_input(self, url):

        data_base = {}
        if url not in data_base:
            pass

    # def create_db(userinput):
    #     dir_path = os.getcwd()
    #     print(dir_path)
    #     list_files = os.listdir(dir_path) 
    #     if 'data.txt' not in list_files: 
    #         with open(os.path.join(dir_path/, 'data.txt'), 'w') as fp:
    #             fp.write(userinput, 'a+')



   

u = Userinput()
print(u.create_random())
    

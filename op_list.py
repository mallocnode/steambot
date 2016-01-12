#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import re
import filter
import message_sender
import time,random
from urllib.request import urlopen

#read_file for each line in the file
#save string in a list then call
#split_list

def read_file(filename):
    l_link_no_split = open(filename, 'rU').readlines()
    return split_list(l_link_no_split)



#split_list divide each string
#of each element in the list_from_file
#and for each list is saved in a new list(of list)

def split_list(list_from_file):
    l_split = []

    for item in list_from_file:
        l_split.append(item.split(', '))

    return l_split

#create_list_of_price take a list of
#link and return a list of all the
# price in it

def create_list_of_price(list_of_link):
    list_of_price=[]
    i = 0
    while i< len(list_of_link):
        try:
            time.sleep(random.randint(10,15))
            html_source = urlopen(list_of_link[i][2]).read()
        except:
            message_sender.send('Probably some error loading the link')
            pass
        list_of_price.append([list_of_link[i][0]]+[list_of_link[i][1]]+filter.html_source(html_source))
        i+=1
    return list_of_price

#calculate_threshold calculate the
#threshold of a given list
def calculate_threshold(price):

    threshold=price-price*15/100

    return threshold



#check_last_price take all the list
#from the file and for each list
#calculate the min value, it return
#a list of all the min value
def check_last_price(filename):
    old_price=[]
    price=read_file(filename)
    app=[]

    for item in price:
        i=0
        while i<len(item):
            o=(item[i].replace('\n',''))
            o=re.findall('\d+.\d+',o)

            if o :
                app.append(float(o[0]))
            i+=1
        app=map(float,app)
        ok=min(app)
        old_price.append(ok)

        app=[]

    return old_price


#save_price write the list_of_item
#in the given filename
def save_price(filename,list_of_item):
    f=open(filename,'w')

    for item in list_of_item:
        f.write(str(item).replace('[','').replace(']','').replace('\'',''))
        f.write('\n')

    f.close()


#check_threshold send the message
#if the threshold condition is
#true
def check_threshold(filename,li):

    la=check_last_price(filename)
    i=0
    while i<len(li):
        #threshold condition
        try:
            if li[i][2]<calculate_threshold(la[i]):
                message_sender.send(str(li[i][1])+str(' ')+str(li[i][2]))
            i+=1
        except:
            message_sender.send(str('len la')+str(len(la)+str('len li')+str(len(li))))


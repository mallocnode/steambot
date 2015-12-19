#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-

import message_sender

#ho_ko_dollar_to_eur take a list of
#values and: convert it in float and €

def ho_ko_dollar_to_eur(values):

        new_values=[]
        if len(values)<1:
            return values
        #convert to float and handle errors
        try:
            values=to_float(values)
        except:
            print 'Error in ho_ko_dollar_to_eur.'+r'The values in the list can\'t be converted'

        #create new list with eur values
        for item in values:
            new_values.append(float('%.2f' % float(item*0.1146)))

        return new_values

#pound_to_eur take a list of
#values and: convert it in float and €

def pound_to_eur(values):

        new_values=[]
        if len(values)<1:
            return values
        #convert to float and handle errors
        try:
            values=to_float(values)
        except:
            print 'Error in pound_to_eur.'+r'The values in the list can\'t be converted'

        #create new list with eur values
        for item in values:
            new_values.append(float('%.2f' % float(item*1.38653389)))

        return new_values

#s_cor_won_to_eur take a list of
#values and: convert it in float and €

def s_cor_won_to_eur(values):

        new_values=[]
        if len(values)<1:
            return values
        #convert to float and handle errors
        try:
            values=to_float(values)
        except:
            print 'Error in s_cor_won_to_eur.'+r'The values in the list can\'t be converted'

        #create new list with eur values
        for item in values:
            new_values.append(float('%.2f' % float(item*0.00076643954)))

        return new_values

#can_dollars_to_eur take a list of
#values and: convert it in float and €

def can_dollars_to_eur(values):

        new_values=[]

        if len(values)<1:
            return values

        #convert to float and handle errors
        try:
            values=to_float(values)
        except :
            print 'Error in can_dollars_to_eur.'+r'The values in the list can\'t be converted'

        #create new list with eur values
        for item in values:
            new_values.append(float('%.2f' % float(item*0.670910)))

        return new_values

#newzel_dollars_to_eur take a list of
#values and: convert it in float and €

def newzel_dollars_to_eur(values):

        new_values=[]

        if len(values)<1:
            return values

        #convert to float and handle errors
        try:
            values=to_float(values)
        except :
            print 'Error in newzel_dollars_to_eur.'+r'The values in the list can\'t be converted'

        #create new list with eur values
        for item in values:
            new_values.append(float('%.2f' % float(item*0.617988)))

        return new_values

#rupiah_to_eur take a list of
#values and: convert it in float and €

def rupiah_to_eur(values):

        new_values=[]

        if len(values)<1:
            return values

        #convert to float and handle errors
        try:
            values=to_float(values)
        except :
            print 'Error in rupiah_to_eur.'+r'The values in the list can\'t be converted'

        #create new list with eur values
        for item in values:
            new_values.append(float('%.2f' % float(item*0.00028)))

        return new_values


#colo_pes_to_eur take a list of
#values and: convert it in float and €

def col_pes_to_eur(values):

        new_values=[]

        if len(values)<1:
            return values

        #convert to float and handle errors
        try:
            values=to_float(values)
        except :
            print 'Error in col_pes_to_eur.'+r'The values in the list can\'t be converted'


        #create new list with eur values
        for item in values:
            new_values.append(float('%.2f' % float(item*0.00027)))

        return new_values

#bri_puond_to_eur take a list of
#values and: convert it in float and €

def bri_puond_to_eur(values):

        new_values=[]

        if len(values)<1:
            return values

        #convert to float and handle errors
        try:
            values=to_float(values)
        except :
            print 'Error in bri_puond_to_eur.'+r'The values in the list can\'t be converted'

        #create new list with eur values
        for item in values:
            new_values.append(float('%.2f' % float(item*0.0251015736)))

        return new_values

#cor_swe_to_eur take a list of
#values and: convert it in float and €

def cor_swe_to_eur(values):

        new_values=[]

        if len(values)<1:
            return values

        #convert to float and handle errors
        try:
            values=to_float(values)
        except :
            print 'Error in cor_swe_to_eur.'+r'The values in the list can\'t be converted'

        #create new list with eur values
        for item in values:
            new_values.append(float('%.2f' % float(item*0.107311)))

        return new_values
#usd_to_eur take a list of
#values and: convert it in float and €

def usd_to_eur(values):

        new_values=[]

        if len(values)<1:
            return values


        #convert to float and handle errors
        try:
            values=to_float(values)
        except :
            print 'Error in usd_to_eur.'+'The values in the list can\'t be converted'
            message_sender.send('Error in Usd_to_eur. Probably a new value')

        #create new list with eur values
        for item in values:
            new_values.append(float('%.2f' % float(item*0.910705341)))

        return new_values

#yen_to_eur take a list of
#values and: convert it in float and €

def yen_to_eur(values):

        new_values=[]

        if len(values)<1:
            return values

        #convert to float and handle errors
        try:
            values=to_float(values)
        except:
            print 'Error in yen_to_eur.'+r'The values in the list can\'t be converted'


        #create new list with eur values
        for item in values:
            new_values.append(float('%.2f' % float(item*0.14074)))
        message_sender.send('Fucking cinese currency')
        return new_values

#mal_rig_to_eur take a list of
#values and: convert it in float and €

def mal_rig_to_eur(values):

        new_values=[]

        if len(values)<1:
            return values

        #convert to float and handle errors
        try:
            values=to_float(values)
        except:
            print 'Error in mal_rig_to_eur.'+r'The values in the list can\'t be converted'


        #create new list with eur values
        for item in values:
            new_values.append(float('%.2f' % float(item*0.211740)))

        return new_values


#bra_dollars_to_eur take a list of
#values and: convert it in float and €

def bra_dollars_to_eur(values):

        new_values=[]

        if len(values)<1:
            return values

        #convert to float and handle errors
        try:
            values=to_float(values)
        except:
            print 'Error in bra_dollars_to_eur.'+r'The values in the list can\'t be converted'

        #create new list with eur values
        for item in values:
            new_values.append(float('%.2f' % float(item*0.241374018)))

        return new_values

#swiss_franc_to_eur take a list of
#values and: convert it in float and €

def swiss_franc_to_eur(values):

        new_values=[]

        if len(values)<1:
            return values

        #convert to float and handle errors
        try:
            values=to_float(values)
        except:
            print 'Error in swiss_franc_to_eur.'+r'The values in the list can\'t be converted'

        #create new list with eur values
        for item in values:
            new_values.append(float('%.2f' % float(item*0.924997841)))

        return new_values

#lir_turc_to_eur take a list of
#values and: convert it in float and €

def lir_turc_to_eur(values):

        new_values=[]

        if len(values)<1:
            return values

        #convert to float and handle errors
        try:
            values=to_float(values)
        except:
            print 'Error in lir_turc_to_eur.'+r'The values in the list can\'t be converted'

        #create new list with eur values
        for item in values:
            new_values.append(float('%.2f' % float(item*0.312207)))

        return new_values

#sig_dollars_to_eur take a list of
#values and: convert it in float and €

def sig_dollars_to_eur(values):

        new_values=[]

        if len(values)<1:
            return values

        #convert to float and handle errors
        try:
            values=to_float(values)
        except:
            print 'Error in sig_dollars_to_eur.'+r'The values in the list can\'t be converted'

        #create new list with eur values
        for item in values:
            new_values.append(float('%.2f' % float(item*0.11753)))

        return new_values

#convert_py6_to_eur take a list of
#values and: convert it in float and €

def py6_to_eur(values):

        new_values=[]

        if len(values)<1:
            return values

        #convert to float and handle errors
        try:
            values=to_float(values)
        except:
            print 'Error in py6_to_eur.',r'The values in the list can\'t be converted'

        #create new list with eur values
        for item in values:
            new_values.append(float('%.2f' % float(item*0.0130854696921585)))

        return new_values

#to_float take a string
# and convert it to float
#It replace the "," with "."

def to_float(string_list):

    if len(string_list)<1:
        return string_list

    i=0

    while i<len(string_list):

        string_list[i]=string_list[i].replace(',','.')
        string_list[i]=float(string_list[i])
        i+=1

    return string_list
#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import re
import convert_price, message_sender


#html_filter take one html source
#code and take all the price
#it return a list with all the price
#converted in €

def html_source(source):

    #take the various values in the source
    #NOTA:non tutte le valute vengono considerate

    no_filtered_price=re.findall('<span class="market_listing_price market_listing_price_with_fee">\s+(.+)\t\t\t\t\t</span>',source)

    price=list_of_price(no_filtered_price)
    price=sorted(price)

    return price


#list_of_price take a list of string
#and convert it in float values if
#they contain numerical values

def list_of_price(no_filtered_list):

    eur_price=[]
    py6_price=[]
    newzel_dol_price=[]
    canadian_dollar=[]
    bri_pound_price=[]
    usd_price=[]
    bra_dollars_price=[]
    lir_turc_price=[]
    sig_dollar=[]
    yen_price=[]
    cor_swe_price=[]
    swiss_franc_price=[]
    ho_ko_dollar=[]
    for item in no_filtered_list:
        if '--' in item:
            item=item.replace('--','').replace(' ','')
        if 'p\xd1\x83\xd0\xb1.' in item:
            py6_price.append(item.replace('p\xd1\x83\xd0\xb1.','').replace(' ',''))
        elif 'NZ$' in item:
            newzel_dol_price.append(item.replace('NZ$','').replace(' ',''))
        elif 'HK$' in item:
            newzel_dol_price.append(item.replace('HK$','').replace(' ',''))
        elif 'CHF' in item:
            swiss_franc_price.append(item.replace('CHF','').replace(' ',''))
        elif '\xc2\xa3' in item:
            bri_pound_price.append(item.replace('\xc2\xa3','').replace(' ',''))
        elif 'CDN$' in item:
            canadian_dollar.append(item.replace('CDN$','').replace(' ',''))
        elif 'USD' in item:
            usd_price.append(item.replace('USD','').replace('$','').replace(' ',''))
        elif '€' in item:
            eur_price.append(item.replace('€','').replace(' ',''))
        elif 'R$' in item:
            bra_dollars_price.append(item.replace('R$','').replace(' ',''))
        elif 'S$' in item:
            sig_dollar.append(item.replace('S$','').replace(' ',''))
        elif 'TL' in item:
            lir_turc_price.append(item.replace('TL','').replace(' ',''))
        elif '\xc2\xa5' in item:
            yen_price.append(item.replace('\xc2\xa5','').replace(' ',''))
        elif 'kr' in item:
            cor_swe_price.append(item.replace('kr','').replace(' ',''))
        elif '$' in item:
            usd_price.append(item.replace('$','').replace(' ',''))
        else:
             message_sender.send('New match ' +str(item))

    price=convert_price.py6_to_eur(py6_price)+convert_price.usd_to_eur(usd_price)+\
    convert_price.to_float(eur_price)+convert_price.newzel_dollars_to_eur(newzel_dol_price)+\
    convert_price.can_dollars_to_eur(canadian_dollar)+convert_price.bri_pound_to_eur(bri_pound_price)+\
    convert_price.bra_dollars_to_eur(bra_dollars_price)+convert_price.sig_dollars_to_eur(sig_dollar)+\
    convert_price.lir_turc_to_eur(lir_turc_price)+convert_price.yen_to_eur(yen_price)+\
    convert_price.cor_swe_to_eur(cor_swe_price)+convert_price.swiss_franc_to_eur(swiss_franc_price)+\
    convert_price.ho_ko_dollar_to_eur(ho_ko_dollar)

    return price
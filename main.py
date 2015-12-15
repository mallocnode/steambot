#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import sys, time,random
import op_list



def main():

    file1=sys.argv[1]
    file2=sys.argv[2]

    #this list will save the current price on the file2
    #so you will not get error when calling the
    # check_threshold function
    op_list.save_price(file2,op_list.create_list_of_price(op_list.read_file(file1)))
    while True:
        try:
            price=op_list.create_list_of_price(op_list.read_file(file1))
            op_list.check_threshold(file2,price)
            op_list.save_price(file2,price)
            time.sleep(random.randint(250,350))
        except:
            message_sender.send('Some error in main')


if __name__ == '__main__':
    main()

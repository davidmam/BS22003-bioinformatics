# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
errmsg='''An error occurred in your code. 
Please check the previous cells have all been run correctly and in order'''

def test1():
    try:    
        if enzyme=='TCCGGA':
            print('variable enzyme created correctly')
        else:
            print('variable enzyme not created correctly')
    except:
        print(errmsg)
def test2():
    try:
        if frag1==840:
            print("Fragment 1 correct" )
        else:
            print("Fragment 1 incorrect")
        if frag2==731 :
            print("Fragment 2 correct" )
        else:
            print("Fragment 2 incorrect")
        if frag3== 556 :
            print("Fragment 3 correct" )
        else:
            print("Fragment 3 incorrect")
    except:
        print(errmsg)
        
        
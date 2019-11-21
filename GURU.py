#!/usr/bin/env py)thon3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 21:09:51 2019

@author: gurucharan
"""

def linelen(string):
    return len(string)

def fileLinecount():
    with open("/home/ashutosh/Desktop/GURU/asd.txt") as fin:
        for line, ele in enumerate(fin):
                #pass
                print(ele)
    return line + 1   

#fname = input("Enter the name of the file\n")
print(fileLinecount())

def encryp(file):
    with open(file , 'a') as fin:
        intab = 'abcdefghijklmnopqrstuvwxyz'
        outtab = '~!@#$%^&*()_+`1234567890-='
        trantab = str.maketrans(intab , outtab)
        fin.translate(trantab)
    return fin

def decryp(file) :
    with open(file , 'a') as fin:
        dec = 'abcdefghijklmnopqrstuvwxyz'
        en = '~!@#$%^&*()_+`1234567890-='
        trantab = str.maketrans(en , dec)
        fin.translate(trantab)
    return fin


#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import commands
import sys

service_name = "httpd"
def check_service_status(service_name):

        status = os.system('service '+service_name+ ' status > /dev/null')
        return status
file = open('stav.txt','a')


def main():

        if (check_service_status(service_name) == 0):
                st = "HTTPD UP!! "
                file.write(st + '\n')
                file.close()
        else:
                st = "HTTPD DOWN!! "
                file.write(st + '\n')
                file.close()
main()



service_name1 = "mysqld"
def check_service_status(service_name1):

        status = os.system('service '+service_name1+ ' status > /dev/null')
        return status

file = open('stav.txt','a')

def main():

         if (check_service_status(service_name1) == 0):
                st = "MYSQL UP!!"
                file.write(st + '\n')
                file.close()
         else:
                st = "MYSQL DOWN!!"
                file.write(st + '\n')
                file.close()
main()

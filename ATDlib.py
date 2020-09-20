import requests
from socket import *
import urllib
import os
import sys

input_file = '/Users/lonetitan/Documents/MIDAS/atd/Files/test-live__session_151000__response_267567_1667467_6346443_18318414__YONaIrjD5EKnIYmh4WwU1A.txt'


class ATD:
    """Python3 implementation of library After The DeadLine. Currently server is set to localhost but can be changed.Any 32 length Hex key will work. Download source code from https://open.afterthedeadline.com/download/download-source-code/ to run local atd server"""
    input_file = None
    key = '6EF6B30F9E557F948C402C89002C7C8A'    # Any 32 Hex key would work
    url = "http://127.0.0.1:1049/"  # Currently only for local host

    def setInputFile(self, inp):
        """Enter the location of input file either in absolute or relative path scheme. File must be .txt only"""
        self.input_file = inp
        try:
            if(os.path.isfile(self.input_file)):
                print("Valid File Name, continuing")
                return
        except:
            self.input_file = None
            raise Exception("Invalid file : file does not exist")

    def stats(self):
        """This function will return number of sentences(an estimate) and total number of words used. Total number of tries will be 5 before terminating the request."""
        counter = 0
        while(counter < 5):
            if(self.input_file == None):
                raise Exception('Please provide input file first')
            if(self.key == None):
                raise Exception('Please provide any 32 Hex valid key first')

            curr_url = self.url + "stats"
            f = open(self.input_file, 'r')
            text = f.read()
            text = text.lower()
            params = urllib.parse.urlencode(
                {'key': '6EF6B30F9E557F948C402C89002C7C8B', 'data': text})
            resp = requests.post(curr_url, data=params)
            if(len(resp.text) == 0):
                counter += 1
                continue
            return resp.text
        print("Some Error occured. Cannot get a valid response from server.")

    def checkDocument(self):
        """The service will send one or more error items. The string item is the phrase in question. The precontext is the token before the string item. Sometimes this variable is empty. Total number of tries will be 5 before terminating the request."""
        counter = 0
        while(counter < 5):
            if(self.input_file == None):
                raise Exception('Please provide input file first')
            if(self.key == None):
                raise Exception('Please provide any 32 Hex valid key first')

            curr_url = self.url + "checkDocument"
            f = open(self.input_file, 'r')
            text = f.read()
            text = text.lower()
            params = urllib.parse.urlencode(
                {'key': '6EF6B30F9E557F948C402C89002C7C8B', 'data': text})
            resp = requests.post(curr_url, data=params)
            if(len(resp.text) == 0):
                counter += 1
                continue
            return resp.text
        print("Some Error occured. Cannot get a valid response from server.")

    def checkGrammar(self):
        """This call is the same as /checkDocument except it does not include spelling errors. Total number of tries will be 5 before terminating the request"""
        counter = 0
        while(counter < 5):
            if(self.input_file == None):
                raise Exception('Please provide input file first')
            if(self.key == None):
                raise Exception('Please provide any 32 Hex valid key first')

            curr_url = self.url + "checkGrammar"
            f = open(self.input_file, 'r')
            text = f.read()
            text = text.lower()
            params = urllib.parse.urlencode(
                {'key': '6EF6B30F9E557F948C402C89002C7C8B', 'data': text})
            resp = requests.post(curr_url, data=params)
            if(len(resp.text) == 0):
                counter += 1
                continue
            return resp.text
        print("Some Error occured. Cannot get a valid response from server.")


def main():
    atd = ATD()
    inp = atd.setInputFile(input_file)
    print(atd.checkDocument())


if(__name__ == '__main__'):
    main()

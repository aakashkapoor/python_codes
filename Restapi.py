# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 18:33:34 2018

@author: Delol
"""

url = "http://api.openweathermap.org/data/2.5/weather"
url += "?q=Jaipur&appid=e624252c34d87485485d6f6dbe3000a6"


# Using urllib2 library
import urllib2

resp = urllib2.urlopen(url)   # GET request to REST API

print resp.read()   # prints the server Response

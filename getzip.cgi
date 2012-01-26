#!/usr/bin/env python

#Import urllib to be able to open web pages
import urllib
#The line below is used for xml parsing purposes
from xml.dom.minidom import parseString

#These two lines are necessary for running the .cgi file in the browser
print "Content-type: text/html"
print ""

#Open the file that to begin extracting the ip address from
ip_file = urllib.urlopen('http://checkip.dyndns.org/')
#Read the file and store the data in ip_data
ip_data = ip_file.read()
#Close the file
ip_file.close()
#This partition is particular to the site I am grabbing the ip from but basically it grabs only the ip and cuts everything else out
ip = ip_data.partition(':')[2].partition('<')[0].strip()

#Open the file to begin extracting the Zip code
geo_file = urllib.urlopen('http://freegeoip.net/xml/' + ip)
#Read the file and store it in geo_data
geo_data = geo_file.read()
#Close the file
geo_file.close()

#Parse the xml into parsed
parsed = parseString(geo_data)
#Get the xml tag by tag name
xml_tag = parsed.getElementsByTagName('ZipCode')[0].toxml()
#Pull the raw data from that xml tag
xml_data = xml_tag.replace('<ZipCode>', '').replace('</ZipCode>', '')

#Print data for testing
print xml_data
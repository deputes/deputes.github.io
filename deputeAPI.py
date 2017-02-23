import urllib2, requests, zipfile, StringIO, os
import json
from json2html import *
#zip_file_url = input("enter url")

zip_file_url = "http://data.assemblee-nationale.fr/static/openData/repository/LOI/scrutins/Scrutins_XIV.json.zip"

def getURI(zip_file_url):
	print "Fetching... "
	r = requests.get(zip_file_url, stream=True)
	if not r.ok:
		print "invalid uri"
		return getURI()
	elif r.ok:
		print 'is ok'
		print r
	return r

def extract(r):
	print "Extracting..."
	z = zipfile.ZipFile(StringIO.StringIO(r.content))
	print z.namelist()
	z.extractall()
	e = z.namelist()[0]
	print "extracted", e
	return e

def convert(e):
	print "Converting..."
	myHTML = open ('%s.html' %e, 'w')
	with open (e, 'r') as f:
		data = json.load(f)
		j2h = json2html.convert(json = data)
		print j2h
		myHTML.write(j2h.encode('utf-8'))
	myHTML.close()
		
	print "done"

#	input = open(e).read()	
#	json2html.convert(json = input)

def reader(r):
	print len(r.content)


convert(extract(getURI(zip_file_url)))

#response = urllib2.urlopen('http://data.assemblee-nationale.fr/static/openData/repository/LOI/scrutins/Scrutins_XIV.json.zip')
#html = response.read()



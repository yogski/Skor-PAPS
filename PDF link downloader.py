#################################################
# CREATED BY: YOGI SAPUTRO						#
# This program retrieves all pdf links in a web #
# page and download them						#
#												#
#												#
#################################################

#dependencies
from bs4 import BeautifulSoup
import urllib3
import re

#internal functions
def link_input():
	return str(input('Please input the link: \n'))

def getLinks():
	#setup and input URL
	target_url = link_input()
	http = urllib3.PoolManager()
	page = http.request('GET',target_url)
	soup = BeautifulSoup(page.data,"html.parser")
	pdf_links=[]
	
	#find all PDF links in URL
	for link in soup.findAll('a', attrs={'href':re.compile("pdf$")}):
		pdf_links.append(link.get('href'))

	#download PDF files
	for i in range(len(pdf_links)):
		r = http.request('GET',pdf_links[i],preload_content=False)
		with open("Skor PAPS"+str(i+1)+".pdf", 'wb') as out:
			while True:
				data = r.read()
				if not data:
					break
				out.write(data)
		print(pdf_links[i]+' has been downloaded.')
		r.release_conn()

	page.release_conn

#main program
getLinks()
# Use https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

import requests
from bs4 import BeautifulSoup

def change_str():
	html_file = open('bshw3.html', 'w')
	baseurl = "http://collemc.people.si.umich.edu/data/bshw3StarterFile.html"
	r = requests.get(baseurl)
	soup = BeautifulSoup(r.text, 'lxml')
	rep_soup = BeautifulSoup(
		str(soup.prettify()).replace(" student ", " AMAZING student "), 'lxml')

	for pic in rep_soup.find_all('img'):
		if pic.get('src').find("bsi_exposition_041316_192.jpg") >= 0:
			#print ("True")
			pic['src'] = './206Dave/206pic.jpg'
			print (pic['src'])
		else:
			#print ("false")
			pic['src'] = './206Dave/logo.png'
	
	html_file.write(str(rep_soup))
	html_file.close()
#print (soup.find_all('img'))
	#print (type(soup.find_all('img')))

change_str()
'''x = soup.find_all(class_ = "field field-name-body field-type-text-with-summary field-label-hidden")
for elem in x:
	if 'students' in elem:
		elem = elem.replace('students', 'FUCKKKFUCKFUCKUFSIFAOF(**#')
		print (elem)

test = []
for x in soup.find_all(class_ = 'html not-front logged-in two-sidebars page-node page-node- page-node-11581 node-type-general-page section-programs'):
	for next in x.find_all(class_ = 'body-inside'):
		for almost in next.find_all(class_ = 'container3'):
			for p in almost.find_all(class_ = 'main'):
				test.append(p)


print (test)

html_file = open('DSHW3.html', 'w')
#html_file.write(message)
html_file.close()
'''
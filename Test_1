from bs4 import BeautifulSoup
import requests
import lxml
import re

#Name of the anime to be searched
name_anime=input("Enter the name of the anime to search\n")
name_update=name_anime.replace (" ","%20")

#requesting main

search_string_1="https://myanimelist.net/search/all?q="
final_search=search_string_1+name_update
#print(final_search)
search_init=requests.get(final_search)
search_soup=BeautifulSoup(search_init.text,'lxml')
the_final_link=""
for link in search_soup.find_all('a', attrs={'class' : 'hoverinfo_trigger fw-b fl-l'},limit=1):

	#print(link['href'])
	the_final_link=link['href']
	#print(the_final_link)



def scrapeit():
	#ff
	res=requests.get(the_final_link)
#res_content=res.content
	soup=BeautifulSoup(res.text,"lxml")
	soup_re=soup.find_all("span", itemprop="description")
#print(soup.title.string)
	for i in soup_re:
		print(i.text)

scrapeit()

from tkinter import *
from bs4 import BeautifulSoup
import requests
import lxml
import re

#main window
window = Tk()
window.title("Anime Synopsis \n")
window.configure(background="black")

#scraping function
def scrapeit(name_anime):
	name_update=name_anime.replace (" ","%20")
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
	res=requests.get(the_final_link)
	soup=BeautifulSoup(res.text,"lxml")
	soup_re=soup.find_all("span", itemprop="description")
	for i in soup_re:
		return(i.text)

#click_button
def click():
	entered_text=textentry.get()
	output.delete(0.0, END)
	try:
		defination=scrapeit(entered_text)
	except:
		defination="Do you even watch Anime?"
	output.insert(END,defination)


#background 
picture_1=PhotoImage(file="./idk_cool_flower.gif")
Label(window, image=picture_1, bg="black").grid(row=0,column=0,sticky=W)


#label1
Label(window, text="For which anime would you like to find the Synopsis?\n", bg="black", fg="white", font="none 12 bold" ).grid(row=1,column=0,sticky=W)

#entry_box_name
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)

#submit button
Button(window, text="Submit", width=6, command=click).grid(row=3, column=0, sticky=W)

#label2
Label(window,text="Synopsis:\n", bg="black", fg="white", font="none 12 bold").grid(row=4, column=0, sticky=W)

#output text
output=Text(window,width=100, height=30, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=3, sticky=W)



#exit function


#mainloop
window.mainloop()

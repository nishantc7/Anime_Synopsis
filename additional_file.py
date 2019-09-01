from tkinter import *
from bs4 import BeautifulSoup
import requests
import lxml
import re
import tkinter.scrolledtext as tkscrolled
#GitHub link to the application: https://github.com/hardikvasa/google-images-download
from google_images_download import google_images_download


def the_function(the_name):
	the_anime=the_name

	#main window
	window = Tk()
	window.title("Anime Synopsis \n")
	window.configure(background="black")
	window.geometry("1280x720")

	#scraping function
	def scrapeit(name_anime):
		anime_name=name_anime
		name_update=name_anime.replace (" ","%20")
		search_string_1="https://myanimelist.net/search/all?q="
		final_search=search_string_1+name_update
		#print(final_search)
		search_init=requests.get(final_search)
		search_soup=BeautifulSoup(search_init.text,'lxml')
		the_final_link=""
		for link in search_soup.find_all('a', attrs={'class' : 'hoverinfo_trigger fw-b fl-l'},limit=1):

			the_final_link=link['href']
		res=requests.get(the_final_link)
	#res_content=res.content
		soup=BeautifulSoup(res.text,"lxml")
		soup_re=soup.find_all("span", itemprop="description")
	#print(soup.title.string)
		for i in soup_re:
			return(i.text)

		

	#background 
	response = google_images_download.googleimagesdownload()   #class instantiation
	arguments = {"keywords":str(the_name),"limit":1,"format":"gif","size":"icon","silent_mode":1}   #creating list of arguments
	paths = response.download(arguments)
	path_1=str(paths[0].get(str(the_name)))
	path_2=path_1.replace('[','')
	path_3=path_2.replace(']','') 
	path_4=path_3.replace("'",'')
	picture_1=PhotoImage(file=path_4)
	Label(window, image=picture_1, bg="black").grid(row=2,column=0,sticky=N+S+E+W)

	#label2
	Label(window,text="Synopsis:\n", bg="black", fg="white", font="none 12 bold").grid(row=6, column=0,sticky=N+S+E+W)


	#output text
	output=tkscrolled.ScrolledText(window,width=100, height=6, wrap=WORD, background="white")
	output.grid(row=7, column=0, columnspan=3,sticky=N+S+E+W)

	output.delete(0.0, END)
	try:
		defination=scrapeit(the_name)
	except:
		defination="Do you even watch Anime?"
	output.insert(END,defination)
		
	#exit function
	def close_window():
		window.destroy()
		exit()

	#exit label
	Label(window,text="Click here to exit\n", bg="black", fg="white", font="none 12 bold").grid(row=0, column=0,sticky=N+S+E+W)

	#exit button
	Button(window,text="Exit", width=14, command=close_window).grid(row=1, column=0,sticky=N+S+E+W)

	#mainloop
	window.mainloop()

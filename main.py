from tkinter import *
from additional_file import *
the_name="hero"


def when_called():

	def input_function():

		the_name_update=click2()
		the_function(the_name_update)
	
	def click2():
		entered_text=textentry.get()
		#the_name=entered_text
		input_window.destroy()
		return entered_text
			
	input_window = Tk()
	input_window.title("Anime Synopsis")
	input_window.configure(background="black")

	#label1
	Label(input_window, text="For which anime would you like to find the Synopsis?\n", bg="black", fg="white", font="none 12 bold" ).grid(row=3,column=0,sticky=N+S+E+W)
	#entry_box_name
	textentry = Entry(input_window, width=20, bg="white")
	textentry.grid(row=4, column=0,sticky=N+S+E+W)
	#submit button
	Button(input_window, text="Submit", width=6, command=input_function).grid(row=5, column=0,sticky=W)

	#mainloop for input window
	input_window.mainloop()

when_called()

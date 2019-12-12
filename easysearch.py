#EasySearch
#IOTECH SOFTWARE

import os
import sys
import thread
from Tkinter import *
from engine import engine



class Main:
	#here we declare our search string as a global variable
	#and set it to a string object lastly seting it to an empty string
	# and declare a variable search which will contain the string to be
	#passed to the search engine
	global src_str
	global search
	#src_str = StringVar()
	
	def __init__(self,title):
		self.win = Tk()
		self.title = title
	
	def CONSTRUCT_WINDOW(self):
		# in here we initialize the main window
		self.win.config(bg="white")
		self.win.geometry("600x300+350+150")
		self.win.attributes("-toolwindow",True)
		self.win.title(self.title)
		self.win.maxsize(600,300)
		self.win.minsize(600,300)
		
		#we now construct the menu bar
		menu = Menu(self.win,bg="#000000")
		self.win.config(menu=menu)
		settings = Menu(menu)
		about = Menu(menu)

		menu.add_cascade(label="Settings",menu=settings)
		settings.add_command(label="Configure",command=Config().configurewin)
		menu.add_cascade(label="Help",menu=about)
		about.add_command(label="About",command=About().ini)
		
		#PROGRAM INITIALIZER
		INI(self.win).INITIALIZE()
	
		
	def INITIALIZE_WINDOW(self):
		# the main window is crreated here
		self.win.mainloop()

class SearchEngine:
	# used to be the original engine class but moved the engine to a separate class file
	def __init__(self,file_name,progress_bar):
		self.file_name = file_name
		self.progress_bar = progress_bar
		
		
	def Search(self):
		#print self.file_name
		engine.SearchEngine(self.file_name,True,None,self.progress_bar).Search() # we now call the engine
			
class Crawl:
	# here we call the engine
	def __init__(self,data,progress_bar):
		self.search = data # this is the file name to be passed to the engine 
		self.progress_bar = progress_bar 

	def InCraw(self):
		#print self.search.get()
		def search_thread(threadName,delay):
			SearchEngine(self.search.get(),self.progress_bar).Search() # here we pass the file name to the engine
		thread.start_new_thread(search_thread,("Crawl",0)) # thread that starts the engine
class INI:
	#Finaly we initialize the programe here
	global src_str
	src_str=""

	def __init__(self,win):
		self.win = win
		
	def Cancel(self):
		
		pass
		
	def INITIALIZE(self):
		# here we create and initialize our objects 
		header = Label(self.win,text="Easy Search",bg="#008F51",fg="white",font="shruti 19 bold")
		header.pack(fill=BOTH)
		Progress = Label(self.win,text="",bg="white",fg="black",font="Shrutil 10")
		Progress.place(x=120,y=99)
		search = Entry(self.win,border=2,relief=GROOVE,textvariable=src_str)
		search.config(width=39,relief=GROOVE,font="Arial 13")
		search.place(x=125,y=180)
		search.focus()
		src_btn = Button(self.win,text="Search",width=10,font="Arial 8 bold",bg="#008F51",fg="white",border=1,relief=GROOVE,command=Crawl(search,Progress).InCraw)
		src_btn.place(x=260,y=210)
		self.win.mainloop()

class About:
	# this is the about class that will display info about the software
	def about(self):
		win2 = Tk()
		win2.config(bg="white")
		win2.title("")
		win2.attributes("-toolwindow",True)
		win2.geometry("600x440+350+150")
		win2.maxsize(600,440)
		win2.attributes("-topmost",True)
		win2.attributes("-alpha",0.91)
		frame=Frame(win2)
		topL=Label(frame,text="Easy Search",font="shruti 25 bold",bg="#90EE90",height=1).pack(fill=BOTH,anchor=CENTER,expand=True)
		Label(frame,text="Version 1.0",font="Shrutil 9 italic",bg="#90EE90",).place(x=210,y=45)
		
		info='''
		easy search is a fast search engine for searching any
		file document on your computer system with over
		95% accuracy this eliminates getting other search
		results that have nothing to do with your search on
		the default search programs and also eliminates
		false positives which are files and or shortcuts cached
		from external drives or files that have been deleted
		
		the default engine comes with a security feature that
		restricts it to only search from the current logged on user
		as this eliminates access to vital system files
		
		
		Author: Tanaka Chinengundu
		Email: tanakah30@gmail.com
		site: https://github.com/TaqsBlaze
		
		follow on twitter:@taqs_blaze
		'''
		Label(frame,text=info,font="shruti 10").pack(anchor="sw")
		frame.pack(fill=BOTH,anchor=CENTER,expand=True)
	def ini(self):
		About().about()
		
class Config:
    def configurewin(self):
       from engine import configwindow
Main("EasySearch").CONSTRUCT_WINDOW() # here we create but do not initialize the main window


#Search engine
#By Tanaka Chinengundu
#version:1.0.0


import os
import sys
import thread
import time
import threading
from threading import *


class SearchEngine:
	
	def __init__(self,file_name,search_ini,search_complite,progress_bar):
		self.file_name = file_name
		self.search_ini = search_ini
		self.search_complite = search_complite
		self.engine_config = {"Restricted":True,"Threads":1}
		self.progress_bar = progress_bar
	def Search(self):
		global search
		global target_dir
 		global search
 		global get_current_user
		os.system("ECHO %USERPROFILE% >CRAWL.txt")
		get_current_user=open("CRAWL.txt",'r').read()
		target_dir = get_current_user
		new_line_removed=target_dir.replace("\n","")
		space_removed=new_line_removed.replace(" ","")
		target_dir = space_removed
		print target_dir
		search=Work(self.file_name,target_dir,self.progress_bar)
		search.start()
		search.join()
		
class Work(Thread):
	def __init__(self,file_name,dir,progress_bar):
		self.file_name = file_name
		self.target_dir = dir
		self.progress_bar = progress_bar
		Thread.__init__(self)
		self.daemon = True
		
				
	def run(self):
		#while True:
		for root,folder,files in os.walk(target_dir):
			try:
								# we are removing directories which users do not users
								# to make our search faster
				if "AppData" in folder:
					folder.remove("AppData")
				
			except Exception, e:
				print e
				pass
			try:
				if ".AndroidStudio3.4" in folder:
					folder.remove(".AndroidStudio3.4")
			except:
				pass
			try:
				if ".vscode" in folder:
					folder.remove(".vscode")
			except:
				pass
			for filez in files:
								# now we are searching for the file
				if filez.startswith(self.file_name) or filez.endswith(self.file_name) or self.file_name in files or self.file_name in filez:
					#print "[+]File found..."
					#print os.path.join(root,self.file_name)
					self.progress_bar.config(text="[+]File Found:\n" + os.path.join(root,self.file_name))
					self.search_ini = False
					self.seach_complite = True
					#print "Opening file location.."
					os.system("explorer {}".format(root))
					thread.exit()
					time.sleep(10)
					#os.system("cls")
					break
				else:
					pass
							# we are looping in files	
				#print "[+]Searching...."
				#print os.path.join(root,filez)
				self.progress_bar.config(text="[+]Searching:\n" + os.path.join(root,filez))
				time.sleep(0.000001)
				#os.system("cls")
		
		#this loop will start threads
		
		thrd=0
		
		'''
		while(self.search_ini == True and self.search_complite == None):
			
		
			thread.start_new_thread(inner_thread,("search{}".format(thrd),5))
			thrd=thrd+1
		'''
		
		thread.exit()
		thread.exit()
class Stop:
	def Stop(self):
		thread.exit()
		thread.exit()
def main():
	search=Work()
	search.start()
	search.join()
 
#main()
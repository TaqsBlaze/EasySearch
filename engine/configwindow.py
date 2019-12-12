from Tkinter import *
from Tkconstants import *
import ttk
import os,sys,threading
	
window = Tk()
window.config(bg="#67C66F")
window.title("Configuration Settings")
window.geometry("550x350+310+110")
window.attributes("-toolwindow",True)

row = 0
while row < 50:
	window.rowconfigure(row,weight=2)
	window.columnconfigure(row,weight=2)
	row += 1
		
menu = ttk.Notebook(window)
menu.grid(row=0,column=0,columnspan=60,rowspan=50,sticky='NESW')

tab1 = ttk.Frame(menu)
tab2 = ttk.Frame(menu)
tab3 = ttk.Frame(menu)
		
menu.add(tab1,text='Global config')
menu.add(tab2,text='Feed back')
menu.add(tab3,text='Developer',state=DISABLED)





frame = Frame(tab1)
frame.config(bg="white")
frame.pack(fill=BOTH,anchor='se',expand=True)
frame_Note = 	Frame(frame)
font = "shrutil 8"
color="white"
value = IntVar()
Restricted = IntVar(value=1)
threads = IntVar()
Shell = IntVar(value=1)
Logs = IntVar()
Auto_start = IntVar()
Auto_update = IntVar()
dev_mode = Checkbutton(frame,text="Developer mode",font=font,variable=value,bg="white",state=DISABLED)
engine = Checkbutton(frame,text="Restricted" ,font=font,variable=Restricted,state=DISABLED,bg="white")
shell = Checkbutton(frame,text="Intergrate with system shell",font=font,bg="white",variable=Shell,state=DISABLED)
auto = Checkbutton(frame,text="Start on system boot",font=font,bg=color,variable=Auto_start)
User_log = Checkbutton(frame,text="Send crush logs",font=font,bg=color,variable=Logs)
Update  = Checkbutton(frame,text="Auto update",font=font,bg=color,variable=Auto_update)
dev_mode.pack(anchor='sw')
engine.pack(anchor='sw')
shell.pack(anchor='sw')
auto.pack(anchor='sw')
User_log.pack(anchor='sw')
Update.pack(anchor="sw")
Threads = Scale(frame,label="Threads",
						command=None,
						variable=threads,from_=1,to=4,
						length=200,orient=HORIZONTAL,bg=color).pack(anchor='sw')

NOTE="NOTE:"
Follow_up='''
The first 3 options are available for developers only and the Restricted
option will not be availabel for the time being for security reasons it is
advazable to keep it at restricted 
if for any reasons the Restricted option is enabled and unchecked it is
adviable not to use the software in that instans and report to the 
developer team
'''
frame_Note.pack(side="bottom",fill='x')
note = Label(frame_Note,text=Follow_up,bg='#67C66F',font=font).pack(anchor=CENTER,fill='x')





class Config_INI:
	def INITIALIZE(self):
		try:
			FRAME = Frame()
			FRAME.config(bg="white",width =20,height=15)
			Label(FRAME,text='Setting up configuration settings for the first time',font='shrutil 13 italic',bg='white',fg='black')
			FRAME.pack(anchor='center',fill=BOTH)
			os.system("echo %USERNAME%>user.ini")
			user_config=open("user.ini",'r').read()
			print user_config[:]
			os.makedirs("C:\Users\\{}\\search\\config\\default".format(user_config[:]))
		except Exception,e:
				print e
		
	
#Config_INI().INITIALIZE()			
window.mainloop()

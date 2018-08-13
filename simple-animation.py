from Tkinter import *
import random
import time

app = Tk()

def create_rects():
	rect = w.create_rectangle(0, 575, 300, 600, fill='black')
	rect2 = w.create_rectangle(400, 575, 600, 600, fill='black')
	w.pack()

def update_circ():
	time.sleep(0.001)
	w.move(rect, 0, -1)
	w.move(rect2, 0, -1)
	if(w.coords(rect)[1]==10):
		w.coords(rect, 0, 575, random.randrange(20, 580), 600)
	if(w.coords(rect2)[1]==10):
		w.coords(rect2, w.coords(rect)[2] + 100, 575, 600, 600)
	app.update_idletasks()
	app.update()

def keyUp(a_boolean):
	while(a_boolean):
		w.move(circ, 0, -1)
		update_circ()
		if(w.coords(circ)[0]==0.0 or w.coords(circ)[1]==0.0 or
		   w.coords(circ)[2]==600.0 or w.coords(circ)[3]==600.0):
			a_boolean = False
	
def keyDown(a_boolean):
	while(a_boolean):
		w.move(circ, 0, 1)
		update_circ()
		if(w.coords(circ)[0]==0.0 or w.coords(circ)[1]==0.0 or
		   w.coords(circ)[2]==600.0 or w.coords(circ)[3]==600.0):
			a_boolean = False
	
def keyLeft(a_boolean):
	while(a_boolean):
		w.move(circ, -1, 0)
		update_circ()
		if(w.coords(circ)[0]==0.0 or w.coords(circ)[1]==0.0 or
		   w.coords(circ)[2]==600.0 or w.coords(circ)[3]==600.0):
			a_boolean = False
	
def keyRight(a_boolean):
	while(a_boolean):
		w.move(circ, 1, 0)
		update_circ()
		if(w.coords(circ)[0]==0.0 or w.coords(circ)[1]==0.0 or
		   w.coords(circ)[2]==600.0 or w.coords(circ)[3]==600.0):
			a_boolean = False

def callback(event):
	frame.focus_set()

app.bind('<Left>', lambda x: keyLeft(True))
app.bind('<Right>', lambda x: keyRight(True))
app.bind('<Up>', lambda x: keyUp(True))
app.bind('<Down>', lambda x: keyDown(True))
w = Canvas(app, height=600, width=600)
circ = w.create_oval(20, 20, 40, 40, fill='black')
rect = w.create_rectangle(0, 575, 300, 600, fill='black') # Randomize Later
rect2 = w.create_rectangle(400, 575, 600, 600, fill='black')
w.pack()
#create_rects()
app.mainloop()
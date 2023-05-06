from fileinput import filename
import tkinter as tk
from tkinter import filedialog, mainloop


def browseFiles():
	filedialog.askopenfilename(initialdir = "saved notes", title = "Select a Note", filetypes = (("notes","*.jpg*"), ("all files","*.*")))
	
def mn():
	window = tk.Tk()
	window.title("Note Storage")
	window.geometry("350x350")
	window.config(background="red")
	
	note_explorer = tk.Label(window, text = "Note Databse", bg = "olive", padx=20, pady=10)
	note_explorer.place(x=135,y=20)
	
	button_explore = tk.Button(window, text = "Browse Notes", command = browseFiles, padx = 15, pady = 15)
	button_explore.place(x=118, y=170)
	
	button_exit = tk.Button(window,	text = "Exit", command = exit, padx = 15, pady = 10)
	button_exit.place(x=142, y=230)

	window.mainloop()

if __name__ == '__mn__':
	mn()
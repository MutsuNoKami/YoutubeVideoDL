import tkinter as tk 
import os
from tkinter import font 
import tkinter.font as tkfont
import youtube_dl
from tkinter import *
from tkinter.ttk import *

root=tk.Tk()
root.title("Youtube Video Downloader")
root.geometry('400x400')
root.resizable(height=False,width=False)

canvas=Canvas(root,height=400,width=400,bg='#000000​')
canvas.pack()

bold_font=tkfont.Font(family='Helvetica' ,size=12, weight="bold")
label1=tk.Label(root,text="Enter the URL" ,width=12 , height=2,bg="#FFFFFF​")
label1.config(font=bold_font)
canvas.create_window(200,100,window=label1)

download_entry=tk.Entry(root)
canvas.create_window(200,140,window=download_entry)

def get_video_url():
    search_item=download_entry.get()
    ydl_opts={
        'format':'best',
        'noplaylist':True,
        'extract-audio':True,
    }
    # Download Directory set 
    os.chdir(r"C:\Users\Admin\Videos\Clips")
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_item])

    bold_font2=tkfont.Font(family="Helvetica",size=11,weight="bold")
    label2=tk.Label(root,text="Video Downloaded" ,width=20, bg ="#263d42​")
    label2.config(font=bold_font2)
    canvas.create_window(200,300,window=label2)

download=tk.Button(text="Download",padx=5,pady=5,fg="white" ,bg="DeepSkyBlue",command=get_video_url)
canvas.create_window(200,250,window=download)
root.mainloop()

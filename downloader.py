#import youtube_dl for download the vedio 
# import tkinter for GUI
from __future__ import unicode_literals
import youtube_dl  
from tkinter import * 
from tkinter import ttk
from tkinter import filedialog 


#fun for download 
def DownloadVideo():
    #get the type of vedio(mp4/mp3)
    choice = ytdchoices.get()
    #get link in url
    url = ytdEntry.get()

    # two condition 
    if (choice==choices[1]):#user want mp3 file this part run 
     
           ydl_opts = {
          'format': 'bestaudio/best',
         'postprocessors': [{
           'key': 'FFmpegExtractAudio',
           'preferredcodec': 'mp3',
           'preferredquality': '320',
          }],
    }
           with youtube_dl.YoutubeDL(ydl_opts) as ydl:
               ydl.download([url])
               print("Task Successful Done...!")

        
    
    elif(choice==choices[0]):#user wants mp4 file this part run
         
            ydl_opts = {
            'format': 'mp4'
     }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                print("Task Successful Done...!")
               


#front-end code

root = Tk()
root.title("Mp3 Converter")#title

root.geometry("350x400") #layout
root.columnconfigure(0,weight=1)

ytdLabel= Label(root,text="Enter the Link of vedio",font=("jost",15)) #print the statement 
ytdLabel.grid()

ytdEntryVar = StringVar()# get the string type input(link)
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()



#print statement for vedio type
ytdQuality = Label(root,text="Select Quality",font=("jost",15))
ytdQuality.grid()
#get input for type of file
choices = ["MP4","Only Audio"]
ytdchoices = ttk.Combobox(root,values=choices) #get value 
ytdchoices.grid()
#download button 
downloadbtn = Button(root,text="Donwload",width=10,bg="red",fg="white",command=DownloadVideo)
downloadbtn.grid()


root.mainloop()

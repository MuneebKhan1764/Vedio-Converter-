from __future__ import unicode_literals
import youtube_dl
print("Press 'Y' for Mp3 format")
print("press 'N' for Mp4 format")
type=input("")

if (type=="y"):
  print("Insert the link for Mp3")
  link = input ("")
  ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
  }

  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
       ydl.download([link])

       print("Task Successful Done...!")

      
     
     
elif(type!="y"):
     print("For Mp4 format")
     print("Insert the link for Mp4")
     link = input ("")
     ydl_opts = {
    'format': 'mp4'
   
    
  }
     
     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
          ydl.download([link])
          print("Task Successful Done...!")
          
          
          
          
          
          
#Updated code 
#get input through GUI
from __future__ import unicode_literals
import youtube_dl
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


Folder_Name = ""

def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="Please Choose Folder!!",fg="red")


def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()


    if (choice==choices[1]):
     #print("Insert the link for Mp3")
     # link = input ("")
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

        
    
    elif(choice==choices[0]):
         #print("For Mp4 format")
          # print("Insert the link for Mp4")
          # link = input ("")
            ydl_opts = {
            'format': 'mp4'
     }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                print("Task Successful Done...!")
               




root = Tk()
root.title("Mp3 Converter")

root.geometry("350x400")
root.columnconfigure(0,weight=1)

ytdLabel= Label(root,text="Enter the Link of vedio",font=("jost",15))
ytdLabel.grid()

ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()




ytdQuality = Label(root,text="Select Quality",font=("jost",15))
ytdQuality.grid()

choices = ["MP4","Only Audio"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()

downloadbtn = Button(root,text="Donwload",width=10,bg="red",fg="white",command=DownloadVideo)
downloadbtn.grid()


root.mainloop()




      
     
     

     




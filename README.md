# YouTube MP3 Downloader
A python tool that let you download videos and convert to mp3 a YouTube video

## Install
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install youtube-dl.  
```bash
pip install youtube-dl
```

```
On windows ones instead, you will need to download the [last build](https://ffmpeg.org/download.html#build-windows)  
At this point copy the 3 files you can find on bin folder, and paste them in the main Python's scripts folder  
![alt text](https://i.ibb.co/gmJZ1zC/aaaaaa.png)

## Info
youtube-dl will be used to download the video from youtube  
ffmpeg will convert them to mp3

## Setup
In the first part of the code, we will need to import unicode_literals from __future__ and import youtube_dl and tkinter for GUI
We want to make the person using the tool to choose the youtube video's link directly in the console, and not in the code, we will make that by declaring a variable named link, which will take the user's input when the tool is runned.
```python
from __future__ import unicode_literals
import youtube_dl
from tkinter import * 
from tkinter import ttk
from tkinter import filedialog 
```


## YTDL Options
We need to specify all the options for the video, like the quality, the codec, etc...  
We will download our video with the maximum quality and in a mp3 format  
```python
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}
```

## Download and convert
```python
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
```

## Code
So our code will look like:
```python
from __future__ import unicode_literals
import youtube_dl
from tkinter import * 
from tkinter import ttk
from tkinter import filedialog 

 if (choice==choices[1]):#user want mp3 file this part run 
     
           ydl_opts = {
          'format': 'bestaudio/best',
         'postprocessors': [{
           'key': 'FFmpegExtractAudio',
           'preferredcodec': 'mp3',
           'preferredquality': '320',
          }],
    }
  }

  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
       ydl.download([link])




For Mp4    



 elif(choice==choices[0]):#user wants mp4 file this part run
         
            ydl_opts = {
            'format': 'mp4'
     }
     
     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
          ydl.download([url])
          print("Task Successful Done...!")

for GUI 
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



....

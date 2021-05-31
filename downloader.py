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
     


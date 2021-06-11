from tkinter import *
from pytube import YouTube
#Create Display Window
root = Tk() #Tk() used to initialize tkinter to create display window
root.geometry('500x400') #geometry() used to set the window’s width and height
#root.resizable(0,0) #resizable(0,0) set the fix size of window
root.title("CodezWord Youtube Downloader") #title() used to give the title of window

Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack() #Label() widget use to display text that users can’t able to modify.root is the name of the window.text which we display the title of the label.font in which our text is written.pack organized widget in block.
#Create Field to Enter Link
link = StringVar() #link is a string type variable that stores the youtube video link that the user enters.
Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90) #Entry() widget is used when we want to create an input text field.textvariable used to retrieve the value of current text variable to the entry widget.
#Create Function to Start Downloading
def Downloader():
    url =YouTube(str(link.get())) #Url variable gets the youtube link from the link variable by get() function and then str() will convert the link in string datatype.
    video = url.streams.first() #The video is download in the first present stream of that video by stream.first() method.
    video.download() # It will download video in project file
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 480 , y = 210)
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'light blue', padx = 2, command = Downloader).place(x=180 ,y = 150) #Button() widget used to display button on the window.
root.mainloop() #root.mainloop() is a method that executes when we want to run the program.
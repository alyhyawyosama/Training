# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 05:29:53 2023

@author: Asama
"""
import youtube_dl 
import pytube 

def YoutubeVideoDownloader(url, res):
    video = pytube.YouTube(url)
    stream = video.streams[res]
    stream.download()
    return stream.default_filename


def facebookVideoDownloard(link):
    print("Is it a public video? ")
    print("1. Yes")
    print("2. No")
    res = input()
    try:
        if res == '1':
            print("Downloading ...")
            with youtube_dl.YoutubeDL({}) as y:
                y.download([link])
            print("Download Complete!")
        else:
            print("Private video can't download")
    except:
        print("There is an error. Please Run again")
        





#youtube
choice = input("Do want to download : \n\t1-Youtube video\n\t2-Facebook video\n\t Enter:")
url = input("Enter url:")

if choice == "1":
    choice2 = input("choose the quality \n1- 144\n2- 360\n3- 720 \nEnter:")
    try:
        if choice2 == "1":
            YoutubeVideoDownloader(url,0)
            print("Video downloaded succefully")
        elif choice2 == "2" :    
            YoutubeVideoDownloader(url,1)
            print("Video downloaded succefully")
        elif choice2 == "3":
            print("Video downloaded succefully")
            YoutubeVideoDownloader(url,2)
        else:
            print("Error")
    except:
        print("There is an error. Please Run again")
        
elif choice == "2":
    try:
        facebookVideoDownloard(url)
    except:
        print("There is an error. Please Run again")
else :
    print("Error")
    
    


    

'''





if(quality=="MP4 360"):
         con = pt.YouTube(get_link).streams[1].download()

    elif(quality=="MP4 144"):
         con = pt.YouTube(get_link).streams[0].download()  

    elif(quality=="MP4 720"):
         con = pt.YouTube(get_link).streams[2].download()    
    else:
        messagebox.showerror("Download","Something Went Wrong")
        
'''
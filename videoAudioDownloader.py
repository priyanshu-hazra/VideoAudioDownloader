# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 21:02:57 2017

@author: priyanshu
"""
"""
Using this Script videos,audios can be downloaded from various sites like facebook,
youtube,9gag,Soundcloud etc 
Follow the Commands in the console
Make changes as neccesary
suggest changes at :- contactme@priyanshuhazra.tk / priyanshu.hazra95@gmail.com

Run this script inside a blank folder with no other files /audios/videos
The Files will be saved in C:/Downloads

The following Script is in python 3.5
"""

## add subclip audio later 
import youtube_dl
import os
import shutil
import moviepy.editor as mp
import imageio


def convertAudio(title):
    try:
        imageio.plugins.ffmpeg.download()
        titlemp3=title+".mp3"
        #print(title1)
        title+=".mp4"
        clip = mp.VideoFileClip(title)
        #print(title)
        clip.audio.write_audiofile(titlemp3)
        clip='c'
        os.remove(title)
    except:
        source=os.listdir(cwd) #takes all the files in the directory mentioned 
        for files in source:
            if files.endswith(".mp4"):
                print("input some other name: ")
                nameTitle=input()
               # nameTitle+=".mp4"
                os.rename(files,nameTitle)
                break
        titlemp3=nameTitle+".mp3"
        #print(title1)
        #nameTitle+=".mp4"
        clip = mp.VideoFileClip(nameTitle)
       # print(title)
        clip.audio.write_audiofile(titlemp3)
        clip='c'
        os.remove(nameTitle)

def downloadSingleVideo(linkAddress,quality_value):
    if quality_value==1:
            
        options = {'outtmpl': '%(title)s.mp4',
                   'format':'best[height<1080]/best'}  # save file as the Title
                   
    elif quality_value==2:
        options = {'outtmpl': '%(title)s.mp4',
                   'format':'worst'} 
        
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([linkAddress])
        #convertAudio("Adele - Hello")
        
    

def downloadAudio(linkAddress,quality_value):
    #extract tile
    ydl = youtube_dl.YoutubeDL()
    r = None
    url = linkAddress
    with ydl:
        r = ydl.extract_info(url, download=False)  # don't download, much faster 
    title=r['title']
    
    #title extracted
    if quality_value ==1:
        if "www.youtube.com" in linkAddress:
            #sending options as dicitionaries 
            options = {'outtmpl': '%(title)s.mp4',
                   'format':'best[height<1080]/best'}
        
        else:
            
            options = {
            'format': 'bestaudio/best', # choice of quality
            'extractaudio' : True,      # only keep the audio
            'audioformat' : "mp3",      # convert to mp3 
            'outtmpl': '%(title)s.mp3',        # name the file the ID of the video
            'noplaylist' : True,        # only download single song, not playlist
            }
    else: #if quality is 2
        if"www.youtube.com" in linkAddress:
             options = {'outtmpl': '%(title)s.mp4',
                   'format':'worst'} 
        else:
            options = {
            'format': 'worstaudio/worst', # choice of quality
            'extractaudio' : True,      # only keep the audio
            'audioformat' : "mp3",      # convert to mp3 
            'outtmpl': '%(title)s.mp3',        # name the file the ID of the video
            'noplaylist' : True,        # only download single song, not playlist
            }
    

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([linkAddress])
    if "www.youtube.com" in linkAddress:
        convertAudio(title)
   
   # convertAudio(title) ##to convert the audio to mp3
        
def downloadPlaylist(linkAddress,quality):
    if quality==1:
        options = {'outtmpl': '%(title)s.mp4',
                   'noplaylist':False,
                   'format':'best'}  # save file as the Title
                   
    elif quality==2: #low quality
        options = {'outtmpl': '%(title)s.mp4',
                   'noplaylist':False,
                   'format':'worst'}
                   
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([linkAddress])
    

def main():
    print('Enter choicce \n 1.Download Video(Eg -facebook,youtube \n 2.Download Audio(Eg-Soundcloud etc\n 3.Download Entire PlayList(Eg- youtube')
    choice=int(input('Enter Choice : '))
    quality_value=int(input('Enter Quality : \n 1-High Quality \n 2-Low Quality \nEnter Choice :'))
    
    
    if choice==1:
        print('Enter the video Link- right click and copy link address from the website ')
        linkAddress=input()
        downloadSingleVideo(linkAddress,quality_value)
    elif choice==2:
        print('Enter the audio link (right click and copy link address )')
        linkAddress=input()
        downloadAudio(linkAddress,quality_value)
    elif choice==3:
        print('Enter the playlist link')
        linkAddress=input()
        downloadPlaylist(linkAddress,quality_value)

imageio.plugins.ffmpeg.download()#CHECK FOR FFMPEG DOWNLOAD
cwd=os.getcwd()
#print(cwd)     #current working directory
final_directory = os.path.join(cwd, r'\Downloads') #directory c:\Downloads
#print(final_directory)
#for downloads inside  final_directory\Downloads=os.path.join(cwd,'Downloads')
if not os.path.exists(final_directory): #create folder if not created
    os.makedirs(final_directory)
    

#for files in source:
#    if files.endswith(".mp4"):
#        shutil.move(os.path.join(cwd,files), os.path.join(final_directory,files))

main()
while(True):   
    #move to downlload directory
    source=os.listdir(cwd) #takes all the files in the directory mentioned 
    for files in source:
        if files.endswith(".mp4"):
            shutil.move(os.path.join(cwd,files), os.path.join(final_directory,files))
    
        if files.endswith(".mp3"):
            shutil.move(os.path.join(cwd,files), os.path.join(final_directory,files))   
    
           
    print("\n**************\nTHE FILES ARE SAVED AT C:\Downloads\n**************")
    x=(int(input('Press 1 to continue else any other key to exit')))
    if x==1:
        main()
    else:
        break
    
    

    



from cProfile import label
from cgitb import text
from re import A
import tkinter as tk
from unicodedata import name
import myproject2 as mw
from tkinter.font import BOLD
import webbrowser
import playsound
from spacy import language
#from markupsafe import te
from gtts import gTTS
import os
import requests
from newsapi import NewsApiClient
#global xwindow
def my1():
  xwindow2 = tk.Tk()
  xwindow2.geometry('800x900')
#xwindow.resizable(0,0)
  xwindow2['background']='black'
  url="https://newsapi.org/v2/top-headlines?country=in&apiKey=b39ee"
  global news
  news=requests.get(url).json()
  label=[1,2,3,4,5,6,7,8,9,10]
  ce=tk.Label(xwindow2, text="Top Headlines", font=("Helvetica", 30,"bold"),bg="black",fg="red")
  ce.config(anchor=tk.CENTER)
  ce.pack()
  for j in range(10):
    articles=news['articles'][j]['title']
    des=news['articles'][j]['description']
    label[j]=tk.Label(xwindow2, text="", font=('Calibri 15'),
      bg="black",fg="white")
    label[j].config(text=str(j+1)+"."+articles )
    label[j].pack()
  label[0].bind("<Button-1>",lambda e:webbrowser.open(news['articles'][0]['url']))
  label[1].bind("<Button-1>",lambda e:webbrowser.open(news['articles'][1]['url']))
  label[2].bind("<Button-1>",lambda e:webbrowser.open(news['articles'][2]['url']))
  label[3].bind("<Button-1>",lambda e:webbrowser.open(news['articles'][3]['url']))    
  label[4].bind("<Button-1>",lambda e:webbrowser.open(news['articles'][4]['url']))
  label[5].bind("<Button-1>",lambda e:webbrowser.open(news['articles'][5]['url']))
  label[6].bind("<Button-1>",lambda e:webbrowser.open(news['articles'][6]['url']))
  label[7].bind("<Button-1>",lambda e:webbrowser.open(news['articles'][7]['url']))
  label[8].bind("<Button-1>",lambda e:webbrowser.open(news['articles'][8]['url']))
  label[9].bind("<Button-1>",lambda e:webbrowser.open(news['articles'][9]['url']))

  labelm=tk.Label(xwindow2, text="", font=("Arial Narrow",20,"bold"),
      bg="black",fg="#FFDF00")
  labelm.config(text="Live News Marathi")
  labelm.pack(anchor="w")
  labelm.bind("<Button-1>",lambda e:webbrowser.open("https://marathi.abplive.com/live-tv"))
  labelm=tk.Label(xwindow2, text="", font=("Arial Narrow",20,"bold"),
      bg="black",fg="#FFDF00")
  labelm.config(text="Live News Hindi")
  labelm.pack(anchor="e")
  labelm.bind("<Button-1>",lambda e:webbrowser.open("https://news.abplive.com/live-tv"))

  labelm=tk.Label(xwindow2, text="", font=("Arial Narrow",20,"bold"),
      bg="black",fg="#FFDF00")
  labelm.config(text="Live News English")
  labelm.pack(anchor="s")
  labelm.bind("<Button-1>",lambda e:webbrowser.open("https://www.indiatoday.in/livetv"))


  b1=tk.Button(xwindow2,font=('arial' ,20),text="Next",fg="white",bg="#16F529",command=lambda:close(xwindow2))
  b1.pack(side=tk.RIGHT)
  b2=tk.Button(xwindow2,font=('arial' ,20),text="Search",fg="white",bg="#16F529",command=lambda:close2(xwindow2))
  b2.pack(side=tk.BOTTOM)
  b3=tk.Button(xwindow2,font=('arial' ,20),text="read",fg="white",bg="#16F529",command=loud)
  b3.pack(side=tk.LEFT)

  xwindow2.mainloop()
def close(xwindow2):
  
  xwindow2.destroy()
  mw.my2()
def close2(xwindow2):
  xwindow2.destroy()
  mw.ser()
def loud():
  strl=[0,1,2,3,4,5,6,7,8,9]
  Str=" "
  for j in range(10):
    strl[j]="\n\n\t\t  Headline no "+str(j+1)+" is   "+news['articles'][j]['title']
  aloud=''.join([str(elem) for elem in strl])
  aloud2=Str+aloud
  language='en'
  myobj=gTTS(text=aloud2,lang=language,slow=False)
  myobj.save("welcome.mp3")
  playsound.playsound('F:/python/newspaper/welcome.mp3',True)
  print(aloud2)

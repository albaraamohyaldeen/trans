from tkinter import *
import pygame
from gtts import gTTS

tk = Tk()
tk.title('Robot')
tk.geometry('688x1111')
tk.resizable(False,False)
tk.configure(bg = 'white')

#صورة الروبوت

img_robot=PhotoImage(file='imgs/Robot.png')

#متغير تحويل الكلمات إلى أصوات

def audio():
 text = entry_text.get()
   
 gt = gTTS(f'{text}')
 gt.save('audio.mp3')
  
 pygame.init()
 pygame.mixer.music.load('audio.mp3')
 pygame.mixer.music.play()
  
 while pygame.mixer.music.get_busy():
   continue
     
 
 pygame.quit()
 
#عنوان الملف

label_t = Label(tk,width=66,font=('Tajawal',12),text='ترجمة الكلمات إلى أصوات',bg='#2f6141',fg='#fff',bd=1,relief=SOLID,cursor='hand2')
label_t.place(x=1,y=1)

#إطار الروبوت

fr_robot = Frame(tk,width=688,bg='white',height=966)
fr_robot.place(x=1,y=45)

robot = Button(fr_robot,width=688,font=('Tajawal',26),bg='white',bd=0,height=988,text='Robot',image=img_robot)
robot.place(x=1,y=45)

label_text = Label(tk,width=10,font=('Tajawal',19),bg='white',bd=0,text='enter a text:')
label_text.place(x=1,y=662)

#حقل إدخال الكلمات

entry_text = Entry(tk,width=26,font=('Tajawal',14),bd=1,relief=SOLID,cursor='hand2',fg='black')
entry_text.place(x=188,y=666)

supmit = Button(tk,width=6,font=('Tajawal',12),bg='purple',bd=1,relief=SOLID,cursor='hand2',fg='black',height=1,text='supmit',command=audio)
supmit.place(x=188,y=716)




tk.mainloop()

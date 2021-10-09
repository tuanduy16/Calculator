from tkinter import *
import tkinter as tk
import math
main=tk.Tk()
main.title('Calculator')
main.resizable(0,0)
text_display=''
first=0
second=0
action=''

def number_press(event):
    global text_display
    press=event.widget['text']
    if press!='0' or (press=='0' and text_display!=''):
        text_display+=press
    else:
        text_display=''
    display()
def display():
    screen.delete(0, 'end')
    if text_display=='':
        screen.insert(0,'0')
    else:
        screen.insert(0, text_display)
def action_press(event):
    global first
    first=float(screen.get())
    global text_display
    text_display=''
    global action
    action=event.widget['text']
    global dotpress
    dotpress=False
def finish_press(event):
    global second, text_display, action
    second=float(screen.get())
    if action=='+':
        result=first+second
    elif action=='-':
        result=first-second
    elif action=='*':
        result=first*second
    elif action=='/':
        if second!=0:
            result=first/second
        else:
            result='NaN'
    else:
        result='NaN'
    screen.delete(0,'end')
    screen.insert(0, result)
    text_display=''
    global dotpress
    dotpress=False
    action=''
def clear_press(event):
    global text_display, first, second, action
    clear=event.widget['text']
  
    text_display=''
    first=0
    second=0
    action=''
    display()
def clear_e_press(event):
    global text_display
    if action=='':
        clear_press(event)
    else:
        text_display=''
        display()
def back_press(event):
    global text_display
    if text_display=='':
        return
    text_display=screen.get()
    text_display=text_display[:-1]
    display()
def reverse_press(event):
    global text_display
    if text_display!='':
        num=float(text_display)
        num=-num
        text_display=str(num)
        display()
dotpress=False
def  dot_press(event):
    global dotpress
    if dotpress:
        return 
    global text_display
    if text_display=='':
        text_display='0'
    text_display+='.'
    display()
    dotpress=True
def x_press(event):
    global action, text_display
    act=event.widget['text']
    if act=='%':
        if action!='':
            num=float(text_display)
            num=num/100
            text_display=str(num)
            display()
        else:
            text_display=''
        display()
    elif act=='1/x':
        num=float(screen.get())
        if num!=0:
            num=1/num
            text_display=str(num)
            display()
        else:
            screen.delete(0,'end')
            screen.insert(0,'NaN')
        text_display=''
    else:
        num=float(screen.get())
        num=math.sqrt(num)
        text_display=str(num)
        display()
        text_display=''
        
def memory_press(event):
    global text_display
    global memory
    act=event.widget['text']
    if act=='MS':
        memory=float(screen.get())
    elif act=='MR':
        text_display=str(memory)
        display()
        text_display=''
    elif act=='M+':
        memory+=float(screen.get())
    elif act=='M-':
        memory-=float(screen.get())
    else:
        memory=0
        
screen = tk.Entry(main, font=('Times New Roman', 17), justify=RIGHT) 
screen.grid(row=0, column=0, columnspan=5, padx=5, pady=5, ipadx=5, ipady=5, sticky=W+E)
screen.insert(0,'0')
keyboard={'MC':0, 'MR':0, 'MS':0, 'M+':0, 'M-':0, '<-':6,'CE':5,'C':4, '+/-':7,'sqrt':9,'7':1,
          '8':1,'9':1, '/':2,'%':9,'4':1,'5':1,'6':1,'*':2,'1/x':9,'1':1,'2':1,'3':1,'-':2,'=':3,'0':1,'':0,'.':8,'+':2}
row=1
keys=list(keyboard.keys())
for i in range(len(keys)):
    if i==26:
        continue
    if i%5==0 and i!=0:
        row+=1
    if i==24:
        btn=tk.Button(main, text=keys[i], width=5, height=6)
        btn.grid(row=row, column=i%5, rowspan=2, padx=5, pady=8)
    elif i==25:
        btn=tk.Button(main, text=keys[i], width=13,height=2)
        btn.grid(row=row, column=i%5, columnspan=2, padx=5, pady=5)
    else:
        
        btn=tk.Button(main, text=keys[i], width=5,height=2)
        btn.grid(row=row, column=i%5, padx=5, pady=5)
    if keyboard[keys[i]]==1:
        btn.bind('<Button-1>',number_press)
    elif keyboard[keys[i]]==2:
        btn.bind('<Button-1>',action_press)
    elif keyboard[keys[i]]==3:
        btn.bind('<Button-1>',finish_press)
    elif keyboard[keys[i]]==4:
        btn.bind('<Button-1>',clear_press)
    elif keyboard[keys[i]]==5:
        btn.bind('<Button-1>',clear_e_press)
    elif keyboard[keys[i]]==6:
        btn.bind('<Button-1>',back_press)
    elif keyboard[keys[i]]==7:
        btn.bind('<Button-1>',reverse_press)
    elif keyboard[keys[i]]==8:
        btn.bind('<Button-1>',dot_press)
    elif keyboard[keys[i]]==9:
        btn.bind('<Button-1>',x_press)
    else:
        btn.bind('<Button-1>',memory_press)
        
        
main.mainloop()

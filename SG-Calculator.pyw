"""
====== GUI Design By: Sancho Godinho (https://github.com/sancho1952007/Modern-GUI-v3.0) ======
====== Images By: Flaticon (https://flaticon.com) ======

\\ Please Do Not Delete the files Folder!

\\ Please Do Not Clear This Comment!

\\ You Are Allowed to Customize this Script.

\\ If you want to share this script or Customize and share: You Should Keep this complete comment with it.

"""

from tkinter.messagebox import *
from bs4 import BeautifulSoup
from tkinter.font import *
from tkinter import *
import requests
import os
path=os.path.dirname(os.path.realpath(__file__))+"\\"
app=Tk()
app.iconbitmap(path+'files/icon.ico')
app.overrideredirect(True)
app.config(bg="#d3d3d3")
app.config(bd=1)
app.attributes('-alpha', 0.9)

with open(path+'files\\location', 'r') as readLoc:
    pos=readLoc.read().split('x')
    x_pos=''.join(pos[0])
    y_pos=''.join(pos[1])
    app.geometry(f"+{x_pos}+{y_pos}")
    readLoc.close()

def qut(): # Quit Function (Exit)
    with open(path+'files\\location', 'w+') as write_loc:
        write_loc.write(str(app.winfo_x())+'x'+str(app.winfo_y()))
        write_loc.close()
        app.destroy()

def bksp():
    new=main.get()[:-1]
    clear()
    insert(new)

def insert(num):
    main['state']=NORMAL
    main.insert(END, num)
    main['state']=DISABLED

def clear():
    main['state']=NORMAL
    main.delete(0, END)
    main['state']=DISABLED

def calc():
  try:
    out=eval(main.get())
    clear()
    insert(out)
  except:
      showerror('Error', 'Please Enter Valid Number/Operator')

def detect_key_press(event):
    if event.keysym=="F1":
        qut()
    
    elif event.keysym=="Escape":
        clear()

    elif event.keysym=="1":
        insert(1)
    elif event.keysym=="2":
        insert(2)
    elif event.keysym=="3":
        insert(3)
    elif event.keysym=="4":
        insert(4)
    elif event.keysym=="5":
        insert(5)
    elif event.keysym=="6":
        insert(6)
    elif event.keysym=="7":
        insert(7)
    elif event.keysym=="8":
        insert(8)
    elif event.keysym=="9":
        insert(9)
    elif event.keysym=="0":
        insert(0)
    elif event.keysym=='plus':
        insert('+')
    elif event.keysym=='minus':
        insert('-')
    elif event.keysym=='asterisk':
        insert('*')
    elif event.keysym=='slash':
        insert('/')

    elif event.keysym=='BackSpace':
        bksp()
    elif event.keysym=='Return' or event.keysym=='equal':
        calc()

def enter_close(event):
    close.config(image=close2)

def leave_close(event):
    close.config(image=close1)

def move(event):
    half1=str(app.winfo_width()/2)
    half2=half1.split('.')
    half=half2[0]
    app.geometry(f"+{event.x_root-int(''.join(half))}+{event.y_root-7}")

close1=PhotoImage(file=path+"files\\close-1.png")
close2=PhotoImage(file=path+"files\\close-2.png")

Top=Frame(app, bd=2, bg="grey")
close=Button(Top, image=close1, bg="grey", bd=0,command=qut)
close.grid(row=0, column=0)

title=Label(Top, text="SG-Calculator", bg="grey", font=("Comic Sans MS", 12))
title.place(anchor=CENTER, relx=0.5, rely=0.5)
Top.pack(fill=X, side='top')

root=Frame(app, bd=2, bg='#d3d3d3')


def update():
  try:
    web=BeautifulSoup(requests.get('https://sancho1952007.github.io/SG-Calculator/Update.html').text, 'html.parser')
    updat=web.find('div', class_='update-latest-version').text
    with open(path+'files\\version', 'r') as ver:
        if updat==ver.read():
            showinfo('No Update' ,'You Are Using The Latest Version!')
        else:
            upd_sure=askyesno('Update Available', 'Update Available!\nDo You Want to Update?')
            if upd_sure:
                os.system('start '+web.find('div', class_='URL').text)
  except:
      showerror('Network Error', 'Please Connect Your Device to A Wifi Networ to Check For Updates...')


main=Entry(root, width="39", state=DISABLED)
main.grid(columnspan=40)

# Buttons Clear, BackSpace
Button(root, text="Clear", width="10", height='2', command=lambda: clear()).grid(row=1, column=0)
Button(root, text="Updates", width="10", height='2', command=lambda: update()).grid(row=1, column=1)
Button(root, text="⌫", width="10", height='2', command=lambda: bksp()).grid(row=1, column=2)

# Buttons 1,2,3
Button(root, text="1", width="10", height='2', command=lambda: insert(1)).grid(row=2, column=0)
Button(root, text="2", width="10", height='2', command=lambda: insert(2)).grid(row=2, column=1)
Button(root, text="3", width="10", height='2', command=lambda: insert(3)).grid(row=2, column=2)

# Buttons 4,5,6
Button(root, text="4", width="10", height='2', command=lambda: insert(4)).grid(row=3, column=0)
Button(root, text="5", width="10", height='2', command=lambda: insert(5)).grid(row=3, column=1)
Button(root, text="6", width="10", height='2', command=lambda: insert(6)).grid(row=3, column=2)

# Buttons 7,8,9
Button(root, text="7", width="10", height='2', command=lambda: insert(7)).grid(row=4, column=0)
Button(root, text="8", width="10", height='2', command=lambda: insert(8)).grid(row=4, column=1)
Button(root, text="9", width="10", height='2', command=lambda: insert(9)).grid(row=4, column=2)

# Buttons +,0,-
Button(root, text="-", width="10", height='2', command=lambda: insert('-')).grid(row=5, column=0)
Button(root, text="0", width="10", height='2', command=lambda: insert(0)).grid(row=5, column=1)
Button(root, text="+", width="10", height='2', command=lambda: insert('+')).grid(row=5, column=2)

# Butons *,/
Button(root, text="*", width="10", height='2', command=lambda: insert('*')).grid(row=6, column=0)
Button(root, text="/", width="10", height='2', command=lambda: insert('/')).grid(row=6, column=1)
Button(root, text="=", width="10", height='2', command=lambda: calc()).grid(row=6, column=2)

root.pack()

#Bindings
app.attributes("-topmost", True)
app.bind("<Key>", detect_key_press)
close.bind("<Enter>", enter_close)
close.bind("<Leave>", leave_close)
Top.bind("<B1-Motion>", move)
title.bind("<B1-Motion>", move)


app.protocol('WM_DELETE_WINDOW', qut)
app.mainloop()

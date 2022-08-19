import tkinter as tk
import subprocess
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import ttk

def call_doo():
        subprocess.Popen(r'C:\Windows\System32\DXDiag.exe')

def call_foo():
        subprocess.Popen(r'C:\Windows\System32\SystemPropertiesAdvanced.exe',shell = True)

def call_boo():
        subprocess.Popen(r'"C:\Windows\System32\rundll32.exe" shell32.dll,Control_RunDLL desk.cpl,,0',shell = True)

def call_woo():
        subprocess.Popen(r'C:\Windows\System32\msdt.exe -id NetworkDiagnosticsWeb')

def call_goodbye():
        root.destroy()

root = Tk()
root.title('わすれた時のSHELL1.2')
root.minsize(400, 400)

style = ttk.Style()
style.theme_use('classic')

# Frame as widget container
frame1 = ttk.Frame(root,padding=(20,20,20,20))
frame1.grid()

# Image_1
icon_image = PhotoImage(file='./img/dx.png')

# Label 1
label1 = ttk.Label(frame1,image=icon_image,padding=(20))
label1.grid(row=0, column=0)

# Label 1_2
label1_2 = ttk.Label(frame1,text='ドライバー機能している？',padding=(20)) # (left, top, right, bottom)
label1_2.grid(row=0, column=2)

# button 1
button1 = ttk.Button(frame1, text='DirectX_Check_Tool',command=call_doo,padding=[20,20,20,20])
button1.grid(row=0, column=1)

# Image_2
icon_image_2 = PhotoImage(file='./img/sys.png')

# Label 2
label2 = ttk.Label(frame1,image=icon_image_2,padding=(20))
label2.grid(row=1, column=0)

# Label 2_1
label2_1 = ttk.Label(frame1,text='PATHの編集？',padding=(20)) # (left, top, right, bottom)
label2_1.grid(row=1, column=2)

# button 2
button2 = ttk.Button(frame1, text='環境変数', command=call_foo , padding=[20,20,20,20])
button2.grid(row=1, column=1)

# Image_3
icon_image_3 = PhotoImage(file='./img/raptop.png')

# Label 3
label2 = ttk.Label(frame1,image=icon_image_3,padding=(20))
label2.grid(row=2, column=0)

# Label 3_1
label2_1 = ttk.Label(frame1,text='ゴミ箱きえた?',padding=(20)) # (left, top, right, bottom)
label2_1.grid(row=2, column=2)

# button 3
button3 = ttk.Button(frame1, text='デスクトップのアイコン', command=call_boo , padding=[20,20,20,20])
button3.grid(row=2, column=1)

# Image_4
icon_image_4 = PhotoImage(file='./img/net.png')

# Label 4
label4 = ttk.Label(frame1,image=icon_image_4,padding=(20))
label4.grid(row=3, column=0)

# Label 4_1
label4_1 = ttk.Label(frame1,text='ネットワークを確認する？',padding=(20)) # (left, top, right, bottom)
label4_1.grid(row=3, column=2)

# button 4
button4 = ttk.Button(frame1, text='トラブルシューティング', command=call_woo , padding=[20,20,20,20])
button4.grid(row=3, column=1)

# Image_5
icon_image_5 = PhotoImage(file='./img/yubi.png')

# Label 5
label5 = ttk.Label(frame1,image=icon_image_5,padding=(20))
label5.grid(row=4, column=0)

# Label 5_1
label5_1 = ttk.Label(frame1,text='終了する？',padding=(20)) # (left, top, right, bottom)
label5_1.grid(row=4, column=2)

# button 5
button5 = ttk.Button(frame1, text='Exit', command=call_goodbye , padding=[20,20,20,20])
button5.grid(row=4, column=1)

root.mainloop()
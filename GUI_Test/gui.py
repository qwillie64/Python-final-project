import tkinter as tk


#fuction
def enter():#搜尋函式
    print("rsdad")



win=tk.Tk()  #建立主視窗
win.title("sex music")#標題
win.geometry("520x400")#大小
win.resizable(False,False)#禁止縮放
win.iconbitmap("oshinoko.ico")#icon
enterbtn=tk.Button(text="確定")#搜尋按鈕
enterbtn.pack()
enterbtn.config(command=enter)


win.mainloop()  #常駐主視窗




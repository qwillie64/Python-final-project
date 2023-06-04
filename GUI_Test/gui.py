import tkinter as tk


#fuction
def enter():#搜尋函式
    
    label.set(pp)
    author.set(pp)
    link.set(pp)
    t=serchentry.get()
    print(t)
    



pp=[6,9,6,9,6,6,6,6,6,6,6,6,6,6,6,6,6,6]
win=tk.Tk()  #建立主視窗
win.title("serch music")#標題
win.geometry("500x700")#大小
win.resizable(False,False)#禁止縮放
win.iconbitmap("oshinoko.ico")#icon
enterbtn=tk.Button(text="確定")#搜尋按鈕
lbserch=tk.Label(text="在下面輸入你想要的曲風or音樂類型")#標籤
lbserch.config(font="微軟正黑體 14")
serchentry=tk.Entry()#輸入框
serchentry.config(width=45)#輸入框寬度
#用來顯示結果的字串
musiclabel=tk.Label(text="音樂標題:",font="微軟正黑體 14")
musicauthor=tk.Label(text="作曲家:",font="微軟正黑體 14")
musiclink=tk.Label(text="音樂連結:",font="微軟正黑體 14")
labelframe = tk.Frame(win, width=15)        # 建立 Frame
authorframe = tk.Frame(win, width=15)        # 建立 Frame
linkframe = tk.Frame(win, width=15)        # 建立 Frame
label = tk.StringVar()#存放音樂標題
author = tk.StringVar()#存放作者

link = tk.StringVar()#存放連結
labelscroll = tk.Scrollbar(labelframe)         # 將 Frame 裡放入 Scrollbar
labelscroll.pack(side='right')
authorscroll = tk.Scrollbar(authorframe)
authorscroll.pack(side='right')
linkscroll = tk.Scrollbar(linkframe)
linkscroll.pack(side='right')
# 在 Frame 中加入 Listbox 元件，設定 yscrollcommand=scrollbar.set
labellistbox = tk.Listbox(labelframe,  listvariable=label, height=6, width=30, yscrollcommand=labelscroll.set)
labelscroll.config(command=labellistbox.yview)
authorlistbox = tk.Listbox(authorframe,  listvariable=author, height=6, width=30, yscrollcommand=authorscroll.set)
authorscroll.config(command=authorlistbox.yview)
linklistbox = tk.Listbox(linkframe,  listvariable=link, height=6, width=60, yscrollcommand=linkscroll.set)
linkscroll.config(command=linklistbox.yview)


#布局
lbserch.pack(side="top")
serchentry.pack(side="top")
enterbtn.pack(side="top")
enterbtn.config(command=enter)
musiclabel.pack(anchor="w")
labelframe.pack(anchor="w")
labellistbox.pack(side='left', fill='x')
musicauthor.pack(anchor="w")
authorframe.pack(anchor="w")
authorlistbox.pack(side='left', fill='x')
musiclink.pack(anchor="w")
linkframe.pack(anchor="w")
linklistbox.pack(side='left', fill='x')


win.mainloop()  #常駐主視窗




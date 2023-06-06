import tkinter as tk
import tkinter.ttk as ttk

import tools.WebScutter as ws
import tools.TextProcess as tp

_font_label = "微軟正黑體 14"
_font_textbox = "微軟正黑體 12"


# search function
def search():
    keyword = serchentry.get()
    try :
        results = ws.search_spotify(keywords=keyword)
    finally(Exception e) :
        print(str(e))

    print(results)
    # add_treeview()



def add_treeview():
    tree.insert()


# windows form
form = tk.Tk()
form.title("Music finder")  # title
form.geometry("800x600")  # form size
form.resizable(True, True)  # resizable = false
form.iconbitmap("oshinoko.ico")  # icon

# search button
button_search = tk.Button(form, text="Search", command=search)
button_search.config(font=_font_label)

# label (for search button)
label_search = tk.Label(form, text="請在下面輸入你想要搜尋的曲風/音樂類型")
label_search.config(font=_font_label)

# input textbox
serchentry = tk.Entry(form)  # bording
serchentry.config(font=_font_textbox, width=55)  # size

# results treeview
tree = ttk.Treeview(form, columns="songs", show="tree headings")
tree.heading("0", text="Inddex")
tree.heading("songs", text="Title")
tree.heading("songs", text="Artist")
tree.heading("songs", text="link")


# layout
label_search.pack(side="top")
serchentry.pack(side="top")
button_search.pack(side="top")


tree.place(relx=0.005, rely=0.4, relwidth=0.99, relheight=0.595)
if __name__ == "__main__":
    form.mainloop()  # 常駐主視窗

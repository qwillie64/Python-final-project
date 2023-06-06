import tkinter as tk
import tkinter.ttk as ttk

import tools.WebScutter as ws
import tools.TextProcess as tp

_font_label = "微軟正黑體 14"
_font_textbox = "微軟正黑體 12"


# search function
def search():
    keyword = serchentry.get()
    ws.setting(5, 0.5, 1, True)
    results = ws.search_spotify(keyword)

    add_treeview(results)


def add_treeview(data: list):
    i = 0
    for d in data:
        if len(d) < 3:
            continue
        tree.insert(
            "", "end", text=str(i), values=(str(i), str(d[0]), str(d[1]), str(d[2]))
        )
        i += 1


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
tree = ttk.Treeview(form, columns=["0", "1", "2", "3"], show="headings")
tree.column("0", width=20, anchor="c")
tree.column("1", anchor="c")
tree.column("2", anchor="c")
tree.column("3", anchor="c")
tree.heading("0", text="Inddex")
tree.heading("1", text="Title")
tree.heading("2", text="Artist")
tree.heading("3", text="link")

# layout
label_search.pack(side="top")
serchentry.pack(side="top")
button_search.pack(side="top")

p_x = 0.008
m_y = 0.4
tree.place(relx=p_x, rely=m_y, relwidth=1 - 2 * p_x, relheight=1 - m_y - p_x)

if __name__ == "__main__":
    form.mainloop()  # 常駐主視窗

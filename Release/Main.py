import tkinter as tk
import tkinter.ttk as ttk

import tools.WebScutter as ws
import tools.TextProcess as tp

import threading
import time

_font_label = "微軟正黑體 14"
_font_textbox = "微軟正黑體 12"
_fint_log = "微軟正黑體 8"


# search function
def search():
    button_search.config(state="disabled")
    textbox_input.config(state="readonly")

    t = threading.Thread(target=thread)
    t.start()

    button_search.config(state="normal")
    textbox_input.config(state="normal")


def add_treeview(data: list):
    i = 0
    for d in data:
        if len(d) < 3:
            continue
        tree.insert(
            "", "end", text=str(i), values=(str(i), str(d[0]), str(d[1]), str(d[2]))
        )
        i += 1


def add_log(message):
    listbox_log.insert(tk.END, message)


def select_treeview(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        v = item["values"]
        ws.open_google(v[len(v) - 1])


def thread():
    keyword = textbox_input.get()
    ws.setting(10, 0.5, 1.2, True, False, add_log)
    results = ws.search_spotify(keyword)
    add_treeview(results)


# windows form
form = tk.Tk()
form.title("Music finder")  # title
form.geometry("800x600")  # form size
form.resizable(False, False)  # resizable = false
form.iconbitmap("oshinoko.ico")  # icon

# search button
button_search = tk.Button(form, text="Search", command=search)
button_search.config(font=_font_label)

# label (for search button)
label_search = tk.Label(form, text="請在下面輸入你想要搜尋的曲風/音樂類型")
label_search.config(font=_font_label)

# input textbox
textbox_input = tk.Entry(form)  # bording
textbox_input.config(font=_font_textbox, width=55)  # size

# log frame
frame_log = tk.Frame(form, width=50, pady=5, height=8)

# scroll (for log listbox)
scroll_log = tk.Scrollbar(frame_log)

# log listbox
listbox_log = tk.Listbox(frame_log, width=50, height=8, yscrollcommand=scroll_log.set)
listbox_log.config(font=_fint_log)

# results treeview
tree = ttk.Treeview(form, columns=["0", "1", "2", "3"], show="headings")
tree.bind("<Double-1>", select_treeview)
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
textbox_input.pack(side="top")
button_search.pack(side="top")
frame_log.pack(side="top", anchor="e")
scroll_log.pack(side="right")
listbox_log.pack(side="top", fill="x")

p_x = 0.008
m_y = 0.4
tree.place(relx=p_x, rely=m_y, relwidth=1 - 2 * p_x, relheight=1 - m_y - p_x)

if __name__ == "__main__":
    form.mainloop()  # 常駐主視窗

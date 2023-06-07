import tkinter as tk
import tkinter.ttk as ttk

import tools.WebScutter as ws
import tools.TextProcess as tp

import threading


_font_label = "微軟正黑體 14"
_font_textbox = "微軟正黑體 12"
_font_log = "微軟正黑體 9"


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
    amount = int(textbox_amount.get())
    speed = float(textbox_speed.get())

    if (amount <= 0) | (amount > 10000):
        amount = 10

    if (speed < 0) | (speed > 1):
        speed = 0.5

    ws.setting(amount, (2.0 - 0.0) * speed, (3.0 - 0.6) * speed, True, False, add_log)
    results = ws.search_spotify(keyword)
    add_treeview(results)


# windows form
form = tk.Tk()
form.title("Music finder")  # title
form.geometry("800x600")  # form size
form.resizable(False, False)  # resizable = false
# form.iconbitmap("oshinoko.ico")  # icon

# search button
button_search = tk.Button(form, text="Search", command=search)
button_search.config(font=_font_label)

# label (for search button)
label_search = tk.Label(form, text="請在下面輸入你想要搜尋的曲風/音樂類型")
label_search.config(font=_font_label)

# label (for amount textbox)
label_amount = tk.Label(form, text="Quantity : ")
label_amount.config(font=_font_log)

# input amount textbox
textbox_amount = tk.Entry(form)  # bording
textbox_amount.config(font=_font_log, width=10)  # size

# label (for speed textbox)
label_speed = tk.Label(form, text="Speed : ")
label_speed.config(font=_font_log)

# input speed textbox
textbox_speed = tk.Entry(form)  # bording
textbox_speed.config(font=_font_log, width=10)  # size

# input keyword textbox
textbox_input = tk.Entry(form)  # bording
textbox_input.config(font=_font_textbox, width=55)  # size

# log frame
frame_log = tk.Frame(form, width=50, height=7)

# scroll (for log listbox)
scroll_log = tk.Scrollbar(frame_log)

# log listbox
listbox_log = tk.Listbox(frame_log, width=48, height=7, yscrollcommand=scroll_log.set)
listbox_log.config(font=_font_log)

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
p_x = 0.008
m_y = 0.4

label_search.pack(side="top")
textbox_input.pack(side="top")
button_search.pack(side="top")
label_amount.place(relx=p_x, rely=0.17)
textbox_amount.place(relx=p_x + 0.13, rely=0.17)
label_speed.place(relx=p_x, rely=0.21)
textbox_speed.place(relx=p_x + 0.13, rely=0.21)
frame_log.place(relx=0.55, rely=0.17)
scroll_log.pack(side="right")
listbox_log.pack(side="left")

tree.place(relx=p_x, rely=m_y, relwidth=1 - 2 * p_x, relheight=1 - m_y - p_x)

if __name__ == "__main__":
    textbox_amount.insert(0, "20")
    textbox_speed.insert(0, "0.4")

    form.mainloop()  # 常駐主視窗

#モジュールをインポート
from cgitb import text
from logging import warning
import tkinter
from tkinter import ttk
from tkinter import messagebox


def default ():
    print("情報ウィンドウを表示")
    if title_entry.get() == "" and content_entry.get() == "":
        print("入力されていません")
        messagebox.showerror(title="【致命的】エラー", message="【エラー】\n内容が入力されていません\n内容を入力してください")
        
    else:
        return "ok"


#情報ウィンドウ
def info_window ():
    what = default()
    if what == "ok":
        messagebox.showinfo(title = title_entry.get(), message = content_entry.get(),)

def warn_window ():
    what = default()
    if what == "ok":
        messagebox.showwarning(title = title_entry.get(), message = content_entry.get(),)

def error_window ():
    what = default()
    if what == "ok":
        messagebox.showerror(title = title_entry.get(), message = content_entry.get(),)

#ウィンドウを閉じる
def window_close ():
    print("ウィンドウを閉じます")
    which = messagebox.askyesno(
        title = "アプリ終了選択",
        message = "アプリを終了しますか?"
    )
    if which == True:
        window.destroy()
    elif which == False:
        messagebox.showinfo(title="アプリ終了選択", message = "まだまだ楽しみましょう!")

def enabled ():
    btn2.destroy()
    btn1.config(state = "normal")
    worn.config(state = "normal")
    error.config(state = "normal")





#ウィンドウを生成
window = tkinter.Tk()

#タイトルを追加
window.title("メッセージボックス生成器")
window.iconbitmap("images/favicon.ico")

window.config(bg = "#C7E1FE")
window.resizable(0,0)
def a ():
    print("a")
window.protocol('WM_DELETE_WINDOW', True)
#ウィンドウのサイズを追加
window.geometry("1024x576")

label1 = ttk.Label(
    text = "メッセージボックス生成器",
    font = ("sans-serif", 20, "bold"),
    background = "#C7E1FE"
)
label1.pack()

btn1 = ttk.Button(
    text = "情報ウィンドウ",
    padding = 10,
    command = info_window,
    state= "disabled" 
)
btn1.pack()

worn = ttk.Button(
    text = "警告ウィンドウ",
    command = warn_window,
    padding = 10,
    state = "disabled"
)
worn.pack()


error = ttk.Button(
    text = "エラーウィンドウ",
    command = error_window,
    padding = 10,
    state = "disabled"
)

error.pack()


btn2 = ttk.Button(
    text = "利用規約を読み\n上のボタンを有効にする",
    state = "normal",
    command = enabled,
)

btn2.pack()

title_label = ttk.Label(
    text = "タイトルを入力",
    padding = 5
)
title_label.pack()
title_entry = ttk.Entry()
title_entry.pack()

content_label = ttk.Label(
    text = "内容を入力",
    padding = 5
)
content_label.pack()

content_entry = ttk.Entry()
content_entry.pack()

btn_close = ttk.Button(
    text = "終了する",
    padding = 10,
    command = window_close,
)
btn_close.pack()
#ウィンドウを表示
window.mainloop()


#-*- coding: utf8 -*-
import sys
import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()

# ウインドウのタイトルを定義する
root.title(u'Entryを使ってみる')

# ここでウインドウサイズを定義する
root.geometry('400x300')

# ボタンが押されたら呼び出される関数
def deleteEntry(event):
    # Entryの中身をすべて削除します
    Entry1.delete(0, tk.END)

def showMessage(text):
    #値を表示
    Entry1_value = Entry1.get()
    print(Entry1_value)
    tkm.showinfo('info', text)

# ラベルを使って文字を画面上に出す
Static1 = tk.Label(text=u'▼　Entryだぞ！　▼')
Static1.pack()

# Entryを出現させる
Entry1 = tk.Entry(width=50)                   # widthプロパティで大きさを変える
Entry1.insert(tk.END, u'挿入する文字列')        # 最初から文字を入れておく
Entry1.pack()

# Entryの値を取得してみる
Entry1_value = Entry1.get()
print(Entry1_value)

# Buttonを設置してみる（文字を表示するボタン）
Show_Button = tk.Button(text=u'何か起こるボタン', width=20, command=lambda: showMessage(Entry1.get()))        # 関数に引数を渡す場合は、commandオプションとlambda式を使う
Show_Button.pack()

# リストボックスを設置してみる
ListBox1 = tk.Listbox(width=55, height=14)
ListBox1.pack()

root.mainloop()

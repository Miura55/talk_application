#-*- coding: utf8 -*-
import sys
import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()

# ウインドウのタイトルを定義する
root.title(u'Entryを使ってみる')

# ここでウインドウサイズを定義する
root.geometry('400x300')
# ボタンが押されたらリストボックスに、Entryの中身を追加
def addList(text):
    mysay = 'you: ' + text
    print(mysay)
    ListBox1.insert(tk.END, mysay)


# ラベルを使って文字を画面上に出す
Static1 = tk.Label(text=u'▼　Entryだぞ！　▼')
Static1.pack()


# Entryを出現させる
Entry1 = tk.Entry(width=50)                   # widthプロパティで大きさを変える
Entry1.insert(tk.END, u'挿入する文字列')        # 最初から文字を入れておく
Entry1.pack()


# Buttonを設置してみる
Button1 = tk.Button(text=u'追加するテキスト', width=50, command=lambda: addList(Entry1.get()))        # 関数に引数を渡す場合は、commandオプションとlambda式を使う
Button1.pack()


# リストボックスを設置してみる
ListBox1 = tk.Listbox(width=55, height=14)
ListBox1.pack()

root.mainloop()

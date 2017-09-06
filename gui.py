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

# Buttonを設置してみる
Button1 = tk.Button(text=u'何も起こらないボタン', width=20)
Button1.bind("<Button-1>", deleteEntry)
Button1.pack()

# Buttonを設置してみる
Button2 = tk.Button(text=u'何も起こらないボタン', width=20, command=lambda: showMessage(Entry1.get()))        # 関数に引数を渡す場合は、commandオプションとlambda式を使う
Button2.pack()

root.mainloop()

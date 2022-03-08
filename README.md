日本語(Japanese) / [英語(English)]() (←Please wait for a while until opening)

# メッセージボックス生成器 (GUI)
メッセージボックス生成器を作ります!!(import tkinter)

# 作り方!!↓

## 1. PythonでTkinterをインポートします

```python

#tkinterをインポート
import tkinter
```
## 2. ウィンドウを作る

```python
#Windowにtkinterデータを格納
window = tkinter.TK()

#Windowが一瞬で閉じないようにループさせる
window.mainloop()
```

## 3. その他をインポート

```python

#デザインをよくするttkをインポート
from tkinter import ttk

#メッセージボックスをインポート
from tkinter import messagebox

```

## 4. 色々決める!(語彙力...)

```python

import tkinter
from tkinter import ttk
from tkinter import massagebox

window = tkinter.TK()

#ウィンドウのタイトルを決める
window.title("メッセージボックス生成器")

#ウィンドウのサイズを決める (16:9を何倍かしたものにした)
window.geometry("1024x576")

window.mainloop()
```

## 5. いよいよボタンを設置

```python
window = tkinter.TK()

#Btn1という変数にボタンデータを格納
btn1 = ttk.Button(
  #ボタンのテキストを決める
  text = "frfre",
  
  #パディングを決める
  padding = 10

)

window.mainloop()

```

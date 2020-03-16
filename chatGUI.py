#!/usr/bin/env python

# -*- coding: UTF-8 -*-
import tkinter as tkinter
from PIL import Image,ImageTk

# 创建窗体
win = tkinter.Tk()
# 设置窗体大小
win.geometry("300x480")
win.title("路人甲")
win.configure(bg="black")
# win.iconbitmap("图标文件")
win.resizable(False, False)

# 创建标题头
topFrame = tkinter.Frame(height=40, bg='yellow', width=300).place(y=0)

# 创建内容框
contentFrame = tkinter.Frame(height=390, bg='pink', width=300).place(y=40)

# 创建frame
bottomFrame = tkinter.Frame(height=60, bg='green', width=300)
# 创建标签
# img = Image.open()
# photo = ImageTk.PhotoImage(img)
# chatImage = tkinter.PhotoImage(file="C:/Users/S-ZHU/Desktop/timg.jpg")
chatImage = [ImageTk.PhotoImage(Image.open("C:/Users/S-ZHU/Desktop/1.png")),
             ImageTk.PhotoImage(Image.open("C:/Users/S-ZHU/Desktop/1.png")),
             ImageTk.PhotoImage(Image.open("C:/Users/S-ZHU/Desktop/1.png")),
             ImageTk.PhotoImage(Image.open("C:/Users/S-ZHU/Desktop/1.png"))]


imgLabel1 = tkinter.Label(bottomFrame, image=chatImage[0]).place(y=0, x=20)
imgLabel2 = tkinter.Label(bottomFrame, image=chatImage[1]).place(y=0, x=40)
imgLabel3 = tkinter.Label(bottomFrame, image=chatImage[2]).place(y=0, x=60)
imgLabel4 = tkinter.Label(bottomFrame, image=chatImage[3]).place(y=0, x=80)


# labchat = tkinter.Button(contentFrame,
#                          height=2,
#                          width=10,
#                          relief='sunken',
#                          bd=0,
#                          font='楷体',
#                          ).place(y=420)
bottomFrame.place(y=420)

win.update()

# 进入消息循环体
win.mainloop()


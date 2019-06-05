import tkinter as tk
from tkinter import IntVar
import webbrowser


def VipCrack():
    if v.get() == 1:
        url = "http://jx.598110.com/?url="
        userUrl = t1.get(0.0, "end")
        url = url+userUrl
        webbrowser.open(url)
    if v.get() == 2:
        url = "http://jx.du2.cc/?url="
        userUrl = t1.get(0.0, "end")
        url = url + userUrl
        webbrowser.open(url)

    if v.get() == 3:

        url = "http://jx.drgxj.com/?url="
        userUrl = t1.get(0.0, "end")
        url = url + userUrl
        webbrowser.open(url)

ifae = tk.Tk()
ifae.geometry("400x400")
ifae.title("VIP Crack QQ联系1069071702")

tk.Label(ifae, text="请复制浏览器地址到下方", font=("宋体", 16)).place(x=0, y=50)
t1 = tk.Text(ifae, width=50, height=1)
t1.place(x=10, y=80)

v=IntVar()
tk.Radiobutton(ifae, variable=v, value=1, text="高速通道1").place(x=10, y=100)
tk.Radiobutton(ifae, variable=v, value=2, text="高速通道2").place(x=140, y=100)
tk.Radiobutton(ifae, variable=v, value=3, text="普通通道1").place(x=270, y=100)

tk.Scale(ifae, from_=100, to=1).place(x=10, y=150)
tk.Scale(ifae, from_=600, to=1).place(x=50, y=150)
tk.Label(ifae, text="音量     亮度").place(x=30, y=256)

tk.Button(ifae, text="破解", width=20, height=5, font=("仿宋", 20), command=VipCrack).place(x=130, y=150)
tk.Label(ifae, text="开通高速通道请联系QQ，加载更快更高清").place(x=5, y=320)
ifae.mainloop()


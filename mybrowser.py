import tkinter as tk
import webbrowser
root = tk.Tk()
root.title("Infinity")
root.geometry("400x150")
x = tk.StringVar()

def fb():
    webbrowser.open_new("www.facebook.com")
def yt():
    webbrowser.open_new("www.youtube.com")
def ig():
    webbrowser.open_new("www.insta.com")
def tw():
    webbrowser.open_new("www.twitter.com")
def search():
    word = x.get()
    search = "https://www.google.com/search?q="+word
    webbrowser.open_new(search)

x = tk.StringVar()
b1 = tk.Button(root,text="Facebook",fg="White",bg="#3b5998",command=fb)
b2 = tk.Button(root,text="Youtube",fg="White",bg="#FF0000",command=yt)
b3 = tk.Button(root,text="Instagram",fg="White",bg="#C13584",command=ig)
b4 = tk.Button(root,text="Twitter",fg="White",bg="#00acee",command=tw)
b5 = tk.Button(root,text="Search",fg="White",bg="#202020",command=search)
b1.place(x=10,y=70,height=30,width=120)
b2.place(x=140,y=70,height=30,width=120)
b3.place(x=270,y=70,height=30,width=120)
b4.place(x=40,y=105,height=30,width=320)
b5.place(x=320,y=10,height=50,width=70)
e1 = tk.Entry(root,textvariable=x)
e1.place(x=10,y=10,width=300,height=50)
root.mainloop()
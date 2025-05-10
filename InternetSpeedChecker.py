from tkinter import *
import speedtest

def speedCheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3)) + "Mbps"
    up = str(round(sp.upload()/(10**6),3)) + "Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

root = Tk()
root.title("Internet Speed Test")
root.geometry("500x500")
root.config(bg="black")

lab = Label(root,text="Internet Speed Test",font=("Times New Roman",25,"bold")).place(x=60,y=30,height=50,width=380)

lab = Label(root,text="Download Speed",font=("Times New Roman",20,"bold"),fg="white",bg="black").place(x=100,y=130,height=50,width=280)
lab_down = Label(root,text="00",font=("Times New Roman",15,"bold"))
lab_down.place(x=100,y=180,height=40,width=280)
lab = Label(root,text="Upload Speed",font=("Times New Roman",20,"bold"),fg="white",bg="black").place(x=100,y=270,height=50,width=280)
lab_up = Label(root,text="00",font=("Times New Roman",15,"bold"))
lab_up.place(x=100,y=320,height=40,width=280)

btn = Button(root,text="Check Speed",font=("Times New Roman",20,"bold"),relief=RAISED,bg="Red",command=speedCheck).place(x=150,y=400,height=50,width=180)

root.mainloop()
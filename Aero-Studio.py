import _tkinter
from tkinter import *
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import requests


root= Tk()
root.title("Aero-Studio")
root.geometry("800x500+400+100")
root.resizable(False,False)
root.geometry("+0+0")

task_list=[]

def deleteTask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open('tasklist.txt', "w") as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete(ANCHOR)


def addTask():
    task=taks_entry.get()
    taks_entry.delete(0,END)

    if task:
        with open('tasklist.txt','a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)

    


def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks=taskfile.readlines()
    
        for task in tasks:
            if task in tasks:
                if task !='\n':
                    task_list.append(task)
                    listbox.insert(END,task)
    except:
        file=open('task.list.txt','w')
        file.close()

#icon
Image_icon=PhotoImage(file=r"C:\Users\Admin\Desktop\fizyka\Aera Studio\Aerostudio,py\task.png")
root.iconphoto(False,Image_icon)

#Top Bar
TopImage=PhotoImage(file=r"C:\Users\Admin\Desktop\fizyka\Aera Studio\Aerostudio,py\topbar.png")
Label(root,image=TopImage).pack()

dockImage=PhotoImage(file=r"C:\Users\Admin\Desktop\fizyka\Aera Studio\Aerostudio,py\dock.png")
Label(root,image=dockImage,bg ="#32405b"). place(x=700,y=25)

heading=Label(root, text="ALL TASK", font="arial 20 bold", fg='white',bg="#32405b")
heading.place(x=325,y=20)

#main
frame=Frame(root,width=700, height=50, bg="white")
frame.place(x=50, y=180)

task=StringVar()
taks_entry=Entry(frame, width=700, font='arial 20', bd=0)
taks_entry.place(x=50, y=7)

button=Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=addTask)
button.place(x=600, y=0)


#listbox
frame1=Frame(root, bd=3, width=1000, height=280, bg="#32405b")
frame1.pack(pady=(160,0))

listbox= Listbox(frame1, font=('arial', 12), width=700, height=16, bg="#32405b", fg="white", cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


openTaskFile()

#Delete
Delete_icon = PhotoImage(file=r"C:\Users\Admin\Desktop\fizyka\Aera Studio\Aerostudio,py\delete.png")
delete_button = Button(frame, image=Delete_icon, bd=0, command=deleteTask)
delete_button.pack(side=BOTTOM, pady=13)
delete_button.place(x=550, y=0)



second_window = tk.Toplevel(root)
second_window .title("Aerostudio")
second_window .geometry("900x500+300+200")
second_window .resizable(False,False)
second_window.geometry(f"+{root.winfo_screenwidth() - 800}+0")

def getWeather():
    try:
        city=textfield.get()
        name.config(text="CURRENT WEATHER")

        #Weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=6a2f0cdcb04ad545e7ee0d59049f1400"

        json_data = requests.get(api).json()
        condition= json_data['weather'][0]['main']
        description=json_data['weather'][0]["description"]
        temp=int(json_data['main']['temp']-273.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE", temp, "°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App","Invilid name")



#Search box
Search_image=PhotoImage(file=r"C:\Users\Admin\Desktop\fizyka\Aera Studio\Aerostudio,py\search.png")
myimage=Label(second_window,image=Search_image)
myimage.place(x=20, y=20)

textfield=tk.Entry(second_window,justify="center", width=17, font=("popins",25,"bold"))
textfield.place(x=50,y=40)
textfield.focus()

Search_icon=PhotoImage(file=r"C:\Users\Admin\Desktop\fizyka\Aera Studio\Aerostudio,py\search_icon.png")
myimage_icon=Button(second_window,image=Search_icon,borderwidth=0, cursor="hand2", bg="#404040",command=getWeather)
myimage_icon.place(x=400, y=34)

#logo
Logo_image=PhotoImage(file=r"C:\Users\Admin\Desktop\fizyka\Aera Studio\Aerostudio,py\logo.png")
logo=Label(second_window,image=Logo_image)
logo.place(x=150, y=100)

#Bottom box
Frame_image=PhotoImage(file=r"C:\Users\Admin\Desktop\fizyka\Aera Studio\Aerostudio,py\box.png")
frame_myimage=Label(second_window,image=Frame_image)
frame_myimage.pack(padx=5, pady=5,side=BOTTOM)

#Time
name=Label(second_window,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(second_window,font=("Helvertica",20))
clock.place(x=30, y=130)

#Label
label1=Label(second_window,text="Wind",font=("Helvetica",15,"bold"), fg="white",bg="#1ab5ef")
label1.place(x=120, y=400)

label2=Label(second_window,text="HUMIDITY", font=("helevetica", 15,'bold'), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3=Label(second_window,text="DESCTIPTION", font=("helevetica", 15,'bold'), fg="white", bg="#1ab5ef") 
label3.place(x=430, y=400)

label4=Label(second_window,text="PRESSURE", font=("helevetica", 15,'bold'), fg="white", bg="#1ab5ef") 
label4.place(x=650, y=400)

t=Label(second_window,font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(second_window,font=("arial",15,"bold"))
c.place(x=400, y=250)

w=Label(second_window,text="...",font=('arial', 20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(second_window,text="...",font=('arial', 20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)
d=Label(second_window,text="...",font=('arial', 20,"bold"),bg="#1ab5ef")
d.place(x=450,y=430)
p=Label(second_window,text="...",font=('arial', 20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)



root=mainloop()
from tkinter import *


constList = ["Residential","Commercial","Industrial"]

def substrcation():
    cc = int(curwat.get())
    pc = int(prewat.get())
    


    if cc > pc:
        ttw = cc - pc
        decwat.delete(0, END)
        decwat.insert(0, ttw)
        print(ttw)
        constType(ttw)        
    else:
        decwat.delete(0, END)
        decwat.insert(0, "Error Total Wattage")
        print("Current wattage must be higher")

def constType(totalW):
    n = int(catcher.get())
    ccc = constList[n]
    youpicked =  ccc + " type "
    textOnframe.config(text=youpicked)
    print(youpicked)

    if totalW >= 100:
        if ccc == constList[0]:
            print("rate=18.75, tax=0.05, addCost=0")
            valuess = dict(rate=18.75, tax=0.05, addCost=0)
            vresOnFrame.config(text=f'Rate: {valuess["rate"]} Tax: {valuess["tax"]}  Additional Cost:{valuess["addCost"]}',bg='pink')
            
        elif ccc == constList[1]:
            print("rate=20.25, tax=0.1, addCost=200")
            valuess = dict(rate=20.25, tax=0.1, addCost=200)
            vresOnFrame.config(text=f'Rate: {valuess["rate"]} Tax: {valuess["tax"]}  Additional Cost:{valuess["addCost"]}',bg='pink')
            
        elif ccc == constList[2]:
            print("rate=22.75, tax=0.1, addCost=500")
            valuess = dict(rate=22.75, tax=0.1, addCost=500)
            vresOnFrame.config(text=f'Rate: {valuess["rate"]} Tax: {valuess["tax"]}  Additional Cost:{valuess["addCost"]}',bg='pink')
            
        else:
            return None
            print("")   

    elif totalW < 100:
        if ccc == constList[0]:
            print("rate=17.5, tax=0, addCost=0")
            valuess = dict(rate=17.5, tax=0, addCost=0)
            vresOnFrame.config(text=f'Rate: {valuess["rate"]} Tax: {valuess["tax"]}  Additional Cost:{valuess["addCost"]}',bg='pink')
            
        elif ccc == constList[1]:
            print("rate=19.75, tax=0.02, addCost=100")
            valuess = dict(rate=19.75, tax=0.02, addCost=100)
            vresOnFrame.config(text=f'Rate: {valuess["rate"]} Tax: {valuess["tax"]}  Additional Cost:{valuess["addCost"]}',bg='pink')
        elif ccc == constList[2]:
            print("rate=22.55, tax=0.05, addCost=300")
            valuess = dict(rate=22.55, tax=0.05, addCost=300)
            vresOnFrame.config(text=f'Rate: {valuess["rate"]} Tax: {valuess["tax"]}  Additional Cost:{valuess["addCost"]}',bg='pink')
            
        else:
            return None
            print("")
            
    else:
        print("Error")
    
    gmb = totalW * valuess["rate"]
    fmb = gmb + valuess["addCost"] + (gmb * valuess["tax"])
    resOnFrame.config(
        text=
        f'Gross Monthly :{gmb} kw/hr\n'+
        f'Final Monthly : {fmb} kw/hr',
        bg='white'
    )
    print(fmb)


root = Tk()
root.title('Billing')
root.geometry("410x250")
root.configure(bg='black')

mainframe = LabelFrame(root,text="Canvs",padx=80,pady=10,bg='red')
mainframe.grid(row=0,column=0,pady=10,padx=10, columnspan=5)

textOnframe = Label(mainframe, text= "Please Select Consumer type", font=("Times New Roman", 10),bg='pink')
textOnframe.grid(row=1, column=0,pady=10,padx=10)


vresOnFrame = Label(mainframe,text="Consumer Type Value will show here",bg='black')
vresOnFrame.grid(row=3, column=0)

resOnFrame = Label(mainframe,
    text="Gross Monthly kw/hr\n"+
        "Final Monthly kw/hr",
        bg='white'
)
resOnFrame.grid(row=2, column=0)


curwatLb = Label(root, text= "Current Wattage ",bg='black')
curwatLb.grid(row=1, column=0)

curwat = Entry(root)
curwat.grid(row=2, column=0,padx=4,pady=2)  

prewatLb = Label(root, text= "Previews Wattage ",bg='black')
prewatLb.grid(row=1, column=1)

prewat = Entry(root)
prewat.grid(row=2, column=1,padx=4,pady=2)

decwatLb = Label(root, text= "Total Wattage",bg='black')
decwatLb.grid(row=1, column=2)

decwat = Entry(root)
decwat.insert(0, "No value")
decwat.grid(row=2, column=2,padx=4,pady=2)


catcher = IntVar()
Residential = Radiobutton(root, text = "Residential" , variable=catcher, value=0, command=constType,bg='pink')
Residential.grid(row=3,column=0 ,padx= 10)
Commercial = Radiobutton(root,text = "Commercial", variable=catcher, value=1,command=constType,bg='pink')
Commercial.grid(row=3,column=1 ,padx= 10)
Industrial = Radiobutton(root,text = "Industrial", variable=catcher, value=2,command=constType,bg='pink')
Industrial.grid(row=3,column=2 ,padx= 10)

OKbtn = Button(root,text = "OK", command=substrcation, padx= 30)
OKbtn.grid(row=4,column=1 ,padx= 10, pady=1)

root.mainloop()
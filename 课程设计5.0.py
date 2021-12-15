#Assets of the bank = balance of the bank + loans made by the bank 

#Read the data for each bank and convert it to a two-dimensional list
def data_file_to_list(data_file):
    cont = 0
    bank_data_list = []
    for bank_data in data_file:
        bank_data.replace("\n",'')
        bank_data_list.append(bank_data.split())#Get a two-dimensional list of banks
        cont+=1
        if cont == n:#Only the first n lines are read
            break
    return bank_data_list

#Total assets of each bank
def original_assets(bank_ID,list1):
    original_assets = 0
    #is not going to show up because I have less n and my total assets are going to go down
    if list1[bank_ID][1] == '1':
        original_assets = eval(list1[bank_ID][0])+eval(list1[bank_ID][3])
    else: 
        original_assets = eval(list1[bank_ID][0])+eval(list1[bank_ID][3])+eval(list1[bank_ID][5])
    return original_assets


#Determine which unsafe banks will cause them to become unsafe
def affect_other_banks(bank_ID,list1):
    i = 0
    for bank_data in list1:
        if bank_data[1]=='2':
            if int(bank_data[2]) == bank_ID:
                assets[i] -= eval(bank_data[3])
            elif int(bank_data[4]) == bank_ID:
                assets[i] -= eval(bank_data[5])
        elif int(bank_data[2]) == bank_ID:
            assets[i] -= eval(bank_data[3])
        if assets[i]<limit:
            if i not in unsafe_bank:#The unsafe bank sequence is not repeated to facilitate subsequent statistics
                unsafe_bank.append(i)
        i+=1

# main program 
# -*- encoding=utf-8 -*-
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import turtle
from PIL import Image ,ImageTk

def insert():
    """Insert data"""
    info = []
    #Format unsafe banks into the list
    unsafe_bank.sort()#Sort the list to make it easier for users to see
    for i in range(len(unsafe_bank)):
        info.append([str(unsafe_bank[i]),\
                     str(original_assets(unsafe_bank[i],data_list)),\
                     str(assets[unsafe_bank[i]])])
    for index,data in enumerate(info):
        table.insert('',END,values = data)#Add data to the end



def draw():
    """Draw a bank relationship diagram"""
    theScreen = turtle.TurtleScreen(canva)
    theScreen.bgcolor("floralwhite")#Set the background color
    t = turtle.RawTurtle(theScreen)
    t.hideturtle()
    t.speed(11)
    if n == 5:
        drawcircle(0,240,1,t)#Draw the first group
        t.goto(10,160)
        t.write(125,font = ("微软雅黑",16))
        drawline(0,240,-20,283,85,t)
        drawline(-6,234,-72,265,40,t)

        drawcircle(-350,150,0,t)#Draw the second group
        t.write(25,font = ("微软雅黑",16))
        drawline(-350,160,15,325,100.5,t)
        drawline(-365,138,-43,250,320.5,t)

        drawcircle(-150,-50,4,t)#Draw the third group
        t.write(181,font = ("微软雅黑",16))
        drawline(-150,-45,2,213,125,t)

        drawcircle(100,-40,2,t)#Draw the fourth group
        t.goto(140,-140)
        t.write(175,font = ("微软雅黑",16))
        drawline(96,-23,40,225,75,t)
        drawline(69,-23,158,452,125,t)

        drawcircle(300,130,3,t)#Draw the fifth group
        t.goto(310,50)
        t.write(75,font = ("微软雅黑",16))
        drawline(262,130,178,610,125,t)
    elif n ==4:
        drawcircle(-350,150,0,t)#Draw the second group
        t.write(345.5,font = ("微软雅黑",16))
        drawline(-350,160,15,325,100.5,t)

        drawcircle(0,240,1,t)#Draw the first group
        t.goto(10,160)
        t.write(125,font = ("微软雅黑",16))
        drawline(0,240,-20,283,85,t)
        drawline(-6,234,-72,265,40,t)

        drawcircle(100,-40,2,t)#Draw the fourth group
        t.goto(140,-140)
        t.write(175,font = ("微软雅黑",16))
        drawline(96,-23,40,225,75,t)
        drawline(69,-23,158,452,125,t)

        drawcircle(300,130,3,t)#Draw the fifth group
        t.goto(310,50)
        t.write(75,font = ("微软雅黑",16))
        drawline(262,130,178,610,125,t)
    elif n == 3:
        drawcircle(-350,150,0,t)#Draw the second group
        t.write(345.5,font = ("微软雅黑",16))
        drawline(-350,160,15,325,100.5,t)

        drawcircle(0,240,1,t)#Draw the first group
        t.goto(10,160)
        t.write(210,font = ("微软雅黑",16))
        drawline(-6,234,-72,265,40,t)

        drawcircle(100,-40,2,t)#Draw the fourth group
        t.goto(140,-140)
        t.write(250,font = ("微软雅黑",16))
        drawline(69,-23,158,452,125,t)
    elif n == 2:
        drawcircle(-350,150,0,t)#Draw the second group
        t.write(345.5,font = ("微软雅黑",16))
        drawline(-350,160,15,325,100.5,t)

        drawcircle(0,240,1,t)#Draw the first group
        t.goto(10,160)
        t.write(250,font = ("微软雅黑",16))
    else:
        drawcircle(-350,150,0,t)#Draw the second group
        t.write(446,font = ("微软雅黑",16))
        drawline(-350,160,15,325,100.5,t)
    theScreen.mainloop()
#Draw some circles   
def drawcircle(x,y,i,t):
    """draw circle"""
    y = y - 100
    t.pu()
    t.setheading(0)
    t.goto(x,y)
    t.pensize(3)
    t.write(i)
    t.goto(x,y-13)
    t.pd()
    t.circle(18)
    t.pu()
    t.goto(x-60,y)
#draw a straight line
def drawline(x,y,angle,length,number,t):
    """Draw a straight line"""
    y = y - 100
    t.pu()
    t.goto(x+18,y)
    t.pd()
    t.setheading(angle)
    t.forward(length)
    t.begin_fill()
    t.fillcolor("black")
    t.setheading(angle-30)
    t.backward(10)
    t.pu()
    t.forward(10)
    t.setheading(angle+30)
    t.backward(10)
    t.setheading(angle+90)
    t.forward(10)
    t.end_fill()
    t.setheading(angle+180)
    t.forward(length/2)
    t.write(number,font = ("微软雅黑",16))

def new_window1():
    """Processes the data and creates a secondary window to display the data"""
    def treeviewClick(event):#Set click event function, can pop up a dialog box to show detailed data
        for item in table.selection():
            item_text = table.item(item,"values")
            tk.messagebox.showinfo(message = "This is bank {}，original assets are {}, final assets are {}".format(item_text[0],item_text[1],item_text[2]),\
                                   title = "the specific data")
                              

    #Prompt user for bank number
    global n
    n = eval(bank_numbers.get())
    #prompt the user for limits
    global limit
    limit = eval(bank_limits.get())
    #The bank data is stored in a txt file, each line is the data of a bank, and the number starts from zero
    #corresponding to the number of each bank successively
    data_file = open("五个银行的基本数据.txt","r")
    global data_list

    data_list = data_file_to_list(data_file)

    #Initial assets deposited in each bank
    global assets
    assets = []
    for i in range(n):
        assets.append(original_assets(i,data_list))
    #Put the ID of each unsecured bank
    global unsafe_bank
    unsafe_bank = []
    for i in range(n):#Here is a preliminary judgment
        if original_assets(i,data_list)<limit:
            affect_other_banks(i,data_list)
    for i in range(n):#Further determine which banks will be affected as other banks become unsafe
        if original_assets(i,data_list)>limit and assets[i]<limit:
            affect_other_banks(i,data_list)

    #If all banks are safe, set the messagebox to tell the user, and no subsequent operation
    if unsafe_bank ==[]:
        tk.messagebox.showinfo(message = 'All banks are safe!')
        return


    new_win = tk.Toplevel(win)
    new_win.title('the analysis of bank crisis')  # titles
    screenwidth = new_win.winfo_screenwidth()  # Screen width
    screenheight = new_win.winfo_screenheight()  # Screen height
    width = 1000
    height = 500
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    new_win.geometry('{}x{}+{}+{}'.format(width, height, x, y))# Size and location

    tk.Label(new_win,text ='The list of unsafe banks',height = 1,width = 30,font = ("微软雅黑",16)).grid(row = 0,column = 1)
    Label(new_win,text = "BANK CRISIS",font = ("Snap ITC",19)).grid(row = 1,column = 0)
    Label(new_win,text = "BANK CRISIS",font = ("Snap ITC",19)).grid(row = 1,column = 2)
    
    #Make a chart
    columns = ['Bank ID', 'Original assets','Final assets']
    global table
    table = ttk.Treeview(
            master=new_win,  #  the parent container
            height=n,  # number of rows displayed in the table,height row
            columns=columns,  # columns displayed
            show='headings',  # Hide the first column
            )

    for column in columns:
        table.heading(column = column,text = column,anchor = CENTER,\
                        command = lambda name = column:
                        messagebox.showinfo('','This is {}~~~'.format(name)))#Define the header
        table.column(column = column , width = 330, minwidth = 330,anchor = CENTER)#define column
    table.grid(row = 1,column = 1)

    insert()
    f1 = Frame(new_win)
    f1.grid(row = 2,column = 1)
    global canva
    canva = Canvas(new_win,width =1000,height = 600)
    canva.grid(row = 3,column = 1)
    tk.Label(f1,text = "The safe limit is {} and {} banks are unsafe in total".format(limit,len(unsafe_bank)),font = ("微软雅黑",12),bg = "red").pack()
    ttk.Button(f1,text = 'Show the loan relationships among banks',width = 40,command = draw).pack()
    image = Image.open("bank1.gif")
    picture = ImageTk.PhotoImage(image)
    Label(new_win,image = picture,width = 275,height = 600).grid(row = 3,column = 2)
    image2 = Image.open("bank2.gif")
    picture2 = ImageTk.PhotoImage(image2)
    Label(new_win,image = picture2,width = 275,height = 600).grid(row = 3,column = 0)
    table.bind("<ButtonRelease-1>",treeviewClick)#The treeviewClick function is triggered when the left mouse button is released
    new_win.mainloop()
    
if __name__ == '__main__':
    pass
    win = tk.Tk()  # main window
    win.title('Welcom to Bank Crisis Analysis')  
    screenwidth = win.winfo_screenwidth()  
    screenheight = win.winfo_screenheight()  
    width = 400
    height = 300
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    # Welcome window canvas for images
    canvas = tk.Canvas(win,width = 400,height = 135)
    canvas.pack(side = "top")
    image_file = tk.PhotoImage(file = 'BANK.gif')
    image = canvas.create_image(250,-90,anchor = 'n',image = image_file)


    ttk.Label(win,text = "Welcome to Bank crisis",font = ("Arial",18)).pack()
    ttk.Label(win,text = "bank numbers:",font = ("Arial",14)).place(x=0,y=170)#Prompt user to enter the bank numbers
    ttk.Label(win,text = "safe limits:",font = ("Arial",14)).place(x=33,y=210)#Prompt the user to enter a safe limit

    bank_numbers = tk.StringVar()#Bind the value entered by the user to the variable
    entry_numbers = ttk.Entry(win,textvariable = bank_numbers,font=('Arial',14))
    bank_numbers.set("an integer between 1-5")
    entry_numbers.place(x = 130,y = 175)

    bank_limits = tk.StringVar()#Bind the value entered by the user to the variable
    entry_limits = ttk.Entry(win,textvariable = bank_limits,font=('Arial',14))
    bank_limits.set("a positive number")
    entry_limits.place(x = 130,y = 215)


    #Get detailed data and loan relationships among banks
    ttk.Button(win,text = "Get the detailed data",width = 20,command = new_window1).place(x = 120,y = 260)
    
    win.mainloop()

#Tubak calculator

#coding utf-8

#importing
import math
import tkinter as tk
from tkinter.filedialog import asksaveasfilename

#Variables used in button command functions
r = 0
bpc = False
bsc = False
bmc = False
bdc = False
blc = False
i = 0

#FUNCTIONS
#calculation functions
def buttonpclick():
    global bpc
    global i
    i = float(editbox1.get())
    editbox1.delete(0, 'end')
    bpc = True
    return
def buttonsclick():
    global bsc
    global i
    i = float(editbox1.get())
    editbox1.delete(0, 'end')
    bsc = True
    return
def buttonmclick():
    global bmc
    global i
    i = float(editbox1.get())
    editbox1.delete(0, 'end')
    bmc = True
    return
def buttondclick():
    global bdc
    global i
    i = float(editbox1.get())
    editbox1.delete(0, 'end')
    bdc = True
    return

def buttonsinclick():
    m = float(editbox1.get())
    editbox1.delete(0, 'end')
    result = math.sin(m)
    editbox1.insert(0, result)
    textbox1.insert(index='end', chars=("sin" + str(m) + " = " + str(result) + "\n"))

def buttoncosclick():
    m = float(editbox1.get())
    editbox1.delete(0, 'end')
    result = math.cos(m)
    editbox1.insert(0, result)
    textbox1.insert(index='end', chars=("cos" + str(m) + " = " + str(result) + "\n"))

def buttontanclick():
    m = float(editbox1.get())
    editbox1.delete(0, 'end')
    result = math.tan(m)
    editbox1.insert(0, result)
    textbox1.insert(index='end', chars=("tan" + str(m) + " = " + str(result) + "\n"))

#editing functions
def buttonsignclick():
    m = float(editbox1.get())
    editbox1.delete(0, 'end')
    signR = m * -1
    editbox1.insert(0, signR)
    return

def buttonsquareclick():
    m = float(editbox1.get())
    editbox1.delete(0, 'end')
    result = m * m
    editbox1.insert(0, result)
    textbox1.insert(index='end', chars=(str(m) + "×" + str(m) + "=" + str(result) + "\n"))

def ButtonLogarithmClick():
    global blc
    global i
    i = float(editbox1.get())
    editbox1.delete(0, 'end')
    blc = True
    return

def Buttonwhatclick():
    print("no sc")
    return 
def buttoneclick():
    global r
    global i
    global bpc
    global bsc
    global bmc
    global bdc
    global blc
    n = float(editbox1.get())
    if bpc == True:
        r = i + n
        c = "+"
    elif blc == True:
        r = math.log(n, i)
        c = "log"
    elif bsc == True:
        r = i - n
        c = "-"
    elif bmc == True:
        r = i * n
        c = "×"
    elif bdc == True:
        if n == 0:
            editbox1.delete(0, 'end')
            editbox1.insert(344)
        else:
            r = i / n
            c = "÷"
    else:
        pass
    if bpc or bsc or bmc or bdc == True:
        editbox1.delete(0, 'end')
        editbox1.insert(0, r)
        textbox1.insert(index='end', chars=(str(i) + " " + c + " " + str(n) + " = " + str(r) + "\n"))
    elif blc == True:
        editbox1.delete(0, 'end')
        editbox1.insert(0, r)
        textbox1.insert(index='end', chars=("log" + str(i) + "(" + str(n) + ")" + " = " + str(r) + "\n"))

    r = 0
    i = 0
    n = 0
    c = ""
    bpc = False
    bsc = False
    bmc = False
    bdc = False
    blc = False
    return

#editing functions are same here, but for the numbers
def buttoncclick():
    editbox1.delete(0, 'end')
def button7click() :
    editbox1.insert('end', 7)
def button8click():
    editbox1.insert('end', 8)
def button9click():
    editbox1.insert('end', 9)
def button4click():
    editbox1.insert('end', 4)
def button5click():
    editbox1.insert('end', 5)
def button6click():
    editbox1.insert('end', 6)
def button1click():
    editbox1.insert('end', 1)
def button2click():
    editbox1.insert('end', 2)
def button3click():
    editbox1.insert('end', 3)
def button0click():
    editbox1.insert('end', 0)
def buttondotclick():
    editbox1.insert('end', ".")
def buttonptteclick():
    editbox1.insert('end', "e+")

#Others
#Save file function
#I deleted save function. because i copied it lol

#HELP button
def HELP():
    textbox1.insert('end', chars="Enter your very own help message or delete.")

#GUI Down below here.
#Window Build
root = tk.Tk()

#Window geometries and etc.
root.geometry("550x400")
root.title("TuBak")

#Labels
label1 = tk.Label(root, text="Calculator", font=("Courier", 14))
label1.place(x=20, y=20)
label2 = tk.Label(root, text="----------------------------------", font=("Courier", 14))
label2.place(x=10, y=40)
label3 = tk.Label(root, text="|", font=("Courier", 20))
label3.place(x=275, y=150)
label4 = tk.Label(root, text="Formula History/Note", font=("Courier", 14))
label4.place(x=295, y=20)

#Interactions/Display
editbox1 = tk.Entry(width=15, font=("Courier", 28))
editbox1.place(x=15, y=70)

textbox1 = tk.Text(width=30, font=("Courier", 14))
textbox1.place(x=295, y=50)

#Buttons/Interactions
#Calculation Buttons
buttonP = tk.Button(root, text = "+", font=("Courier", 14), command=buttonpclick)
buttonP.place(x=20, y=155)

buttonS = tk.Button(root, text="-", font=("Courier", 14), command=buttonsclick)
buttonS.place(x=20, y=185)

buttonM = tk.Button(root, text="×", font=("Courier", 14), command=buttonmclick)
buttonM.place(x=20, y=215)

buttonD = tk.Button(root, text="÷", font=("Courier", 14), command=buttondclick)
buttonD.place(x=20, y=245)

buttonE = tk.Button(root, text="=", font=("Courier", 14), command=buttoneclick)
buttonE.place(x=20, y=275)

buttonsin = tk.Button(root, text="sin", font=("Courier", 14), command=buttonsinclick)
buttonsin.place(x=200, y=125)

buttoncos = tk.Button(root, text="cos", font=("Courier", 14), command=buttoncosclick)
buttoncos.place(x=200, y=155)

buttontan = tk.Button(root, text="tan", font=("Courier", 14), command=buttontanclick)
buttontan.place(x=200, y=185)

buttonsqre = tk.Button(root, text="sqr", font=("Courier", 14), command=buttonsquareclick)
buttonsqre.place(x=200, y=215)

buttonLogarithm = tk.Button(root, text="log", font=("Courier", 14), command=ButtonLogarithmClick)
buttonLogarithm.place(x=200, y=245)

buttonpttE = tk.Button(root, text="e", font=("Courier", 14), command=buttonptteclick)
buttonpttE.place(x=60, y=125)

buttonsign = tk.Button(root, text="±", font=("Courier", 14), command=buttonsignclick)
buttonsign.place(x=100, y=125)

buttonC = tk.Button(root, text="C", font=("Courier", 14), command=buttoncclick)
buttonC.place(x=20, y=125)

#Number Buttons
button7 = tk.Button(root, text="7", font=("Courier", 14), command=button7click)
button7.place(x=60, y=155)

button8 = tk.Button(root, text="8", font=("Courier", 14), command=button8click)
button8.place(x=100, y=155)

button9 = tk.Button(root, text="9", font=("Courier", 14), command=button9click)
button9.place(x=140, y=155)

button4 = tk.Button(root, text="4", font=("Courier", 14), command=button4click)
button4.place(x=60, y=185)

button5 = tk.Button(root, text="5", font=("Courier", 14), command=button5click)
button5.place(x=100, y=185)

button6 = tk.Button(root, text="6", font=("Courier", 14), command=button6click)
button6.place(x=140, y=185)

button1 = tk.Button(root, text="1", font=("Courier", 14), command=button1click)
button1.place(x=60, y=215)

button2 = tk.Button(root, text="2", font=("Courier", 14), command=button2click)
button2.place(x=100, y=215)

button3 = tk.Button(root, text="3", font=("Courier", 14), command=button3click)
button3.place(x=140, y=215)

button0 = tk.Button(root, text="0", font=("Courier", 14), command=button0click)
button0.place(x=100, y=245)

buttondot = tk.Button(root, text=".", font=("Courier", 14), command=buttondotclick)
buttondot.place(x=60, y=245)

#Other functionings
#savebutton = tk.Button(root, text="Save", font=("Courier", 14), command=save_file)
#savebutton.place(x=475, y=20)

HelpButton = tk.Button(root, text="HELP", font=("Courier", 14), command=HELP)
HelpButton.place(x=200, y=360)

#End building Window
root.mainloop()

import tkinter as tk
import random as rd
window = tk.Tk()


def Iniciar():
    DisplayDice = tk.Frame(master = window, borderwidth = 1, relief = tk.GROOVE)
    DisplayControl = tk.Frame(master = window)
    DisplayButtonArea = tk.Frame(master = window)
    DisplayDice.pack(expand = True)
    DisplayControl.pack(expand = True)
    DisplayButtonArea.pack(expand = True)

    Rolled = tk.Label(master = DisplayDice, text = "", background = "black", foreground = "white", wraplength=400, anchor="w")
    Rolled.grid(row = 0 , column = 0)    
    
    DiceNumber = tk.Entry(master = DisplayControl, width = 2)
    DiceMax = tk.Entry(master=DisplayControl, width = 3)
    D = tk.Label(master = DisplayControl, text = "d")

    RollButton = tk.Button(master = DisplayButtonArea, text = "Rolar", command = lambda: Roll(DiceNumber, DiceMax, Rolled))
    AddQuestion = tk.Button(master = DisplayButtonArea, bg = "red", command = lambda: Switching(AddQuestion))

    DiceNumber.grid(row = 0, column = 0)
    DiceMax.grid(row = 0, column = 2)
    D.grid(row = 0, column = 1)

    RollButton.grid(row = 1, column = 1)
    AddQuestion.grid(row = 1, column = 2)

def Roll(DiceNumber, DiceMax, Rolled):
    global Switch
    Dices = DiceNumber.get()
    Max = DiceMax.get()
    Dices = int(Dices)
    Max = int(Max)
    Rolls= []
    Added = 0
    RollsString = "| "
    
    for i in range(0, Dices):
        roll = rd.randint(1, Max)
        Rolls.append(roll)

    if Switch == False:
        for i in Rolls:
            b = str(i)
            RollsString = RollsString + b + " | "
    elif Switch == True:
        for i in Rolls:
            Added = Added + i
        Added = str(Added)
        RollsString = RollsString + Added + " |"
            
    print(RollsString)
    Rolled.configure(text=RollsString)

def Switching(AddQuestion):
    global Switch
    if Switch == False:
        Switch = True
        AddQuestion.configure(bg = "Blue")
    else:
        Switch = False
        AddQuestion.configure(bg="Red")
        
Switch = False
Iniciar()


window.mainloop()
from tkinter import *
import random
from tkinter import messagebox
import time

win = Tk()
win.title("Match It")
win.resizable(height = False, width = False)

count, winner = 0, 0
btn_dict = {}
ans_list = []
ans_dict = {}

def reset():
    global matches, winner, btn_dict
    winner = 0
    matches = [1,1,2,2,3,3,4,4,5,5,6,6]
    random.shuffle(matches)
    for button in btn_dict.values():
        button.config(text=" ", state = "normal")

def OnClick(row, col, i):
    global btn_dict, count, ans_list, ans_dict, winner
    
    if btn_dict[row, col]["text"] == ' ' and count < 2:
        b = btn_dict[row, col]
        b["text"] = numbers[i]
        ans_list.append(numbers[i])
        ans_dict[b] = numbers[i]
        count += 1

        if count == 2:            
            #if the numbers match
            if ans_list[0] == ans_list[1]:
                for k in ans_dict:
                    k['state'] = "disabled"
                ans_list = []
                ans_dict = {}
                count = 0
                winner += 1
                if winner == 6:
                    messagebox.showinfo("Game Over", "Wooohooo !! Congratulations. Game over.")
                
            #if the numbers don't match
            else:
                messagebox.showinfo("Try again", "Try Again...")            
                for k in ans_dict:                    
                    k["text"] = ' '                
                ans_list = []
                ans_dict = {}
                count = 0

numbers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
random.shuffle(numbers)
rows, cols = 3, 4
ind = 0

for r in range(rows):
    for c in range(cols):
        btn = Button(win, command = lambda r=r, c=c, ind=ind: OnClick(r, c, ind), width = 6, height = 3, text = ' ', font = ("Raleway", 20), relief = "ridge", bg = "pink")
        btn.grid(row = r, column = c)
        btn_dict[r, c] = btn
        ind += 1


#Adding a menu
my_menu = Menu(win)
win.config(menu = my_menu)
option_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label = "Options", menu = option_menu)
option_menu.add_command(label = "Reset Game", command = reset)

win.mainloop()

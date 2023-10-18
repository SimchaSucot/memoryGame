import tkinter as tk
from random import randint
import time
dic_num = {} # Dictionary for CLASS Card
lst_btn = [] # List for CLASS Start
lst_too = [] # List for CLASS Play
now_time = 0 # Variable to save the time that started playing
opn = 0 # Variable for CLASS Play
won = 0 # Variable for CLASS Play
class Start:

    # The function gives the name of the game
    # and below it two buttons to choose between a big or a small game
    def home_page(self):
        hello = tk.Label(text='     משחק הזיכרון     ',font=30,bg='yellow')
        hello.grid(row=0,column=0,columnspan=4,sticky='NESW')
        little_play = tk.Button(text='  לוח קטן  ', font=40, fg='green', command=self.little)
        little_play.grid(row=1, column=0, columnspan=4, sticky='NESW')
        big_play = tk.Button(text='  לוח גדול  ', font=40,fg='green', command=self.big)
        big_play.grid(row=2, column=0, columnspan=4,sticky='NESW')
        big_play = tk.Button(text='  לוח ענק  ', font=40, fg='green', command=self.biger)
        big_play.grid(row=3, column=0, columnspan=4, sticky='NESW')

    # The following 3 functions define the three sizes of the board
    def little(self):
        self.all_btn(16)
    def big(self):
        self.all_btn(36)
    def biger(self):
        self.all_btn(64)

    # The function makes the data of the buttons,
    # including (card number, position 1 of the card, position 2 of the card),
    # and sends it to the class Play that builds the buttons.
    # And also enters the data into a list.
    # And also sends the amount of cards to class Card which creates the numbers that will appear on the cards.
    def all_btn(self,num):
        global now_time
        now_time=(time.time())
        print(now_time) ###############################
        self.num = num
        number = 0
        for i in range(int(self.num**0.5)):
            for n in range(int(self.num**0.5)):
                Play(number, i, n)
                lst_btn.append([ i, n])
                number += 1
        print(lst_btn) #############################
        Card(self.num)
class Card:
    def __init__(self,card):
        self.card = card
        self.lst_card = []
        self.amount()
    def amount(self):
        for i in range(int(self.card//2)):
            self.lst_card.append(i)
            self.lst_card.append(i)
        print(self.lst_card) ############################
        self.rand()
    def rand(self):
        self.number1 = 0
        while len(dic_num) < self.card:
            r = randint(0, self.card-1)
            if r not in dic_num.keys():
                dic_num.update([(r, self.lst_card[self.number1])])
                self.number1 += 1
        print(dic_num) ##########################
class Play:
    def __init__(self,num1,num2,num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.winning = []
        self.covered_button()
        global now_time
    def covered_button(self):
        self.button = tk.Button(root, text=f'   ?   ', font=30, fg='red', command=self.visible_button)
        self.button.grid(row=self.num2,column=self.num3,sticky='NESW')
    def visible_button(self):
        lst_too.append(self.num1)
        self.btn1 = tk.Button(text=f'  {dic_num[lst_too[0]]}  ', font=30, fg='green')
        self.btn1.grid(row=lst_btn[lst_too[0]][0], column=lst_btn[lst_too[0]][1], sticky='NESW')
        root.after(800, self.btn1.destroy)
        if len(lst_too) == 2:
            global opn
            opn += 1
            self.btn1 = tk.Button(text=f'  {dic_num[lst_too[0]]}  ', font=30,fg='green')
            self.btn1.grid(row=lst_btn[lst_too[0]][0], column=lst_btn[lst_too[0]][1], sticky='NESW')
            self.btn2 = tk.Button(text=f'  {dic_num[lst_too[1]]}  ', font=30,fg='green')
            self.btn2.grid(row=lst_btn[lst_too[1]][0], column=lst_btn[lst_too[1]][1], sticky='NESW')
            if dic_num[lst_too[0]] != dic_num[lst_too[1]] or lst_too[0] == lst_too[1]:
                self.btn1.after(800,self.btn1.destroy)
                self.btn2.after(800,self.btn2.destroy)
            else:
                global won
                won += 1
                print(won) #################
                print(len(lst_btn)//2)  ###########
                if won == len(lst_btn)//2:
                    for i in root.winfo_children():
                        i.destroy()
                    finish = tk.Label(text=f'סיימת את המשחק ב {int((time.time())-now_time)} שניות',font=30,fg='blue')
                    finish.grid(row=0,column=0,columnspan=4, sticky='NESW')
                    num_opn = tk.Label(text=f'פתחת {opn} פעמים את הכרטיסים', font=30,fg='blue')
                    num_opn.grid(row=1, column=0, columnspan=4, sticky='NESW')
                    again = tk.Button(text='    שחק שוב    ',font=30,bg='yellow',command=self.agn)
                    again.grid(row=2,column=0,columnspan=4, sticky='NESW')
                    print(int((time.time())-now_time))
            print(lst_too)  ##########################
            lst_too.clear()
    def agn(self):
        global dic_num
        global lst_btn
        global opn
        global won
        dic_num = {}
        lst_btn = []
        opn = 0
        won = 0
        Start().home_page()

root = tk.Tk()
Start().home_page()
root.mainloop()
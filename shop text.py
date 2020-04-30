from Tkinter import *

class Player(object):
    def __init__(self):
        self.hp = 100
        self.mp = 100
        self.attack = 10
        self.gold = 300
        self.inventory = ["Broken Sword"]
        self.name = ''
        self.currWeapon = ''
def showinv():
    print "{}".format(PlayerDe.inventory)

    def __str__(self):
        return self.name

PlayerDe = Player()
def buy(args):
    if args == 1:
        if PlayerDe.gold >= 40:
            PlayerDe.gold -= 40
            PlayerDe.inventory.append("Great Sword")
            print "You bought Great Sword"
        else:
            print "You dont have enough gold"
    if args == 2:
        if PlayerDe.gold >= 10:
            PlayerDe.gold -= 10
            PlayerDe.inventory.append("Potion")
            print "You bought Potion"
        else:
            print "You dont have enough gold"
    if args == 3:
        if PlayerDe.gold >= 25:
            PlayerDe.gold -= 25
            PlayerDe.inventory.append("Key")
            print "You bought Key"
        else:
            print "You dont have enough gold"
    if args == 4:
        if PlayerDe.gold >= 25:
            PlayerDe.gold -= 25
            PlayerDe.inventory.append("Dagger")
            print "You bought Dagger"
        else:
            print "You dont have enough gold"
            
    if args == 5:
        if PlayerDe.gold >= 35:
            PlayerDe.gold -= 35
            PlayerDe.inventory.append("Bow")
            print "You bought Bow"
        else:
            print "You dont have enough gold"
    if args == 6:
        if PlayerDe.gold >= 55:
            PlayerDe.gold -= 55
            PlayerDe.inventory.append("Staff")
            print "You bought Staff"
        else:
            print "You dont have enough gold"


window = Tk()
window.title("Shop")
lbl = Label(window, text="Welcome to the Shop", font= ("Arial Bold",25))
lbl.grid(column=0, row =0)

b1 = Button(window, text="Great Sword", command = lambda:buy(1))
b1.grid(column=0, row=1)
b2 = Button(window, text="Potion", command = lambda:buy(2))
b2.grid(column=0, row=2)
b3 = Button(window, text="Key", command = lambda:buy(3))
b3.grid(column=0, row=3)
b4 = Button(window, text="Inventory", command = showinv)
b4.grid(column=3, row=8)

b5 = Button(window, text="Dagger", command = lambda:buy(4))
b5.grid(column=0, row=5)
b6 = Button(window, text="Bow", command = lambda:buy(5))
b6.grid(column=0, row=6)
b7 = Button(window, text="Staff", command = lambda:buy(6))
b7.grid(column=0, row=7)

window.mainloop()



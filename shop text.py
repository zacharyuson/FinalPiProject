from Tkinter import *
inventory = []
def viewInv():
    print "You have: {}".format(inventory)

class item(object):
    def __init__(self,name, desc, value):
        self.name = name
        self.desc = desc
        self.value = value
    def buy(self):
        inventory.append(item)
        print "You just bought {}".format(self.name)
    def __str__(self):
        return self.name

GS = item("Great Sword", "A large sword", 25)
Pot = item("Potion", "A potion that heals", 10)
Key = item("Key", "A key that opens a door", 45)
window = Tk()
window.title("Shop")
lbl = Label(window, text="Welcome to the Shop", font= ("Arial Bold",25))
lbl.grid(column=0, row =0)

b1 = Button(window, text="Great Sword", command = item.buy(GS))
b1.grid(column=0, row=1)
b2 = Button(window, text="Potion", command = item.buy(Pot))
b2.grid(column=0, row=2)
b3 = Button(window, text="Key", command = item.buy(Key))
b3.grid(column=0, row=3)
b4 = Button(window, text="Inventory", command = viewInv)
b4.grid(column=3, row=4)

window.mainloop()



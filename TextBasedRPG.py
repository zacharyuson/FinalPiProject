from Tkinter import *
import sys
import os
import time
import random

class Player(object):
    def __init__(self):
        self.hp = 100
        self.mp = 100
        self.attack = 10
        self.gold = 40
        self.name = ''
        self.currWeapon = ''

    @property
    def attack(self):
        attackDmg = self.attack

        if self.currWeapon == "Sword":
            attackDmg += 10

        elif self.currWeapon == "Wand":
            attackDmg += 15

        return attackDmg

    @attack.setter
    def attack(self, value):
        self._attack = value


def play_game():
    print "Played!"

class Game(Frame):
    # the constructor
    def __init__(self, parent):
        # call the constructor in the superclass
        Frame.__init__(self, parent)

    # sets up the GUI
    def setupGUI(self):
        # organize and pack the GUI
        self.pack(fill=BOTH, expand=1)

        # setup the player input (bottom)
        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()

        # setup text output on the right of the display
        text_frame = Frame(self, width=WIDTH)
        Game.text = Text(text_frame, bg="lightgrey", wrap=WORD, spacing1=2, state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack()

    # sets the status displayed on the right of the GUI
    def setStatus(self, status):
        Game.screen_selection = "title"
        # clear the text widget
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        Game.text.tag_configure("center", justify='center')

        if status == "":
            Game.text.insert(END, "\n" * 8 + "-Play-\n-Help-\n-Quit-")
        else:
            Game.text.insert(END, status)

        Game.text.tag_add("center", "1.0", "end")
        Game.text.config(state=DISABLED)

    def play(self):
        # configure the GUI
        self.setupGUI()
        # set the current status
        self.setStatus("")

    def process(self, event):
        # set a default response
        response = "I don't understand. Try verb noun. Valid verbs are go, look, and take. Make sure you spell command correctly."

        # get the command input from the GUI
        action = Game.player_input.get()
        action = action.lower()

        # handle verbs and nouns
        words = action.split()

        if len(words) == 1:
            command = words[0]

            if command == "play":
                ## START FUNCTION HERE ##
                response = "Played!"

            if command == "help":
                response = ""
                response += '#' * 80 + "\n"
                response += "Type a command such as 'move' then 'left'\n"
                response += "to navigate the map of the cube puzzle.\n"
                response += "Inputs such as 'look' or 'examine' will\n"
                response += "let you interact with puzzles in rooms.\n"
                response += "Puzzles will require various input and \n"
                response += "possibly answers from outside knowledge.\n"
                response += "Please ensure to type in lowercase for ease.\n"
                response += '#' * 80 + "\n"
                response += "     Type 'back' to return to the main menu.     \n"
                response += '#' * 80 + "\n"

            if command == "back":
                response = ""

            if command == "quit":
                sys.exit()

        #if (len(words) == 2):
         #   verb = words[0]
          #  noun = words[1]

        self.setStatus(response)
        Game.player_input.delete(0, END)

##########################################################
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Final Pi Project")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()

# wait for the window to close
window.mainloop()

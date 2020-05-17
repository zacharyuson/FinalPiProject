from Tkinter import *
import sys
import os
import time
from random import randrange


class Weapon(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Rock(Weapon):
    def __init__(self, name, value, damage):
        self.damage = damage
        super(Rock, self).__init__(name, value)

class Dagger(Weapon):
    def __init__(self, name, value, damage):
        self.damage = damage
        super(Dagger, self).__init__(name, value)

class GreatSword(Weapon):
    def __init__(self, name, value, damage):
        self.damage = damage
        super(GreatSword, self).__init__(name, value)

class Bow(Weapon):
    def __init__(self, name, value, damage):
        self.damage = damage
        super(Bow, self).__init__(name, value)

class Staff(Weapon):
    def __init__(self, name, value, damage):
        self.damage = damage
        super(Staff, self).__init__(name, value)

weaponRock = Rock("Rock", 1, 5)
weaponDagger = Dagger("Dagger", 5, 10)
weaponGreatSword = GreatSword("Great Sword", 100, 50)
weaponBow = Bow("Bow", 10, 15)
weaponStaff = Staff("Staff", 50, 30)

class NPC(object):
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

class Boss(object):
    def __init__(self, name, final = False):
        self.name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    def bossSkills(enemyBoss, eAttack):
        rand = randrange(4)
        if(enemyBoss.name == "boss"):
            if(rand == 0):
                player.hp -= eAttack
            elif(rand == 1):
                player.hp -= eAttack
            elif(rand == 2):
                player.hp -= eAttack
            else:
                player.hp -= eAttack


# the player class
class Player(object):
    def __init__(self):
        self.inventoryDisplay = [weaponRock.name]
        self.inventory = [weaponRock]
        self.hp = 100
        self.mp = 100
        self.damage = 10
        self.gold = 0
        self.name = ""
        self.rating = -10
        self.equipped = ""

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value

player = Player()

# the room class
# note that this class is fully implemented with dictionaries as illustrated in the lesson "More on Data Structures"
class Room(object):
    # the constructor
    def __init__(self, name, image):
        # rooms have a name, an image (the name of a file), exits (e.g., south), exit locations
        # (e.g., to the south is room n), items (e.g., table), item descriptions (for each item),
        # and grabbables (things that can be taken into inventory)
        self.name = name
        self.image = image
        self.exits = {}
        self.items = {}
        self.grabbables = []
        self.enemies = {}
        self.enemiesDamage = {}
        self.enemiesGold = {}
        self.enemiesCheck = {}
        self.enemiesName = []
        self.NPCs = {}

    # getters and setters for the instance variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    @property
    def enemies(self):
        return self._enemies

    @enemies.setter
    def enemies(self, value):
        self._enemies = value

    @property
    def enemiesDamage(self):
        return self._enemiesDamage

    @enemiesDamage.setter
    def enemiesDamage(self, value):
        self._enemiesDamage = value

    @property
    def enemiesGold(self):
        return self._enemiesGold

    @enemiesGold.setter
    def enemiesGold(self, value):
        self._enemiesGold = value
    
    @property
    def enemiesCheck(self):
        return self._enemiesCheck

    @enemiesCheck.setter
    def enemiesCheck(self, value):
        self._enemiesCheck = value

    @property
    def enemiesName(self):
        return self._enemiesName

    @enemiesName.setter
    def enemiesName(self, value):
        self._enemiesName = value
        

    @property
    def NPCs(self):
        return self._NPCs

    @NPCs.setter
    def NPCs(self, value):
        self._NPCs = value

    def addEnemy(self, name, hp, damage, gold, boss = False, finalBoss = False):
        # append the enemy to the list
        self._enemies[name] = hp
        self._enemiesDamage[name] = damage
        self._enemiesGold[name] = gold
        self._NPCs[name] = "..."
        self._enemiesCheck[name] = boss
        self._enemiesName.append(name)

    def delEnemy(self, enemy):
        # remove the enemy from the list
        self._enemies.remove(enemy)

    def addNPC(self, name, hp, damage, gold, description):
        # append the NPC to the list
        self._enemies[name] = hp
        self._enemiesDamage[name] = damage
        self._enemiesGold[name] = gold
        self._NPCs[name] = description
        self._enemiesCheck[name] = False
        self._enemiesName.append(name)

    def delNPC(self, NPC):
        # remove the NPC from the list
        self._NPCS.remove(NPC)

    # adds an exit to the room
    # the exit is a string (e.g., north)
    # the room is an instance of a room
    def addExit(self, exit, room):
        # append the exit and room to the appropriate dictionary
        self._exits[exit] = room

    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made of wood)
    def addItem(self, item, desc):
        # append the item and description to the appropriate dictionary
        self._items[item] = desc

    # adds a grabbable item to the room
    # the item is a string (e.g., key)
    def addGrabbable(self, item):
        # append the item to the list
        self._grabbables.append(item)

    # removes a grabbable item from the room
    # the item is a string (e.g., key)
    def delGrabbable(self, item):
        # remove the item from the list
        self._grabbables.remove(item)

    # a function that subtracts player damage from enemy health
    # and if the enemy isn't killed it's attack from yours
    def attack(self, enemy, pAttack, eAttack):
        best_weapon = None
        max_dmg = 0
        for i in player.inventory:
            if isinstance(i, Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i
        pAttack = i.damage

        # Change the enemy's hp based on the strength of the attack
        self._enemies[enemy] -= pAttack
        # remove the enemy if it dies
        if (self._enemies[enemy] <= 0):
            del self._enemies[enemy]
        # or they retailiate
        else:
            if(self._enemiesCheck[enemy] == False):
                player.hp -= eAttack
            else:
                Boss.bossSkills(Boss(enemy), eAttack)

    def checkRating(self, rating):
        if(rating > 0):
            print " > 0"
        elif(rating < 0):
            g.end()
        else:
            print "0"

    # returns a string description of the room
    def __str__(self):
        # first, the room name
        s = "You are in {}.\n".format(self.name)

        # next, the enemies in the room
        s += "You encounter: "
        for enemy in self.enemies:
            s += enemy + " "
        s += "\n"

        # next, the items in the room
        s += "You see: "
        for item in self.items.keys():
            s += item + " "

        s += "\n"

        # next, the exits from the room
        s += "Exits: "
        for exit in self.exits.keys():
            s += exit + " "
        s += "\n"

        return s


# the game class
# inherits from the Frame class of Tkinter
class Game(Frame):
    # the constructor
    def __init__(self, parent):
        # call the constructor in the superclass
        Frame.__init__(self, parent)

    # creates the rooms
    def createRooms(self):
        # Create the rooms
        global main_menu
        # The starting town rooms
        r1 = Room("Town Square", "square.gif")
        r2 = Room("Shop", "shop.gif")
        r3 = Room("Slums", "slums.gif")
        r4 = Room("Residential Area", "inn.gif")
        main_menu = Room("Main Menu", None)

        r1.addExit("east", r2)
        r1.addExit("west", r3)
        r1.addExit("south", r4)
        r1.addNPC("villager", 7, 2, 10, "Welcome to our town!")
        r1.addItem("sign", "east is the shop, west is the slums, south is the residential area and north is the wild area!")
        r2.addExit("west", r1)
        r3.addExit("east", r1)
        r4.addExit("north", r1)
        main_menu.addExit("play", r1)

        # supplement code to add features to the created rooms

        # The Wild area
        r5 = Room("Starting Path", "path.gif")
        r6 = Room("First Encounter", "path.gif")
        r7 = Room("East Path 1", "path.gif")
        r8 = Room("West Path 1", "path.gif")
        r9 = Room("East Path 2", "path.gif")
        r10 = Room("West Path 2", "path.gif")
        r11 = Room("Reconvergence 1", "path.gif")
        r12 = Room("Second Encounter", "path.gif")
        r13 = Room("East Path 3", "path.gif")
        r14 = Room("West Path 3", "path.gif")
        r15 = Room("East Path 4", "path.gif")
        r16 = Room("West Path 4", "path.gif")
        r17 = Room("East Side Path 1", "path.gif")
        r18 = Room("East Side Path 2", "path.gif")
        r19 = Room("East Side Encounter", "path.gif")
        r20 = Room("West Side Path 1", "path.gif")
        r21 = Room("West Side Path 2", "path.gif")
        r22 = Room("West Side Encounter", "path.gif")
        r23 = Room("Reconvergence 2", "path.gif")
        r24 = Room("Cave 1", "path.gif")
        r25 = Room("Cave Encounter 1", "path.gif")
        r26 = Room("Cave 3", "path.gif")
        r27 = Room("Cave encounter 2", "path.gif")
        r28 = Room("Cave 4", "path.gif")
        r29 = Room("Cave East 1", "path.gif")
        r30 = Room("Cave West 1", "path.gif")
        r31 = Room("Cave East 2", "path.gif")
        r32 = Room("Cave West 2", "path.gif")
        r33 = Room("Cave North East 1", "path.gif")
        r34 = Room("Cave South East 1", "path.gif")
        r35 = Room("Cave North East Encounter", "path.gif")
        r36 = Room("Cave South East Treasure", "path.gif")
        r37 = Room("Cave North West 1", "path.gif")
        r38 = Room("Cave South West 1", "path.gif")
        r39 = Room("Cave North Treasure", "path.gif")
        r40 = Room("Cave South West Encounter", "path.gif")
        r41 = Room("Boss Encounter", "path.gif")

        r1.addExit("north", r5)
        r5.addExit("south", r1)
        r5.addExit("north", r6)
        r6.addExit("south", r5)
        r6.addExit("east", r7)
        r6.addExit("west", r8)
        r6.addEnemy("boar", 7, 7, 5)
        r7.addExit("west", r6)
        r7.addExit("north", r9)
        r8.addExit("east", r6)
        r8.addExit("north", r10)
        r9.addExit("west", r11)
        r9.addExit("south", r7)
        r10.addExit("south", r8)
        r10.addExit("east", r11)
        r11.addExit("east", r9)
        r11.addExit("west", r10)
        r11.addExit("north", r12)
        r12.addExit("south", r11)
        r12.addExit("east", r13)
        r12.addExit("west", r14)
        r12.addEnemy("boar", 7, 7, 5)
        r13.addExit("north", r15)
        r13.addExit("east", r17)
        r13.addExit("west", r12)
        r14.addExit("east", r12)
        r14.addExit("north", r16)
        r14.addExit("west", r20)
        r15.addExit("south", r13)
        r15.addExit("west", r23)
        r16.addExit("south", r14)
        r16.addExit("east", r23)
        r17.addExit("east", r18)
        r17.addExit("west", r13)
        r18.addExit("west", r17)
        r18.addExit("east", r19)
        r19.addExit("west", r18)
        r19.addEnemy("boar", 7, 7, 5)
        r20.addExit("east", r14)
        r20.addExit("west", r21)
        r21.addExit("east", r20)
        r21.addExit("west", r22)
        r22.addExit("east", r21)
        r22.addEnemy("boar", 7, 7, 5)
        r23.addExit("east", r15)
        r23.addExit("west", r16)
        r23.addExit("down", r24)
        r23.addExit("north", r41)
        r24.addExit("up", r23)
        r24.addExit("north", r25)
        r25.addExit("south", r24)
        r25.addExit("north", r26)
        r25.addEnemy("goblin", 15, 5, 10)
        r26.addExit("south", r25)
        r26.addExit("north", r27)
        r27.addExit("south", r26)
        r27.addExit("north", r28)
        r27.addEnemy("goblin", 15, 5, 10)
        r28.addExit("south", r27)
        r28.addExit("east", r29)
        r28.addExit("west", r30)
        r29.addExit("west", r28)
        r29.addExit("east", r31)
        r30.addExit("east", r28)
        r30.addExit("west", r32)
        r31.addExit("west", r29)
        r31.addExit("north", r33)
        r31.addExit("south", r34)
        r32.addExit("east", r30)
        r32.addExit("north", r37)
        r32.addExit("south", r38)
        r33.addExit("south", r31)
        r33.addExit("north", r35)
        r34.addExit("north", r31)
        r34.addExit("south", r36)
        r35.addExit("south", r33)
        r35.addEnemy("goblin", 15, 5, 10)
        r36.addExit("north", r34)
        r37.addExit("south", r32)
        r37.addExit("north", r39)
        r38.addExit("north", r32)
        r38.addExit("south", r40)
        r39.addExit("south", r37)
        r40.addExit("north", r38)
        r40.addEnemy("goblin", 15, 5, 10)
        r41.addExit("south", r40)
        r41.addEnemy("giant boar", 25, 15, 20, True, False)

        # supplement code to add features to the created rooms

        # The Fortress Level 1
        r42 = Room("Fortress 1", "dungeon.gif")
        r43 = Room("Fortress 2", "dungeon.gif")
        r44 = Room("Fortress Encounter 1", "dungeon.gif")
        r45 = Room("Fortress 4", "dungeon.gif")
        r46 = Room("Fortress East Path 1", "dungeon.gif")
        r47 = Room("Fortress West Path 1", "dungeon.gif")
        r48 = Room("Fortress East Encounter", "dungeon.gif")
        r49 = Room("Fortress West Encounter", "dungeon.gif")
        r50 = Room("Fortress North East Path 1", "dungeon.gif")
        r51 = Room("Fortress South East Path 1", "dungeon.gif")
        r52 = Room("Fortress North East Path 2", "dungeon.gif")
        r53 = Room("Fortress South East Path 2", "dungeon.gif")
        r54 = Room("Fortress North North East Path 1", "dungeon.gif")
        r55 = Room("Fortress South South East Path 1", "dungeon.gif")
        r56 = Room("Fortress Encounter NNE", "dungeon.gif")
        r57 = Room("Fortress Encounter SSE", "dungeon.gif")
        r58 = Room("Death Trap", "guillotine.gif")
        r59 = Room("Sublevel Room", "stairs.gif")
        r60 = Room("Fortress North West Path 1", "dungeon.gif")
        r61 = Room("Fortress South West Path 1", "dungeon.gif")
        r62 = Room("Fortress North West Path 2", "dungeon.gif")
        r63 = Room("Fortress South West Path 2", "dungeon.gif")
        r64 = Room("Fortress North North West Path 1", "dungeon.gif")
        r65 = Room("Fortress South South West Path 1", "dungeon.gif")
        r66 = Room("Fortress Encounter NNW", "dungeon.gif")
        r67 = Room("Fortress Encounter SSW", "dungeon.gif")
        r68 = Room("Death Trap", "guillotine.gif")
        r69 = Room("Treasure Storehouse", "treasure.gif")

        r41.addExit("north", r42)
        r42.addExit("south", r41)
        r42.addExit("north", r43)
        r43.addExit("south", r42)
        r43.addExit("north", r44)
        r44.addExit("north", r45)
        r44.addExit("south", r43)
        r44.addEnemy("knight", 50, 10, 20)
        r45.addExit("east", r46)
        r45.addExit("west", r47)
        r45.addExit("south", r44)
        r46.addExit("west", r45)
        r46.addExit("east", r48)
        r47.addExit("east", r45)
        r47.addExit("west", r49)
        r48.addExit("west", r46)
        r48.addExit("north", r50)
        r48.addExit("south", r51)
        r48.addEnemy("knight", 50, 10, 20)
        r49.addExit("east", r47)
        r49.addExit("north", r60)
        r49.addExit("south", r61)
        r49.addEnemy("knight", 50, 10, 20)
        r50.addExit("south", r48)
        r50.addExit("north", r52)
        r51.addExit("north", r48)
        r51.addExit("south", r53)
        r52.addExit("east", r54)
        r52.addExit("south", r50)
        r53.addExit("east", r55)
        r53.addExit("north", r51)
        r54.addExit("west", r52)
        r54.addExit("east", r56)
        r55.addExit("west", r53)
        r55.addExit("east", r57)
        r56.addExit("west", r54)
        r56.addExit("east", r58)
        r56.addEnemy("knight", 50, 10, 20)
        r57.addExit("west", r55)
        r57.addExit("east", r59)
        r57.addEnemy("knight", 50, 10, 20)
        r59.addExit("west", r57)
        r60.addExit("north", r62)
        r60.addExit("south", r49)
        r61.addExit("north", r49)
        r61.addExit("south", r63)
        r62.addExit("south", r60)
        r62.addExit("west", r64)
        r63.addExit("north", r61)
        r63.addExit("west", r65)
        r64.addExit("east", r62)
        r64.addExit("west", r66)
        r65.addExit("east", r63)
        r65.addExit("west", r67)
        r66.addExit("east", r64)
        r66.addExit("west", r69)
        r66.addEnemy("knight", 50, 10, 20)
        r67.addExit("east", r65)
        r67.addExit("west", r68)
        r67.addEnemy("knight", 50, 10, 20)
        r69.addExit("east", r66)

        # Fortress Level 2
        r70 = Room("Floor 2 Room 1", "dungeon.gif")
        r71 = Room("Floor 2 Room 2", "dungeon.gif")
        r72 = Room("Floor 2 Room 3", "dungeon.gif")
        r73 = Room("Floor 2 Room 4", "dungeon.gif")
        r74 = Room("Floor 2 Room 5", "dungeon.gif")
        r75 = Room("Floor 2 Room 6 Encounter", "dungeon.gif")
        r76 = Room("Floor 2 Room 7 Encounter", "dungeon.gif")
        r77 = Room("Floor 2 Room 8 Enounter", "dungeon.gif")
        r78 = Room("Floor 2 Room 9 Encounter", "dungeon.gif")
        r79 = Room("Floor 2 Room 10", "dungeon.gif")
        r80 = Room("Floor 2 Room 11", "dungeon.gif")
        r81 = Room("Floor 2 Room 12", "dungeon.gif")
        r82 = Room("Floor 2 Room 13", "dungeon.gif")
        r83 = Room("Floor 2 Room 14", "dungeon.gif")
        r84 = Room("Floor 2 Room 15 Encounter", "dungeon.gif")
        r85 = Room("Floor 2 Room 16", "dungeon.gif")
        r86 = Room("Floor 2 Room 17", "dungeon.gif")
        r87 = Room("Floor 2 Room 18", "dungeon.gif")
        r88 = Room("Floor 2 Room 19", "dungeon.gif")
        r89 = Room("Floor 2 Room 20", "dungeon.gif")
        r90 = Room("Floor 2 Room 21", "dungeon.gif")
        r91 = Room("Floor 2 Room 22 Encounter", "dungeon.gif")
        r92 = Room("Floor 2 Room 23", "dungeon.gif")
        r93 = Room("Floor 2 Room 24 Encounter", "dungeon.gif")
        r94 = Room("Floor 2 Room 25", "stairs.gif")
        r95 = Room("Floor 2 Room 26 Encounter", "dungeon.gif")
        r96 = Room("Floor 2 Room 27 Encounter", "dungeon.gif")
        r97 = Room("Floor 2 Room 28 Enounter", "dungeon.gif")
        r98 = Room("Floor 2 Room 29 Encounter", "dungeon.gif")

        r59.addExit("down", r70)
        r70.addExit("north", r71)
        r70.addExit("east", r72)
        r70.addExit("south", r73)
        r70.addExit("west", r74)
        r70.addExit("up", r59)
        r71.addExit("south", r70)
        r71.addExit("north", r79)
        r71.addExit("east", r76)
        r71.addExit("west", r75)
        r72.addExit("west", r70)
        r72.addExit("north", r76)
        r72.addExit("east", r80)
        r72.addExit("south", r77)
        r73.addExit("south", r81)
        r73.addExit("north", r70)
        r73.addExit("east", r77)
        r73.addExit("west", r78)
        r74.addExit("south", r78)
        r74.addExit("north", r75)
        r74.addExit("east", r70)
        r74.addExit("west", r82)
        r75.addExit("south", r74)
        r75.addExit("north", r94)
        r75.addExit("east", r71)
        r75.addExit("west", r92)
        r75.addEnemy("knight", 50, 10, 20)
        r76.addExit("south", r72)
        r76.addExit("north", r83)
        r76.addExit("east", r85)
        r76.addExit("west", r71)
        r76.addEnemy("knight", 50, 10, 20)
        r77.addExit("south", r88)
        r77.addExit("north", r72)
        r77.addExit("east", r86)
        r77.addExit("west", r73)
        r77.addEnemy("knight", 50, 10, 20)
        r78.addExit("south", r89)
        r78.addExit("north", r74)
        r78.addExit("east", r73)
        r78.addExit("west", r91)
        r78.addEnemy("knight", 50, 10, 20)
        r79.addExit("south", r71)
        r79.addExit("north", r95)
        r79.addExit("east", r83)
        r79.addExit("west", r94)
        r80.addExit("north", r85)
        r80.addExit("south", r86)
        r80.addExit("east", r96)
        r80.addExit("west", r72)
        r81.addExit("north", r73)
        r81.addExit("south", r97)
        r81.addExit("east", r88)
        r81.addExit("west", r89)
        r82.addExit("north", r92)
        r82.addExit("south", r91)
        r82.addExit("east", r74)
        r82.addExit("west", r98)
        r83.addExit("south", r76)
        r83.addExit("east", r84)
        r83.addExit("west", r79)
        r84.addExit("south", r85)
        r84.addExit("west", r83)
        r84.addEnemy("knight", 50, 10, 20)
        r85.addExit("north", r84)
        r85.addExit("south", r80)
        r85.addExit("west", r76)
        r86.addExit("north", r80)
        r86.addExit("south", r87)
        r86.addExit("west", r77)
        r87.addExit("north", r86)
        r87.addExit("west", r88)
        r88.addExit("north", r77)
        r88.addExit("east", r87)
        r88.addExit("west", r81)
        r89.addExit("north", r78)
        r89.addExit("east", r81)
        r89.addExit("west", r90)
        r90.addExit("north", r91)
        r90.addExit("east", r89)
        r91.addExit("north", r82)
        r91.addExit("south", r90)
        r91.addExit("east", r78)
        r91.addEnemy("knight", 50, 10, 20)
        r92.addExit("north", r93)
        r92.addExit("south", r82)
        r92.addExit("east", r75)
        r93.addExit("south", r92)
        r93.addExit("east", r94)
        r93.addEnemy("knight", 50, 10, 20)
        r94.addExit("south", r75)
        r94.addExit("east", r79)
        r94.addExit("west", r93)
        r95.addExit("south", r79)
        r95.addEnemy("knight", 50, 10, 20)
        r96.addExit("west", r80)
        r96.addEnemy("knight", 50, 10, 20)
        r97.addExit("north", r81)
        r97.addEnemy("knight", 50, 10, 20)
        r98.addExit("east", r82)
        r98.addEnemy("knight", 50, 10, 20)

        # Fortress Level 3
        r99 = Room("Floor 3 Stairway", "stairs.gif")

        r94.addExit("down", r99)
        r99.addExit("up", r94)

        # Fortress Level 4
        r100 = Room("Final Boss", "dungeon.gif")

        r99.addExit("down", r100)
        r100.addExit("up", r99)
        r100.addEnemy("big bad", 50, 25, 1000, True, True)

        # supplement code to add features to the created rooms

        # set the current room to r1
        Game.currentRoom = r99
        Game.previousRoom = r1

    # sets up the GUI
    def setupGameGUI(self):
        # organize and pack the GUI
        self.pack(fill=BOTH, expand=1)

        # setup player input (bottom)
        Game.gameplay_player_input = Entry(self, bg="white")
        Game.gameplay_player_input.bind("<Return>", self.processGame)
        Game.gameplay_player_input.pack(side=BOTTOM, fill=X)
        Game.gameplay_player_input.focus()

        # setup the image on the left of the display
        img = None
        Game.image = Label(self, width=WIDTH / 2, image=img)
        Game.image.pack(side=LEFT, fill=Y)
        Game.image.pack_propagate(False)  # don't let the img change the size of the window

        # setup the output on the right of the display
        Game.gameplay_text_frame = Frame(self, width=WIDTH / 2)
        Game.text = Text(Game.gameplay_text_frame, bg="lightgrey", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        Game.gameplay_text_frame.pack(side=RIGHT, fill=Y)
        Game.gameplay_text_frame.pack_propagate(False)

    def setupMenuGUI(self):
        # organize and pack the GUI
        self.pack(fill=BOTH, expand=1)

        # setup the player input (bottom)
        Game.menu_player_input = Entry(self, bg="white")
        Game.menu_player_input.bind("<Return>", self.processMenu)
        Game.menu_player_input.pack(side=BOTTOM, fill=X)
        Game.menu_player_input.focus()

        # setup text output on the right of the display
        Game.menu_text_frame = Frame(self, width=WIDTH)
        Game.text = Text(Game.menu_text_frame, bg="lightgrey", wrap=WORD, spacing1=2, state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        Game.menu_text_frame.pack()

    def setupEndGUI(self):
        # organize and pack the GUI
        self.pack(fill=BOTH, expand=1)

        # setup the player input (bottom)
        Game.menu_player_input = Entry(self, bg="white")
        Game.menu_player_input.bind("<Return>", self.processEnd)
        Game.menu_player_input.pack(side=BOTTOM, fill=X)
        Game.menu_player_input.focus()

        # setup text output on the right of the display
        Game.menu_text_frame = Frame(self, width=WIDTH)
        Game.text = Text(Game.menu_text_frame, bg="lightgrey", wrap=WORD, spacing1=2, state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        Game.menu_text_frame.pack()

    # sets the current room image
    def setRoomImage(self):
        if (Game.currentRoom == None):
            Game.img = PhotoImage(file="skull.gif")

        else:
            Game.img = PhotoImage(file=Game.currentRoom.image)

        Game.image.config(image=Game.img)
        Game.image.image = Game.img

    # sets the status displayed on the right of the GUI
    def setGameStatus(self, status):
        # clear the text widget
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        Game.text.tag_configure("center", justify='center')

        if (Game.currentRoom == None):
            Game.text.insert(END, "You are dead. You may quit.")
            Game.config(state=DISABLED)

        elif (Game.currentRoom.name == "Shop"):

            Game.shopTitle = Label(Game.text, text="Welcome to the Shop", font=("Arial Bold", 25))
            Game.shopTitle.pack()
            Game.goldLabel = Label(Game.text, text="You have: {} Gold".format(player.gold), font=("Arial", 10))
            Game.goldLabel.pack()

            Game.b1 = Button(Game.text, text="Great Sword", command=lambda: self.buy(1))
            Game.b1.pack()
            Game.b2 = Button(Game.text, text="Potion", command=lambda: self.buy(2))
            Game.b2.pack()
            Game.b3 = Button(Game.text, text="Key", command=lambda: self.buy(3))
            Game.b3.pack()
            Game.b4 = Button(Game.text, text="Dagger", command=lambda: self.buy(4))
            Game.b4.pack()
            Game.b5 = Button(Game.text, text="Bow", command=lambda: self.buy(5))
            Game.b5.pack()
            Game.b6 = Button(Game.text, text="Staff", command=lambda: self.buy(6))
            Game.b6.pack()

        elif(status == " "):
            Game.text.insert(END, "something")

        else:

            Game.text.insert(END, str(Game.currentRoom) + "\nYou are carrying: " + str(player.inventoryDisplay) + "\n\n" + "\n You have {} gold; you have {} reputation".format(player.gold, player.rating) + "\n\n" + status)
            Game.text.config(state=DISABLED)
            Game.text.tag_add("center", "1.0", "end")

            if (Game.previousRoom.name == "Shop"):
                Game.shopTitle.pack_forget()
                Game.goldLabel.pack_forget()
                Game.b1.pack_forget()
                Game.b2.pack_forget()
                Game.b3.pack_forget()
                Game.b4.pack_forget()
                Game.b5.pack_forget()
                Game.b6.pack_forget()

        Game.text.config(state=DISABLED)

    def setMenuStatus(self, status):
        # clear the text widget
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        Game.text.tag_configure("center", justify='center')

        if (status == ""):
            Game.text.insert(END, "NAME IN DEVELOPMENT")
            Game.text.insert(END, "\n" * 8 + "-Play-\n-Help-\n-Quit-")
            Game.text.config(state=DISABLED)

        else:
            Game.text.insert(END, status)
            Game.text.config(state=DISABLED)

        Game.text.tag_add("center", "1.0", "end")
        Game.text.config(state=DISABLED)

    def setEndStatus(self, status):
        # clear the text widget
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        Game.text.tag_configure("center", justify='center')  

        if (status == ""):
            Game.text.insert(END, "NAME IN DEVELOPMENT")
            Game.text.insert(END, "\n" * 8 + "-Play-\n-Help-\n-Quit-")
            Game.text.config(state=DISABLED)
            Game.text.insert(END, "something")

        Game.text.tag_add("center", "1.0", "end")
        Game.text.config(state=DISABLED)
          
        

    # plays the game
    def play(self):
        # add the rooms to the game
        self.createRooms()
        # configure the GUI
        self.setupGameGUI()
        # set the current room
        self.setRoomImage()
        self.setGameStatus("")

    def start(self):
        self.setupMenuGUI()
        self.setMenuStatus("")

    def end(self):
        Game.gameplay_player_input.destroy()
        Game.gameplay_text_frame.destroy()
        Game.image.destroy()
        self.setGameStatus(" ")
        
        self.setupEndGUI()
        self.setEndStatus(status = "")

    # processes the player's input
    def processGame(self, event):
        # set a default response
        response = "I don't understand. Try noun verb. Valid verbs are go, look and take."

        # get the command input from the GUI
        action = Game.gameplay_player_input.get()
        action = action.lower()

        # handle the end of the game
        if (Game.currentRoom == None):
            Game.player_input.delete(0, END)
            return

        # handle verbs and nouns
        words = action.split()

        if (len(words) == 2):
            verb = words[0]
            noun = words[1]

            # process go
            if (verb == "go"):
                # default response
                response = "Invalid exit."

                # check the currentRoom's exits
                if (noun in Game.currentRoom.exits):
                    if(Game.currentRoom.enemiesName == [] or Game.currentRoom.enemiesName == ["villager"]):
                       Game.previousRoom = Game.currentRoom
                       # If it's valid, update the current room
                       Game.currentRoom = Game.currentRoom.exits[noun]
                       # check if it's the boss room
                       if(Game.currentRoom.name == "Final Boss"):
                           Game.currentRoom.checkRating(player.rating)
                       # notify user that the room has changed
                       response = "Room changed."
                    else:
                        if (Game.currentRoom.exits[noun] == Game.previousRoom):
                            Game.previousRoom = Game.currentRoom
                            Game.currentRoom = Game.currentRoom.exits[noun]
                            
                        

            # process look
            elif (verb == "look"):
                # default response
                response = "I don't see that item."

                # check the currentRoom's items
                if (noun in Game.currentRoom.items):
                    response = Game.currentRoom.items[noun]

            # process take
            elif (verb == "take"):
                # default response
                response = "I don't see that item."

                # check currentRoom's grabbables
                for grabbable in Game.currentRoom.grabbables:
                    if (noun == grabbable):
                        # set the response
                        response = "{} grabbed".format(grabbable)
                        # remove it from the room's grabbables
                        Game.currentRoom.delGrabbable(grabbable)
                        break

            # process attack
            elif (verb == "attack"):
                # default response
                response = "I don't see that creature."

                # check currentRoom's creatures
                for enemy in Game.currentRoom.enemies:
                    n = len(Game.currentRoom.enemies)
                    x = Game.currentRoom.enemies[enemy]
                    if (noun == enemy):
                        # set the response
                        # calculate the attack sequence
                        Game.currentRoom.attack(enemy, 1, Game.currentRoom.enemiesDamage[enemy])
                        best_weapon = None
                        max_dmg = 0
                        for i in player.inventory:
                            if isinstance(i, Weapon):
                                if i.damage > max_dmg:
                                    max_dmg = i.damage
                                    best_weapon = i
                        pAttack = i.damage
                        response = "Attacked {} with {} for {} damage, took {}. You have {} hp remaining".format(enemy,
                                                                                                                 i.name,
                                                                                                                 pAttack,
                                                                                                                 Game.currentRoom.enemiesDamage[enemy],
                                                                                                                 player.hp)
                        # Check if the enemy was defeated
                        if (n > len(Game.currentRoom.enemies)):
                            player.gold += Game.currentRoom.enemiesGold[enemy]
                            if(Game.currentRoom.enemiesCheck[enemy] == False):
                                player.rating += 10
                            else:
                                player.rating += 50
                            if(enemy == "villager"):
                                player.rating -= 25
                            # set the response and break
                            response = "You defeated {}, gained {} gold".format(enemy, Game.currentRoom.enemiesGold[enemy])
                            Game.currentRoom.enemiesName.remove(enemy)
                            break
            
                        elif (player.hp <= 0):
                            Game.currentRoom = None
                        else:
                            if(x > Game.currentRoom.enemies[enemy] and enemy == "villager"):
                                Game.currentRoom.NPCs[enemy] = "You fiend!"
            
            elif (verb == "talk"):
                # default response
                response = "I don't see that NPC."

                # check currentRoom's creatures
                for NPC in Game.currentRoom.enemies:
                    if (noun == NPC):
                        # set the response
                        # calculate the attack sequence
                        response = Game.currentRoom.NPCs[NPC]


        # call the update for display
        self.setGameStatus(response)
        self.setRoomImage()
        Game.gameplay_player_input.delete(0, END)

    def processMenu(self, event):
        # set a default response
        response = "NAME IN DEVELOPMENT" + "\n" * 8 + "-Play-\n-Help-\n-Quit-" + "\n" * 8 + "I don't understand. Try one word. Valid words are play, help, and quit."

        # get the command input from the GUI
        action = Game.menu_player_input.get()
        action = action.lower()

        # handle verbs and nouns
        words = action.split()

        if (len(words) == 1):
            command = words[0]

            if command == "play":
                Game.menu_player_input.destroy()
                Game.menu_text_frame.destroy()
                g.play()

            elif command == "help":
                response = " "
                response += '#' * 80 + "\n"
                response += "To move around, type a command such as 'go' then any compass direction, \n"
                response += "such as 'east' that is displayed, on the menu to navigate \n"
                response += "the map of the cube puzzle.\n"
                response += "Inputs such as 'look' or 'take' will\n"
                response += "let you interact with items in the area displayed with 'you see'.\n"
                response += "Interacting with villagers or any other NPC\n"
                response += "will require you to type 'talk' followed by\n"
                response += "the name of the NPC.\n"
                response += "to initiate combat, type 'attack' then the name of the creature dsiplayed\n"
                response += "Please type in lowercase for an easier playthrough.\n\n"
                response += "Thanks for playing and have fun!\n"
                response += '#' * 80 + "\n"
                response += "     Type 'back' to return to the main menu.     \n"
                response += '#' * 80 + "\n"

            elif command == "back":
                response = ""

            elif command == "quit":
                sys.exit()

            # call the update for display
            Game.menu_player_input.delete(0, END)
            self.setMenuStatus(response)

    def processEnd(self, event):
        # get the command input from the GUI
        action = Game.menu_player_input.get()
        action = action.lower()
        response = "something"

    def buy(self, args):

        if args == 1:
            if player.gold >= weaponGreatSword.value:
                player.gold -= weaponGreatSword.value
                player.inventory.append(weaponGreatSword)
                player.inventoryDisplay.append(weaponGreatSword.name)
                print "You bought Great Sword"
            else:
                print "You dont have enough gold"
        if args == 2:
            if player.gold >= 10:
                player.gold -= 10
                player.inventory.append("Potion")
                print "You bought Potion"
            else:
                print "You dont have enough gold"
        if args == 3:
            if player.gold >= 25:
                player.gold -= 25
                player.inventory.append("Key")
                print "You bought Key"
            else:
                print "You dont have enough gold"
        if args == 4:
            if player.gold >= weaponDagger.value:
                player.gold -= weaponDagger.value
                player.inventory.append(weaponDagger)
                player.inventoryDisplay.append(weaponDagger.name)
                print "You bought Dagger"
            else:
                print "You dont have enough gold"

        if args == 5:
            if player.gold >= weaponBow.value:
                player.gold -= weaponBow.value
                player.inventory.append(weaponBow)
                player.inventoryDisplay.append(weaponBow.name)
                print "You bought Bow"
            else:
                print "You dont have enough gold"
        if args == 6:
            if player.gold >= weaponStaff.value:
                player.gold -= weaponStaff.value
                player.inventory.append(weaponStaff)
                player.inventoryDisplay.append(weaponStaff.name)
                print "You bought Staff"
            else:
                print "You dont have enough gold"

        Game.shopTitle.pack_forget()
        Game.goldLabel.pack_forget()
        Game.b1.pack_forget()
        Game.b2.pack_forget()
        Game.b3.pack_forget()
        Game.b4.pack_forget()
        Game.b5.pack_forget()
        Game.b6.pack_forget()

        Game.shopTitle = Label(Game.text, text="Welcome to the Shop", font=("Arial Bold", 25))
        Game.shopTitle.pack()
        Game.goldLabel = Label(Game.text, text="You have: {} Gold; you have {} reputation".format(player.gold, player.rating), font=("Arial", 10))
        Game.goldLabel.pack()
        Game.b1 = Button(Game.text, text="Great Sword", command=lambda: self.buy(1))
        Game.b1.pack()
        Game.b2 = Button(Game.text, text="Potion", command=lambda: self.buy(2), )
        Game.b2.pack()
        Game.b3 = Button(Game.text, text="Key", command=lambda: self.buy(3))
        Game.b3.pack()
        Game.b4 = Button(Game.text, text="Dagger", command=lambda: self.buy(4))
        Game.b4.pack()
        Game.b5 = Button(Game.text, text="Bow", command=lambda: self.buy(5))
        Game.b5.pack()
        Game.b6 = Button(Game.text, text="Staff", command=lambda: self.buy(6))
        Game.b6.pack()

##########################################################
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Text RPG")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.start()

# wait for the window to close
window.mainloop()

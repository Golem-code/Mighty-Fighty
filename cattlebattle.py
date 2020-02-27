import random
import time

inventory = []
consumables = []
hp = 100
atk = 25
mp = 0
gold = 10
silver = 30
xp = 0
speed = 5
sight = 5
gems = 0
level = 1
souls = 0

names1 = ["Reivod","Prollop","Pelow","Demund","Rakard","Deirag","Surrik","Carow","Gorit"]
names2 = ["Obnoxious","Obese","Ugly","Oblivious","Demonic","Filthy","Rude","Rabid","Stupid","Lonely"]
beginitems = ["sword","torch","key","shield"]

sword = "sword"
torch = "torch"
key = "key"
shield = "shield"

def cattlebattle():
    print("   (    ,       )(     )         ")
    print("   )\  ((  (/ (( ))  ((\  (   o  ")
    print(" ((( )((/)(_)/())(\ , )(_) )) o  ")
    print(" )\___))())\_))(_))/(_|()/((  o  ")
    print("((/ __/(_)_| |_| |_)| |_)(\)) o  ")
    print(" | |__/ _  |  _|  _|| | -_|   o  ")
    print(" _\___\__,_|\__|\__||_| __|_  o  ")
    print(" ______        _   _  | \     o  ")
    print("|      \.---.-| |_| |_| |-----.  ")
    print("|.  I   |  I  |  _|  _| |  -__|  ")
    print("|.      \___,_\___\___\_|_____|_ ")                                                           
    print("|:  I    \                      |")
    print("|::.. .  /  Reign Of Helliot    |")
    print("'-------'|______________________|")
    print("                                 ")
    
charclasses = ["knight","berserker","rogue","hunter"]
beginitem = random.choice(beginitems)
inventory.append(beginitem)
name1 = random.choice(names1)
name2 = random.choice(names2)
name = name1 + ' the ' + name2
charclass = random.choice(charclasses)
if sword in inventory:
    atk += 20
if torch in inventory:
    sight += 5
if shield in inventory:
    hp += 30
cattlebattle()
time.sleep(1)
print("After your extraordinary success in the league of sworos, you have been appointed commander of the kings army.")
time.sleep(1)
print("Although, King Morosoph and Queen Ignoramus, the leaders of the Kingdom of Mightifyon, have been assasinated!")
time.sleep(1)
print("This leaves their daughter, Princess Helliot in charge of the kingdom. The culprit is most likely the King of Cattelion.")
time.sleep(1)
print("You have been sent to the kingdom of Cattelion to fight in the arena and try to find some more information.")
time.sleep(1.5)
code = input("What is your name?\n")
if code == 'mega':
    level = 5
    gold = 200
    silver = 400
    gems = 100
    souls = 150
    speed = 50
    sight = 50
    hp = 100
    mp = 100
    xp = 300
    atk = 100
if code == 'golem':
    level = 10
    inventory.append('sword')
    inventory.append('axe')
    inventory.append('pitchfork')
    inventory.append('whip')
    inventory.append('torch')
    inventory.append('key')
    inventory.append('shield')
    consumables.append('meal')
if code == 'codelevel2':
    level = 2
if code == 'codelevel3':
    level = 3
if code == 'codelevel4':
    level = 4
if code == 'codexp':
    xp = 300
    
print("Greetings! You have been named " + name + ".")


def stats():
    time.sleep(1)
    print("~ S T A T I S T I C S ~")
    time.sleep(0.7)
    print(name)
    time.sleep(0.5)
    print("Class: {}".format(charclass))
    time.sleep(0.5)
    print("Level: {}".format(level))
    time.sleep(0.5)
    print("Inventory: {}".format(inventory))
    time.sleep(0.5)
    print("Consumables: {}".format(consumables))
    time.sleep(0.5)
    print("Gems: {}".format(gems))
    time.sleep(0.5)
    print("Gold: {}".format(gold))
    time.sleep(0.5)
    print("Silver: {}".format(silver))
    time.sleep(0.5)
    print("XP: {}".format(xp))
    time.sleep(0.5)
    print("MP: {}".format(mp))
    time.sleep(0.5)
    print("HP: {}".format(hp))
    time.sleep(0.5)
    print("Attack: {}".format(atk))
    time.sleep(0.5)
    print("Speed: {}".format(speed))
    time.sleep(0.5)
    print("Sight: {}".format(sight))


def lose():
    global xp
    print("YOU LOSE!")
    xpminus = random.randint(1,30)
    xp -= xpminus
    time.sleep(0.5)
    print("XP - {}".format(xpminus))
   
def win():
    global xp
    global gold
    global silver
    global gems
    global consumables
    ifgemadd = random.randint(1,5)
    goldadd = random.randint(0,3)
    silveradd = random.randint(1,10)
    xpadd = random.randint(1,30)
    print("You Win!")
    if ifgemadd == 3:
        gems += 1
        time.sleep(0.5)
        print("Gems + 1")
    elif ifgemadd == 4:
        gems += 2
        time.sleep(0.5)
        print("Gems + 2")
    else:
        pass
    gold += goldadd
    time.sleep(0.5)
    print("Gold + {}".format(goldadd))
    silver += silveradd
    time.sleep(0.5)
    print("Silver + {}".format(silveradd))
    xp += xpadd
    time.sleep(0.5)
    print("XP + {}".format(xpadd))
    if level >= 3:
        soulplus = 1
        if 'soulcatcher' in consumables:
            soulplus += 1
        souls += soulplus
        time.sleep(0.5)
        print("{} Soul".format(soulplus))

def draw():
    global xp
    global gold
    global silver
    print("It's a draw!")
    goldadd = random.randint(0,2)
    silveradd = random.randint(0,7)
    xpadd = random.randint(1,20)
    
    gold += goldadd
    time.sleep(0.5)
    print("Gold + {}".format(goldadd))
    silver += silveradd
    time.sleep(0.5)
    print("Silver + {}".format(silveradd))
    xp += xpadd
    time.sleep(0.5)
    print("XP + {}".format(xpadd))
    

def fight(nmehp1,nmehp2,nmespeed1,nmespeed2,nmeatk1,nmeatk2):
    enemytypes = ["Berserker","Barbarian","Demonlord","Dragonhunter","Housecarl","Henchman","Beastslayer"]
    enemynames1 = ["Blood","Bone","Beast","Death","Dark","Troll","Fist","Life","Skull","Rage","Rock","Satan","Knuckle"]
    enemynames2 = ["One","Blood","Bone","Slayer","Crusher","Destroyer","Maker","Hunter","Taker","Knuckle","Devil","Toe","Father","Killer","Hand","Arm","Demon","Man","Goblin"]
    enemyname1 = random.choice(enemynames1)
    enemyname2 = random.choice(enemynames2)
    nmename = enemyname1 + enemyname2
    nmetype = random.choice(enemytypes)
    global name
    global hp
    global atk
    global inventory
    global xp
    global speed
    global charclass
    global gems
    global gold
    global silver
    global mp
    global speed
    global sight
    global consumables
    yes = ["yes","y","Y"]
    no = ["no","n","N"]
    health = hp
    quick = speed
    attack = atk
    nmehp = random.randint(nmehp1,nmehp2)
    nmespeed = random.randint(nmespeed1,nmespeed2)
    time.sleep(1)
    print("===========================")
    time.sleep(0.5)
    print(nmename)
    time.sleep(0.5)
    print("ENEMY TYPE| {}".format(nmetype))
    time.sleep(0.5)
    print("DIFFICULTY| easy")
    time.sleep(0.5)
    print("ENEMY HP| {}".format(nmehp))
    time.sleep(0.5)
    print("ENEMY ATTACK| {}-{}".format(nmeatk1, nmeatk2))
    time.sleep(0.5)
    print("ENEMY SPEED| {}".format(nmespeed))
    time.sleep(0.5)
    print(consumables)
    time.sleep(0.5)
    print("If you have a consumable that you want to use now, name it below.")
    time.sleep(1)
    fight = input("Fight?\n")
    if fight in no:
        pass
    else:
        if fight == 'meal' and 'meal' in consumables:
            health += 30
            consumables.remove('meal')
            print("Plus 30 health for this fight.")
            time.sleep(0.5)
        if fight == 'nut' and 'nut' in inventory:
            quick += 2
            consumables.remove('nut')
            print("Plus 2 speed for the fight.")
        if fight == 'potion' and 'potion' in consumables:
            attack += 20
            consumables.remove('potion')
            print("Plus 20 attack for this fight")
            time.sleep(0.5)
        if fight == 'pillows' and 'pillows' in consumables:
            attack += 10
            consumables.remove('pillows')
            print("Plus 10 attack for this fight")
            time.sleep(0.5)
        if fight == 'ice' and 'ice' in consumables:
            health += 20
            consumables.remove('ice')
            print("Plus 20 health for this fight")
            time.sleep(0.5)
        if fight == 'pasta' and 'pasta' in consumables:
            quick += 2
            consumables.remove('pasta')
            print("Plus 2 speed for this fight")
            time.sleep(0.5)
        if nmespeed > quick: #nme start
            print("Enemy Starts:")
            while True:
                if fight == 'deathorb' and 'deathorb' in consumables:
                    win()
                    break
                nmeatk = random.randint(nmeatk1,nmeatk2) 
                
                time.sleep(1.5)
                health -= nmeatk
                print("Enemy deals {} damage".format(nmeatk))
                if health < 1:
                    time.sleep(1)
                    lose()
                    break
                elif health > 0:
                    pass
                time.sleep(1.5)
                print("Health: {}".format(health))
                nmehp -= attack
                time.sleep(1.5)
                print("You deal {} damage".format(atk))
                if nmehp < 1:
                    time.sleep(1)
                    win()
                    break
                elif nmehp > 0:
                    pass
                time.sleep(1.5)
                print("Enemy Health: {}".format(nmehp))
                
        elif nmespeed < quick: #u start
            print("You Start")
            while True:
                nmeatk = random.randint(10,30) 
                
                nmehp -= attack
                time.sleep(1.5)
                print("You deal {} damage".format(atk))
                if nmehp < 1:
                    time.sleep(1)
                    win()
                    break
                elif nmehp > 0:
                    pass
                time.sleep(1.5)
                print("Enemy Health: {}".format(nmehp))
                health -= nmeatk
                time.sleep(1.5)
                print("Enemy deals {} damage".format(nmeatk))
                if health < 1:
                    time.sleep(1)
                    lose()
                    break
                elif health > 0:
                    pass
                time.sleep(1.5)
                print("Health: {}".format(health))
        else:
            draw()
                
                
########################################################################
#       ##      ##      ###       ##  ###  ##      ##   ###  ##        #
#  # #  ##  ######  ###  ##  #######  ###  ##  ##  ##    ##  #####  ####
#  # #  ##      ##       ##  #######       ##      ##  #  #  #####  ####
#  # #  ##  ######   #  ###  #######  ###  ##  ##  ##  ##  # #####  ####
#  # #  ##      ##  ###  ##       ##  ###  ##  ##  ##  ###   #####  ####
########################################################################
merchtimes = 0
def merchant():
    
    global merchtimes
    global name
    global hp
    global atk
    global inventory
    global xp
    global speed
    global charclass
    global gems
    global gold
    global silver
    global mp
    global speed
    global sight
    global level
    merchtimes += 1
    time.sleep(1)
    print("  ,,,,,,     _____________________  ")
    time.sleep(.1)
    print(" / _  _ \   /                     \ ")
    time.sleep(.1)
    print("/ (o)(o) \ <  Welcome to my shop! | ")
    time.sleep(.1)
    print("#  ____  #  \_____________________/ ")
    time.sleep(.1)
    print("## \--/ ##                          ")
    time.sleep(.1)
    print(" ########                           ")
    time.sleep(.1)
    print("   ####                             ")
    time.sleep(2)
    print("__________________________________")
    time.sleep(.1)
    print(" |  1  ___     o            /@\ | ")
    time.sleep(.1)
    print(" |.(_) |_|//8 /^\  c=|----  \_/ | ")
    time.sleep(.1)
    print(' |""""""""""""""""""""""""""""""| ')
    time.sleep(.1)
    print(' | mm () 0o / & 0-, !.. /#| +ZX.| ')
    time.sleep(.1)
    print(' |""""""""_"""""""""""""""""""""| ')
    time.sleep(.1)
    print(' |   @  //_\\ _/\_  _   _._  |/ | ')
    time.sleep(.1)
    print(' |  / . "|_|" (oo) {@} /]_[\ /x|| ')
    time.sleep(.1)
    print(' |------------------------------| ')
    time.sleep(.1)
    print(' "                              " ')
    if merchtimes == 1:
        time.sleep(2)
        print("Greetings, young hero, I am the merchant. I come bringing the best goods from all across the land!")
        time.sleep(.5)
        print("You can exchange your hard earned silver for higher points such as Hp.")
        time.sleep(.5)
        print("I will give you high-quality items for gems, and useful consumables for gold!")
        time.sleep(.5)
        print("Remember, you can leave the shop any time by typing 'exit'.")
        time.sleep(2)
        
            
        print("Your Gold = {}".format(gold))
        time.sleep(.2)
        print("Your Silver = {}".format(silver))
        time.sleep(.2)
        print("Your Gems = {}\n".format(gems))
        time.sleep(.5)
        print("::::::STATS::::::")
        time.sleep(.5)
        print("1 HP = 1 Silver")
        time.sleep(.2)
        print("1 Attack = 1 Silver")
        time.sleep(.2)
        print("1 Speed = 5 Silver")
        time.sleep(.2)
        print("1 MP = 1 Silver")
        time.sleep(.2)
        print("1 Sight = 5 Silver")
        time.sleep(.2)
        print("10 XP = 1 Silver\n")
        print("::::::ITEMS::::::")
        time.sleep(.5)
        if 'torch' not in inventory:
            time.sleep(.2)
            print("Torch = 30 Gold")
        if 'sword' not in inventory:
            time.sleep(.2)
            print("Sword = 30 Gold")
        if 'shield' not in inventory:
            time.sleep(.2)
            print("Shield = 30 Gold")
        if 'key' not in inventory:
            time.sleep(.2)
            print("Key = 30 Gold")
        print(" ")
        time.sleep(.2)
        print(":::CONSUMABLES:::")
        time.sleep(.5)
        print("1 potion = 2 Gems")
        time.sleep(.2)
        print("1 meal = 2 Gems")
        time.sleep(.2)
        print("1 nut = 1 Gem")
        time.sleep(.5)
#################################################################################
        while True:
            print("Here's a list of the names of things for sale:")
            time.sleep(.5)
            print("hp, attack, speed, mp, sight, xp, torch, sword, shield, potion, meal, nut.")
            time.sleep(.5)
            print("Just enter the name of what you want to buy below")
            time.sleep(.5)
            print("Type 'exit' to leave shop.")
            time.sleep(.2)
            buy = input("What to buy? \n >")
            if buy == 'hp': #hp
                print("Plus 1 HP per silver")
                time.sleep(.5)
                amount = input("How many do you want to buy?\n >")
                amount = int(amount)
                if amount > silver or amount < 0:
                    print("You don't have enough silver.")
                else:
                    hp += amount
                    silver -= amount
                    print("Plus {} HP".format(amount))
                    time.sleep(1)
                    
            elif buy == 'attack': #attack
                print("Plus 1 Attack per silver")
                time.sleep(.5)
                amount = input("How many do you want to buy?\n >")
                amount = int(amount)
                if amount > silver or amount < 0:
                    print("You don't have enough silver.")
                else:
                    atk += amount
                    silver -= amount
                    print("Plus {} Attack".format(amount))
                    time.sleep(1)
                    
            elif buy == 'speed': #speed
                print("Plus 1 Speed per 5 silver")
                time.sleep(.5)
                amount = input("How many do you want to buy?\n >")
                amount = int(amount)
                if amount > silver or amount < 0:
                    print("You don't have enough silver.")
                else:
                    atk += amount
                    silver -= amount * 5
                    print("Plus {} Speed".format(amount))
                    time.sleep(1)
            elif buy == 'mp': #mp
                print("Plus 1 MP per silver")
                time.sleep(.5)
                amount = input("How many do you want to buy?\n >")
                amount = int(amount)
                if amount > silver or amount < 0:
                    print("You don't have enough silver.")
                else:
                    mp += amount
                    silver -= amount
                    print("Plus {} MP".format(amount))
                    time.sleep(1)
            elif buy == 'sight': #mp
                print("Plus 1 Sight per 5 silver")
                time.sleep(.5)
                amount = input("How many do you want to buy?\n >")
                amount = int(amount)
                if amount > silver or amount < 0:
                    print("You don't have enough silver.")
                else:
                    sight += amount
                    silver -= amount * 5
                    print("Plus {} Sight".format(amount))
                    time.sleep(1)
            elif buy == 'xp': #mp
                print("Plus 10 XP per silver")
                time.sleep(.5)
                amount = input("How many do you want to buy?\n >")
                amount = int(amount)
                if amount > silver or amount < 0:
                    print("You don't have enough silver.")
                else:
                    xp += amount * 10
                    silver -= amount
                    print("Plus {} XP".format(amount * 10))
                    time.sleep(1)
            elif buy == 'torch' and 'torch' not in inventory: #torch
                if gold >= 30:
                    print("The torch gives +5 sight and allows you to enter the cave.")
                    sure = input("Do you want to buy the torch?")
                    if sure == 'yes':
                        inventory.append("torch")
                        print("Torch bought.")
                        gold -= 30
                    else:
                        pass
                else:
                    print("You don't have enough gold, this isn't a charity y'know?")
            elif buy == 'sword' and 'sword' not in inventory: #sword
                if gold >= 30:
                    print("The sword gives +20 attack and allows you to fight beasts.")
                    sure = input("Do you want to buy the sword?")
                    if sure == 'yes':
                        inventory.append("sword")
                        print("Sword bought.")
                        gold -= 30
                    else:
                        pass
                else:
                    print("You don't have enough gold, this isn't a charity y'know?")
            elif buy == 'shield' and 'shield' not in inventory: #shield
                if gold >= 30:
                    print("The shield gives +30 hp and allows you to block arrows.")
                    sure = input("Do you want to buy the shield?")
                    if sure == 'yes':
                        inventory.append("shield")
                        print("Shield bought.")
                        gold -= 30
                    else:
                        pass
                else:
                    print("You don't have enough gold, this isn't a charity y'know?")

            elif buy == 'key' and 'key' not in inventory: #key
                if gold >= 30:
                    print("The key allows you to open chests and doors.")
                    sure = input("Do you want to buy the key?")
                    if sure == 'yes':
                        inventory.append("key")
                        print("Key bought.")
                        gold -= 30
                    else:
                        pass
                else:
                    print("You don't have enough gold, this isn't a charity y'know?")

            elif buy == 'potion': #potion
                if gems > 2:
                    print("Potions give you a boost of 20 attack at the beginning of a fight.")
                    sure = input("Do you want to buy a potion?")
                    if sure == 'yes':
                        consumables.append("potion")
                        print("You have bought a potion.")
                        gems -= 2
                    else:
                        pass
                else:
                    print("You're too poor, sorry.")
                    
            elif buy == 'meal': #meal
                if gems > 2:
                    print("Meals give you a boost of 30 hp at the beginning of a fight.")
                    sure = input("Do you want to buy a meal?")
                    if sure == 'yes':
                        consumables.append("meal")
                        print("You have bought a meal.")
                        gems -= 2
                    else:
                        pass
                else:
                    print("You're too poor, sorry.")

            elif buy == 'nut': #nut
                if gems > 2:
                    print("Nuts give you a boost of 2 Speed at the beginning of a fight.")
                    sure = input("Do you want to buy a nut?")
                    if sure == 'yes':
                        consumables.append("nut")
                        print("You have bought a nut.")
                        gems -= 2
                    else:
                        pass
                else:
                    print("You're too poor, sorry.")
            
            elif buy == 'exit': #exit
                break
            else:
                print("Sorry, I don't have that...")
#################################################################################
# ______   _______  _______  _______  _       
#(  __  \ (  ____ \(       )(  ___  )( (    /|
#| (  \  )| (    \/| () () || (   ) ||  \  ( |
#| |   ) || (__    | || || || |   | ||   \ | |
#| |   | ||  __)   | |(_)| || |   | || (\ \) |
#| |   ) || (      | |   | || |   | || | \   |
#| (__/  )| (____/\| )   ( || (___) || )  \  |
#(______/ (_______/|/     \|(_______)|/    )_)
                                                         
demontimes = 0       
def demon():
    global name
    global hp
    global atk
    global inventory
    global xp
    global speed
    global charclass
    global gems
    global gold
    global silver
    global mp
    global speed
    global souls
    global sight
    global level
    global demontimes
    global consumables
    demontimes += 1
    demonquotes = ["My name a Jeff!","# Geoffrey!!!##","Freddy Twohorn#","## Deeemond ###","Welcome Mortal!"]
    demonquote = random.choice(demonquotes)
    print("########################################")
    time.sleep(.2)
    print("#########/|##|\#########################")
    time.sleep(.2)
    print("########/ |##| \########################")
    time.sleep(.2)
    print("########\ _\/_ /########################")
    time.sleep(.2)
    print("####.###((*)(*))###.###{}#".format(demonquote))
    time.sleep(.2)
    print("####|\__( ____ )__/|####################")
    time.sleep(.2)
    print("####/___o\\\##//o___\####################")
    time.sleep(.2)
    print("###|   ,\_\  /_/,   |###################")
    time.sleep(.2)
    print("###|  |__,_\/_,__|  |###################")
    time.sleep(.2)
    print("####\___ _/()\_ ___/####################")
    time.sleep(.2)
    print("########\_/##\_/########################")
    time.sleep(.2)
    print("########################################")
    time.sleep(1)
    if demontimes == 1:
        print('''
Greeetings mortal... I am the almighty demon Jeff! I have come to the mortal
realm in search of souls. Throughout level 3 or higher, you win the soul of
everyone you kill in fights. You can then come here with them and exchange
them for your beloved pieces of metal you call currency.
I also have some exclusive items crafted in the forges of Hell that cannot be
found anywhere else!
        ''')
        time.sleep(2)
    print("Your souls: {}\n".format(souls))
    time.sleep(.5)
    print("1 Gold = 1 Soul")
    time.sleep(.5)
    print("5 Silver = 1 Soul")
    time.sleep(.5)
    print("1 Gem = 2 Souls\n")
    time.sleep(.5)
    print("Demontorch = 30 Souls")
    time.sleep(.5)
    print("Pitchfork = 20 Souls")
    time.sleep(.5)
    print("Whip = 15 Souls\n")
    time.sleep(1)
    while True:
        print("These are the names of what you can buy.")
        time.sleep(.5)
        print("gold, silver, gem, demontorch, pitchfork, whip.")
        time.sleep(.5)
        print("Just enter the name of what you want to buy below (Type 'exit' to leave).")
        time.sleep(.5)
        buy = input(" >")
        if buy == 'gold' and souls >= 1:
            sure = input("Trade a soul for a piece of gold?\n")
            if sure == 'yes':
                souls -= 1
                gold += 1
                print("+1 Gold")
            else:
                pass
        elif buy == 'sliver' and souls >= 1:
            sure = input("Trade a soul for five pieces of silver?\n")
            if sure == 'yes':
                souls -= 1
                silver += 5
            else:
                pass
        elif buy == 'gem' and souls >= 2:
            sure = input("Trade two souls for a gem?\n")
            if sure == 'yes':
                souls -= 2
                gems += 1
            else:
                pass
        elif buy == 'demontorch' and 'demontorch' not in inventory:
            if souls >= 30:
                print("The demontorch is a torch lit with demonfyre.\nIt gives +10 sight and is the only item which lets you see through everdark.\n(a darkness which cannot be penetrated by normal light")         
                sure = input("Buy the demontorch?\n")
                if sure == 'yes':
                    souls -= 7
                    inventory.append("demontorch")
                    print("Demontorch bought")
                    sight += 10
                else:
                    pass
        elif buy == 'pitchfork' and 'pitchfork' not in inventory:
            if souls >= 20:
                print("Useful for impaling people, the pitchfork can kill undead as well as allowing\nyou to fight against beasts if you don't have a sword.\nIt also adds 10 attack.")
                sure = input("Buy the pitchfork?")
                if sure == 'yes':
                    souls -= 5
                    inventory.append("pitchfork")
                    print("Pitchfork bought")
                    atk += 10
                else:
                    pass
        elif buy == 'whip' and 'whip' not in inventory:
            if souls >= 15:
                print("The whip is used mostly for torture, but  it also allows you to avoid imps.\It also gives you 10 attack.")
                sure = input("Buy the whip?")
                if sure == 'yes':
                    souls -= 6
                    inventory.append("whip")
                    print("Whip bought")
                    atk += 10
                else:
                    pass
            else:
                print("Sorry, you have to kill more people first.")
oracletimes = 0
#                      _      
#                     | |     
#  ___  _ __ __ _  ___| | ___ 
# / _ \| '__/ _` |/ __| |/ _ \
#| (_) | | | (_| | (__| |  __/
# \___/|_|  \__,_|\___|_|\___|
                             
                             
def oracle():
    global oracletimes
    if oracletimes == 0:
        oracletimes = 1
        print("Welcome, I am the oracle. I was gifted foresight by the gods in exchange for my eyes. I now serve the crown as an oracle, and I shall give you as much advise as I can find.")
    tips = ["The right door is number 3","Souls are more valuable than gold.","There is a valuable secret hidden behind the everdark.","The cake is a lie.","The demontorch is necessary for your quest.","The merchant will die soon.","You should buy all of the merchant's items before it is too late.","You need at least 30 MP to complete your quest."]
    tip = random.choice(tips)
    print("         __-----__         ")
    time.sleep(0.1)
    print("      .-'         '-.      ")
    time.sleep(0.1)
    print("    .'               '.    ")
    time.sleep(0.1)
    print("   /                   \   ")
    time.sleep(0.1)
    print("  /         /\          \   Nothing")
    time.sleep(0.5)
    print(" ;         |  \_         ;  is")
    time.sleep(0.5)
    print(" |         |  ' \        ;  permantent")
    time.sleep(0.5)
    print(" ;         )   ,_\       |  except")
    time.sleep(0.5)
    print(" ;        /    | '       ;  change.")
    time.sleep(0.1)
    print("  \      /      \        / ")
    time.sleep(0.1)
    print("   \     |       \      /  ")
    time.sleep(0.1)
    print("    '.    \       \   .'   ")
    time.sleep(0.1)
    print("      '-._|        \-'     ")
    time.sleep(0.1)
    print("          | |\      |      ")
    time.sleep(0.1)
    print("  ________/ | '.    /_________")
    time.sleep(1)
    print(tip)
    time.sleep(1.5)
#     _ _ _           
# ___|_| | |___ _ _ _ 
#| . | | | | . | | | |
#|  _|_|_|_|___|_____|
#|_|                  
pillowtimes = 0
def pillowman():
    global name
    global hp
    global atk
    global inventory
    global xp
    global speed
    global charclass
    global gems
    global gold
    global silver
    global mp
    global speed
    global sight
    global level
    global souls
    global pillowtimes
    global consumables
    pillowquotes = ["1+1=3","Jaski Good","Mmm... Ice!","HeSow","Quacky Attacky","'_'","Salve!","'-'",";-;"]
    pillowquote = random.choice(pillowquotes)
    print("\\\///\\\\\//   ")
    time.sleep(0.2)
    print("|  _   _ |  /  ")
    time.sleep(0.2)
    print("| (o) (o)| < {}".format(pillowquote))
    time.sleep(0.2)
    print("| (_____)|  \  ")
    time.sleep(0.2)
    print(" \  \-/  /     ")
    time.sleep(0.2)
    print("  \__,__/      ")
    time.sleep(1)
    if pillowtimes == 0:
        pillowtimes = 1
        print("Hello! I'm Pillowman! I'm a merchant, but instead of selling you stats, I buy them off you!")
        time.sleep(0.5)
        print("Although, I do have some special consumables that you might want to take a look at.")
        time.sleep(1)
        
    print(";sTatItiCS;\n")
    time.sleep(0.5)
    print("I'll give you 1 Silver for 1 HP,")
    time.sleep(0.2)
    print("1 Silver for 1 MP,")
    time.sleep(0.2)
    print("1 Silver for 1 Attack,")
    time.sleep(0.2)
    print("5 Silver for 1 Speed,")
    time.sleep(0.2)
    print("5 Silver for 1 Sight,")
    time.sleep(0.2)
    print("1 Silver for 10 XP,")
    time.sleep(0.2)
    print("1 Gold for 1 Soul,")
    time.sleep(0.2)
    print("or 5 Silver for 1 Gold.\n")
    time.sleep(0.2)
    print(";cOnSuMabLEs;\n;")
    time.sleep(0.5)
    print("Ice = 1 gem")
    time.sleep(0.2)
    print("Pillows = 1 gem")
    time.sleep(0.2)
    print("Pasta = 1 gem")
    time.sleep(1)
    while True:
        print("Heres a list of what you can sell (Type 'exit' to leave):")
        time.sleep(0.5)
        print("hp, mp, attack, speed, sight, xp, soul, gold.")
        time.sleep(0.2)
        print("And you can buy: ice, pillows, pasta.")
        time.sleep(0.2)
        sell = input('>>>')
        if sell == 'hp' and hp > 0:
            hp -= 1
            silver += 1
            print("1 HP sold for 1 silver")
        elif sell == 'mp' and mp > 0:
            mp -= 1
            silver += 1
            print("1 MP sold for 1 silver")
        elif sell == 'attack' and atk > 0:
            atk -= 1
            silver += 1
            print("1 Attack sold for 1 silver")
        elif sell == 'speed' and speed > 0:
            speed -= 1
            silver += 5
            print("1 speed sold for 5 silver")
        elif sell == 'sight' and sight > 0:
            sight -= 1
            silver += 5
            print("1 sight sold for 5 silver")
        elif sell == 'xp' and xp >= 10:
            xp -= 10
            silver += 1
            print("10 XP sold for 1 silver")
        elif sell == 'soul' and souls > 0:
            souls -= 1
            gold += 1
            print("1 Soul sold for 1 Gold")
        elif sell == 'gold' and gold > 0:
            gold -= 1
            silver += 5
            print("1 Gold sold for 5 silver")
        elif sell == 'ice':
            print("Ice is the healthiest meal ever! It gives you +20 health before a fight.")
            print("For lunch I eat 7 cubes of ice, a handful of hard spaghetti, and raw eggs mixed with sugar. Buy Ice?")
            ifbuy = input(">")
            if ifbuy == 'yes' and gems >= 1:
                consumables.append('ice')
                print("You've bought frozen water!!!")
                gems -= 1 
            else:
                pass
        elif sell == 'pillow' or sell == 'pillows':
            print("Perfect for sleeping with. Pillows give you +10 attack before a fight. Buy pillows?")
            ifbuy = input(">")
            if ifbuy == 'yes' and gems >= 1:
                consumables.append('pillows')
                print("You've bought pillows!")
                gems -= 1
            else:
                pass
        elif sell == 'pasta' or sell == 'spaghetti':
            print("Raw, rock hard spaghetti, my favourite snack. Gives you +2 speed before a fight. Buy pasta?")
            ifbuy = input(">")
            if ifbuy == 'yes' and gems >= 1:
                consumables.append('pasta')
                print("You've bought pasta!")
                gems -= 1
            else:
                pass
        else:
            break
# _  _  _ _______  ______ _______ _______ _______ _______
# |  |  | |______ |  ____ |______ |_____| |       |______
# |__|__| |______ |_____| |       |     | |_____  |______
                                                        
wegtimes = 0           
def wegface():
    global name
    global hp
    global atk
    global inventory
    global xp
    global speed
    global charclass
    global gems
    global gold
    global silver
    global mp
    global speed
    global sight
    global level
    global souls
    global wegtimes
    global consumables
    wegquotes = ["Jeff","I Want Candy","Poniferus","WAGAMAMA!","Billy Time!","Eggy, Weggy, Weggggyy"]
    wegquote = random.choice(wegquotes)
    print("    _____    ")
    time.sleep(0.2)
    print(" __|     |__ ")
    time.sleep(0.2)
    print("|___________|")
    time.sleep(0.2)
    print("  #########   < {}".format(wegquote))
    time.sleep(0.2)
    print("  #########  ")
    time.sleep(0.2)
    print("   #######   ")
    time.sleep(0.2)
    print("    #####    ")
    time.sleep(1)
    if wegtimes == 0:
        wegtimes = 1
        print("I am Wegface, I was once a successful executioner and woodcutter. However, I accidently cut a tree down on top of my head one day.")
        time.sleep(0.5)
        print("I then awoke in the terrible pits of Tartarus, where it was Fiery Hot but Icy Cold.")
        time.sleep(0.2)
        print("I climbed up from the dark depths of the underworld, losing my face in the attempt, but I finally arrived here, on the surface.")
        time.sleep(0.2)
        print("I have brought with me some items from Tartarus, crafted with darkness and despair by the servants of death.")
        time.sleep(1)
    print("ooooooooooooooooooo-consumables-oooooooooooooooooooooo")
    time.sleep(0.2)
    print("deathorb = 3 gems")
    time.sleep(0.2)
    print("soulcatcher = 1 gem")
    time.sleep(0.2)
    print("oooooooooooooooooooooo-items-oooooooooooooooooooooooooo")
    time.sleep(0.2)
    print("axe = 30 gold")
    time.sleep(0.2)
    print("scythe = 50 gold")
    time.sleep(0.5)
    while True:
        print("You can buy (Type 'exit' to leave):")
        time.sleep(0.2)
        print("deathorb, soulcatcher, axe, scythe")
        time.sleep(0.2)
        buy = input("What to buy?")
        if buy == 'deathorb':
            print("A Deathorb will immediately kill your enemy in a fight.")
            surebuy = input("Buy deathorb?")
            if surebuy == 'yes' and gems >= 3:
                consumables.append('deathorb')
                gems -= 3
                print("Deathorb bought.")
            else:
                pass
        elif buy == 'soulcatcher':
            print("A soulcatche doubles the amount of souls gained in a fight.")
            surebuy = input("Buy soulcatcher?")
            if surebuy == 'yes' and gems >= 1:
                consumables.append('soulcatcher')
                gems -= 1
                print("Soulcatcher bought.")
            else:
                pass
        elif buy == 'axe':
            print("An executioner's axe, won't only let you fight beasts, but allows you to always win!")
            surebuy = input("Buy axe?")
            if surebuy == 'yes' and gold >= 30 and 'axe' not in inventory:
                inventory.append('axe')
                gold -= 30
                print("Axe bought.")
            else:
                pass
        elif buy == 'scythe':
            
            print("The reaper's scythe, allows you to kill enemies and take their souls in the cave or forest.")
            surebuy = input("Buy scythe?")
            if surebuy == 'yes' and gold >= 50 and 'scythe' not in inventory:
                inventory.append('scythe')
                gold -= 50
                print("Scythe bought.")
            else:
                pass
        else:
            break

def beast():
    global name
    global hp
    global atk
    global inventory
    global xp
    global speed
    global charclass
    global gems
    global gold
    global silver
    global mp
    global speed
    global sight
    global level
    global souls
    global foretimes
    global consumables
    print("A deadly beast stands before you, the likes of which you have never seen before.")
    if 'sword' not in inventory or 'axe' not in inventory or 'pitchfork' not in inventory:
        time.sleep(0.5)
        print("Without a weapon, you flee with fear.")
        time.sleep(0.5)
    else:
        time.sleep(0.5)
        print("With your weapon, you charge toward the beast.")
        poss = random.randint(0,1)
        if poss == 0 and 'axe' not in inventory:
            lose()
        elif poss == 1 or 'axe' in inventory:
            win()
def treasure():
    global name
    global hp
    global atk
    global inventory
    global xp
    global speed
    global charclass
    global gems
    global gold
    global silver
    global mp
    global speed
    global sight
    global level
    global souls
    global foretimes
    global consumables
    print("You see a treasure chest before you.")
    time.sleep(0.5)
    silverplus = random.randint(1,10)
    goldplus = random.randint(1,5)
    gemplus = random.randint(0,1)
    if 'key' in inventory:
        print("You have a key, so you're able to open the chest.")
        silver += silverplus
        gold += goldplus
        gems += gemplus
        print("Plus {} silver".format(silverplus))
        time.sleep(0.5)
        print("Plus {} gold".format(goldplus))
        time.sleep(0.5)
        print("Plus {} gems".format(gemplus))
        time.sleep(0.5)
    else:
        prin("You should buy a key bru.")
def cake():
    global hp
    print("You see a piece of cake before you.")
    time.sleep(0.5)
    eatit = input("Eat It?\n")
    if eatit == 'no':
        print("You leave empty handed.")
    else:
        print("THE CAKE IS A LIE, YOU IDIOT!")
        time.sleep(0.5)
        hp -= 50
        print("HP minus 50, moron")
        
        
    
foretimes = 0            
def forest():
    global name
    global hp
    global atk
    global inventory
    global xp
    global speed
    global charclass
    global gems
    global gold
    global silver
    global mp
    global speed
    global sight
    global level
    global souls
    global foretimes
    global consumables
    
    happens = ["beast","treasure","cake","nothing","fight","imp"]
    happen = random.choice(happens)
    if foretimes == 0:
        foretimes = 1
        print("The forest has been in the kingdom for thousands of years, said to be haunted by the spirits of the kings of cattelion. It is crawling with monsters and tricks.")
    print("A deep, dark forest lay before you, full of beasts and spirits.")
    if 'torch' not in inventory:
        print("The forest is too dark without a torch...")
    elif 'torch' in inventory:
        enter = input("Luckily you have a torch, enter forest?\n")
        if enter == 'yes':
            if happen == 'beast':
                beast()
            elif happen == 'treasure':
                treasure()
            elif happen == 'cake':
                cake()
            elif happen == 'nothing':
                print("You found nothing at all...")
            elif happen == 'fight':
                print("You see an enemy.")
                fight(10,130,1,7,1,60)
            elif happen == 'imp':
                print("You spot a fat little imp in the sky.")
                time.sleep(0.5)
                if 'whip' not in inventory:
                    print("The imp comes down and tears of your head because you haven't got a whip yet, you dumbass.")
                    hp -= 10
                    time.sleep(0.5)
                    print("Minus 10 HP")
                elif 'whip' in inventory:
                    print("Luckily, you have a whip, the imp flees.")
                    hp += 3
                    time.sleep(0.5)
                    print("Plus 3 HP")
                  
                    
        else:
            pass
def everdark():
    global name
    global hp
    global atk
    global inventory
    global xp
    global speed
    global charclass
    global gems
    global gold
    global silver
    global mp
    global speed
    global sight
    global level
    global souls
    global consumables
    while True:
        print("With a demontorch, you descend into the everdark................")
        time.sleep(1)
        print("There is a big, hard door blocking the passage.")
        time.sleep(1)
        if 'key' not in inventory:
            print("You can't open the door because you don't have a key.")
            break
        elif 'key' in inventory:
            print("You open the door with your key.")
            time.sleep(0.5)
        print("Behind the door is a particularly dangerous looking undead warrior.")
        time.sleep(0.5)
        if 'pitchfork' not in inventory:
            print("Without a pitchfork, you can't kill undead.")
            break
        elif 'pitchfork' in inventory:
            print("You kill the undead warrior with your pitchfork.")
            time.sleep(0.5)
        print("There are a long set of stairs before you, you descend them.")
        time.sleep(0.5)
        print("An old man sits on the ground before you.")
        time.sleep(0.5)
        print("OLD MAN| Well hello, are you wanting to get past then?")
        time.sleep(0.5)
        print("YOU| Yes")
        time.sleep(0.5)
        print("Well I'm gonna need five silver for that...")
        time.sleep(0.5)
        paybribe = input("Pay the bribe?\n")
        if paybribe == 'yes':
            print("You give the man 5 silver and he gives you 5 gold in return.")
            silver -= 5
            gold += 5
            time.sleep(0.5)
            print("Confused, you continue.")
            time.sleep(0.5)
        else:
            print("You can't get past the old man.")
            break
        print("Below this is an entire room of imps. A particular ugly looking one begins to talk.")
        time.sleep(0.5)
        print("IMP| Ahr, Mortal, let's eat 'em")
        time.sleep(0.5)
        print("The rest of the imps cheered with approval")
        time.sleep(0.5)
        print("IMP| We'll tear out your throat, bite off your nails, crush your toes.")
        time.sleep(1)
        print("YOU| Who are you?!")
        time.sleep(0.5)
        print("IMP| I am Lowarrrn, the king of the imps, and this 'ere is meh brother, Samon, he's the commander of the army!")
        time.sleep(0.5)
        if 'whip' not in inventory:
            print("Without a whip, the tear you apart.")
            break
        elif 'whip' in inventory:
            print("You draw the whip from your belt and lash one of the round the face with it.")
            time.sleep(0.5)
            print("The rest flee with horror, screaming and screeching.")
            time.sleep(0.5)
        print("Three doors lay before you. You can only open one, make sure it's the right one.")
        time.sleep(0.5)
        whichdoor = input("Open which door? (1,2,3)\n")
        if whichdoor == 3:
            print("Right door, you continue.")
            time.sleep(0.5)
        else:
            print("WRONG DOOR, YOU SHOULD'VE LISTENED TO THE ORACLE.")
            break
#heed wid da warnin' new day iz dawnin'
#grympu the third
        print("A funny looking fairy flies before you.")
        time.sleep(0.5)
        print("FAIRY| I'm Jay bird, I'm a magical flappy fairy")
        time.sleep(0.5)
        print("YOU| And?")
        time.sleep(0.5)
        print("FAIRY| I can sell you MP here, cuz you're gonna need it later...")
        time.sleep(0.5)
        print("YOU| Great!")
        time.sleep(0.5)
        print("FAIRY| Buuut, I can only sell you 10 MP, no more no less.")
        time.sleep(0.5)
        buymp = input("Buy 10 MP for 10 silver?")
        if buymp == 'yes':
            mp += 10
            silver -= 10
        else:
            print("Seeya then...")
            time.sleep(0.5)
        print("You finally get to the end of the everdark.")
        time.sleep(0.5)
        print("Before you is a large black orb, the EverOrb!")
        time.sleep(0.5)
        print("However, you need 30 MP to be able to hold such power!!!")
        time.sleep(0.5)
        if mp >= 30:
            print("Luckily you have enough!")
            time.sleep(0.5)
        else:
            print("Oh well... You don't have enough...")
            time.sleep(0.5)
            break
        print("You've got the everorb! But, of course, nothing can just end that easily can it?")
        time.sleep(0.5)
        print("To leave the everdark, you must have a shield and a scythe, for no particular reason other than to be annoying.")
        time.sleep(0.5)
        if scythe not in inventory and shield not in inventory:
            print("Oh dear, that was a bit of a faff for nothing, wasn't it?")
            time.sleep(0.5)
            break
        else:
            print("Well that was lucky!")
        time.sleep(1)
        print("You complete your quest, you give the everorb to Queen Helliot, she kills old king cattelion with it, and everything is well and good again!")
        time.sleep(0.5)
        print("Or is it?")
        time.sleep(0.5)
        break
        quit()
#{{{  "][" {()} {()} ][,,  }}}
cavetimes = 0
def cave():
    global name
    global hp
    global atk
    global inventory
    global xp
    global speed
    global charclass
    global gems
    global gold
    global silver
    global mp
    global speed
    global sight
    global level
    global souls
    global cavetimes
    global consumables
    
    happens = ["beast","treasure","cake","nothing","fight","souls","thief","everdark"]
    happen = random.choice(happens)
    if cavetimes == 0:
        cavetimes = 1
        print("A dark, wet and soggy cavern full of bats, rats, and foul smells. Sometimes, in a corner of the cave lies the enchanted everdark, a darkness that is so black that normal fire cannot penetrate it.")
    print("A deep, dark cave lay before you, full of beasts and spirits.")
    if sight < 15:
        print("You need more sight to enter the cave.")
    elif sight >= 15:
        enter = input("Luckily you have enough sight, enter cave?\n")
        if enter == 'yes':
            if happen == 'beast':
                beast()
            elif happen == 'treasure':
                treasure()
            elif happen == 'cake':
                cake()
            elif happen == 'nothing':
                print("You found nothing at all...")
            elif happen == 'fight':
                print("You see an enemy.")
                fight(1,200,1,20,1,100)
            elif happen == 'souls':
                print("Three souls drift forlornly toward you.")
                souls += 3
                time.sleep(0.5)
                print("Plus 3 souls")
            elif happen == 'thief':
                print("In a flash, a thief jumps out of the dark and steals some gold and silver.")
                gold -= 5
                silver -= 5
                time.sleep(0.5)
                print("Silver minus 5, gold minus 5")
            elif happen == 'everdark':
                print("This is dark that cannot be penetrated by fire, you must use demonfire.")
                if 'demontorch' in inventory:
                    pass
                else:
                    everdark()
        else:
            pass

#who stunks the stankiest turd in town?    
#    __                       
#   / /_  ____  ____ ___  ___ 
#  / __ \/ __ \/ __ `__ \/ _ \
# / / / / /_/ / / / / / /  __/
#/_/ /_/\____/_/ /_/ /_/\___/ 
                                
def home():
    global name
    global hp
    global atk
    global inventory
    global xp
    global speed
    global charclass
    global gems
    global gold
    global silver
    global mp
    global speed
    global sight
    global level
    while True:
        time.sleep(0.5)
        print(" ,___,           _    ")
        print(" (o,o)          (_)   ")
        print(" /)__)                ")    
        print('--"-"-------------------------------------------')
        time.sleep(1)
        print("Type 'fight' to battle in the arena.")
        time.sleep(0.5)
        print("Type 'stats' to view your points and currency.")
        time.sleep(0.5)
        if level < 4:
            print("Type 'merchant' to see the merchant's shop.")
            time.sleep(0.5)
        print("Type 'oracle' to speak to the oracle.")
        time.sleep(0.5)
        if level >= 3:
            print("Type 'demon' to see Jeff the Demon.")
            time.sleep(0.5)
        if level >= 2:
            print("Type 'pillowman' to see the pillowman.")
            time.sleep(0.5)
            print("Type 'forest' to go to the forest.")
            time.sleep(0.5)
        if level >= 4:
            print("Type 'wegface' to buy off wegface")
            time.sleep(0.5)
        if xp >= 300:
            print("Type 'upgrade' to upgrade to the next level.")
        #meirdiga    
        do = input("What to do?\n >")
        if do == 'fight' and level == 1:
            fight(10,110,1,10,1,30)
        elif do == 'fight' and level == 2:
            fight(10,150,1,10,1,60)
        elif do == 'fight' and level == 3:
            fight(10,175,1,11,40,70)
        elif do == 'fight' and level == 4:
            fight(10,200,1,10,10,100)
        elif do == 'fight' and level == 5:
            fight(10,300,1,20,10,200)
        elif do == 'stats':
            stats()
        elif do == 'merchant' and level < 4:
            merchant()
        elif do == 'merchant' and level >= 4:
            print("Unfortunately, the merchant seems to have been killed by king cattelion for helping you in your quest.")
            time.sleep(1)
            print("And now, your quest has changed drastically.")
            time.sleep(0.5)
            print("The queen has ordered you to seek out the EverOrb, whatever that is.")
            time.sleep(0.5)
            print("Apparently, it has the power to kill anyone she wants it to.")
            time.sleep(0.5)
            print("Useful, huh?")
            time.sleep(0.3)
            print("The only problem is, you have no fekin' idea were the hell it is.")
            time.sleep(0.5)
        elif do == 'oracle':
            oracle()
        elif do == 'pillowman' and level >= 2:
            pillowman()
        elif do == 'forest' and level >= 2:
            forest()
        elif do == 'demon' and level >= 3:
            demon()
        elif do == 'wegface' and level >= 4:
            wegface()
        elif do == 'upgrade' and xp >= 300:
            xp -= 300
            level += 1
            print("You now have level {}!".format(level))
        else:
            print("???")


stats()    
home()


#------------------------------END----------------------------------------
'''
    global name
    global hp
    global atk
    global inventory
    global xp
    global speed
    global charclass
    global gems
    global gold
    global silver
    global mp
    global speed
    global sight
    global level
    global consumables
'''



    
'''HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH'''

import random
import time



def mightyfighty():
    print("'..~~~~~~~~~~~~~~~\*^*/~~~~~~~~~~~~~~~~~..")
    print("'   _    _  ___   __   _  _ _____ _   _  '")
    print("'   |\  /|   |   |     |  |   |   |   |  '")
    print("'   | \/ |   |   | __  |__|   |    \ /   '")
    print("'   |    |  _|_  |__|  |  |   |     |    '")
    print("'==                                    =='")
    print("' _____  _   _____  _   _   _____  __  __'")
    print("'/  __/ / \ /  __/ / \ / \ /__ __\ \ \/ /'")
    print("'| ___\ | | | |___ | |_| |   / \    \  / '")
    print("'| |    | | | |/ / | | | |   | |    / /  '")
    print("'\_|    \_/ \___/  \_/ \_/   \_/   /_/   '")
    print("'~~~~~~~~~~~~LEAGUE OF SWOROS~~~~~~~~~~~~'")
    print("              _                           ")
    print("        /\___| /________________          ")
    print("       < |___|@|_________________\        ")
    print("        \/   |_\                          ")
    print("                                          ")


no = ["no","NO","n","No","N"]
yes = ["yes","YES","y","Yes","Y"]
answers = ["fight","shop","stats",]
shopstuff = ["health","attack","potion","xp","exit","upgrade"]
points = ["hp","atk","xp","gold",]

hp = random.randint(50,100)
health = hp
atk = random.randint(25,50)
xp = 0
gold = random.randint(1,10)
potion = 0
level = 1

titles1 = ["Rainbow","Fluffy","Sparkly","Demonic","Evil","Dark","Confused","Lonely","Magical","Rabid","Beastly","Stinky","Slimey","Boring"]
titles2 = ["Unicorn","Fairy","Pixie","Demon","Dragon","Necromancer","Faun","Knight","Pirate","Beast","Angel","Skeleton","Ghost","Blanket","Witch"]
title1 = random.choice(titles1)
title2 = random.choice(titles2)
title = title1 + " " + title2
mightyfighty()
time.sleep(1)
print("Greetings! King Morosoph has entered you into 'The League Of Sworos'!")
time.sleep(1)
print("You must fight in the arena against the badfolk for the king's entertainment.")
time.sleep(1)
print("If you are strong enough, you will be appointed to commander of the kings army!")
time.sleep(1)
print("For variation, you have been given a random title and random stats, Good Luck!")
time.sleep(1)

 
name = input("So, what is your name, hero?\n")

if name == 'codeall':
    gold += 100
    xp += 500
    atk += 100
    hp += 100
    potion += 10
    print('+10 potion, +100 gold, +500 xp, +100 atk, +100 hp!!!')
if name == 'codexp':
    xp += 200
    print('+200 xp')
    time.sleep(1)
if name == 'codexpmega':
    print('+800 xp')
    xp += 800
if name == 'codexpultra':
    print('+2000 xp')
    xp += 2000
if name == 'codelevel':
    print('level 2')
    level += 1
if name == 'codepotion':
    print('+1 potion')
    potion += 1
if name == 'codelevelmega':
    print('level 3')
    level += 2

print("Welcome! You have been given the title of {}!".format(title))
def info():
    global xp
    print('''

Mighty Fighty is my first fully-functional game made from scratch with python.
It is a text-based 'mini-game' built primarily on loops, functions, and randomness.
In the beginning, the code generates a random name, hp, attack, and gold.
Gold and xp is then gained in 'fights' in which a random enemy is generated with random stats.
You can use the gold to go to the shop and buy health, potions, attack, xp and upgrades.
When enough xp is gained, an upgrade is available, along with more features such as the oracle, quickfights, and medium difficulty fights.
The game finishes at level 4.

    ''')
    xp += 1
    
def stats():
    global title
    global hp
    global atk
    global xp
    global gold
    global potion
    global level
    print("STATS [")
    time.sleep(1)
    print(title)
    time.sleep(1)
    print("HP| {}".format(hp))
    time.sleep(1)
    print("ATTACK| {}".format(atk))
    time.sleep(1)
    print("XP| {}".format(xp))
    time.sleep(1)
    print("GOLD| {}".format(gold))
    time.sleep(1)
    print("POTIONS| {}".format(potion))
    time.sleep(1)
    print("LEVEL| {}".format(level))
    time.sleep(1)
    print(" ]")
####################################################
def enemy(xppri, xpsec, nmehp, nmeatk1, nmeatk2, difficulty, goldpri, goldsec):
    enemytypes = ["Skeleton","Massive Eye","Foot","Troll","Ogre","Runtchild","Fishmaster"]
    enemynames1 = ["Skelly","Skellington","Skellidor","Gobliris","Ogrin","Orcrud","Trollop","Trollit","Skelpy","Goblind","Gobber","Bogger","Gobbit"]
    enemynames2 = ["Skelling","Runt","Ogre","Gobble","Gobli","Trot","Toe","Troll","Skelpy","Kelpie","Orange","Foot","Beastly"]
    enemynames3 = ["child","breath","mouth","foot","toe","finger","face","arm","brain","torch","blood","neck","hammer","beast","kelp","ton","winky","tit"]
    enemytype = random.choice(enemytypes)
    enemyname1 = random.choice(enemynames1)
    enemyname2 = random.choice(enemynames2)
    enemyname3 = random.choice(enemynames3)
    enemyname = enemyname1 + ' ' + enemyname2 + enemyname3
    enemynamecaps = enemyname1.upper()
    
    global xp
    global gold
    global hp
    global health
    global atk
    global no
    global yes
    global xpplus

    xpplus = random.randint(xppri,xpsec)
    enemyhp = random.randint(25,nmehp)
    enemyatk = random.randint(nmeatk1,nmeatk2)
    print("===========================")
    print(enemyname)
    time.sleep(1)
    print("ENEMY TYPE| {}".format(enemytype))
    time.sleep(1)
    print("DIFFICULTY| {}".format(difficulty))
    time.sleep(1)
    print("ENEMY HP| {}".format(enemyhp))
    time.sleep(1)
    print("ENEMY ATTACK| {}".format(enemyatk))
    time.sleep(1)
    fight = input("FIGHT?\n")
    if fight in no:
        pass
    elif fight in yes:
        print(title + ' vs ' + enemyname)
        time.sleep(2)
        print("BATTLE HAS BEGUN!")
        while enemyhp > 0 or health > 0:
            health -= enemyatk
            time.sleep(2)
            print(enemynamecaps + " HITS YOU (you lose {} health)".format(enemyatk))
            if health < 1:
                time.sleep(2)
                print("YOU DIE!")
                time.sleep(2)
                print("YOU LOSE!")
                xp -= xpplus
                time.sleep(1)
                print("-{} XP".format(xpplus))
                health = hp
                break
            time.sleep(2)
            print("HEALTH| {}".format(health))
            enemyhp -= atk
            time.sleep(2)
            print("YOU HIT " + enemynamecaps + "(enemy loses {} health)".format(atk))
            if enemyhp < 1:
                time.sleep(2)
                print(enemynamecaps + " DIES!")
                time.sleep(2)
                print("YOU WIN!")
                xp += xpplus
                time.sleep(1)
                print("+{} XP".format(xpplus))
                goldplus = random.randint(goldpri,goldsec)
                gold += goldplus
                time.sleep(1)
                print("+{} GOLD".format(goldplus))
                health = hp
                break
            time.sleep(2)
            print(enemynamecaps + " HEALTH| {}".format(enemyhp))
##################################################################quickfight
def quickfight():
    global hp
    global xp
    global atk
    global gold
    global qhealth
    print("QUICKFIGHT")
    time.sleep(1)
    qenemyhp = random.randint(50,100)
    qenemyatk = random.randint(25,65)
    qhealth = hp
    while True:
        qenemyhp -= atk
        if qenemyhp < 1 and qhealth > 0:
            print("YOU WIN!!!")
            xp += 10
            gold += 2
            time.sleep(1)
            print("XP +10")
            time.sleep(1)
            print("GOLD +2")
            break
        qhealth -= qenemyatk
        if qhealth < 1 and qenemyhp > 0:
            print("YOU LOSE!!!")
            xp -= 20
            time.sleep(1)
            print("XP -20")
            break
        

    

   # if atk > qenemyhp:
       # time.sleep(1)
   #     print("YOU WIN!!!")
      #  gold += 2
    #elif qenemyatk > hp:
     #   time.sleep(1)
    #    print("YOU LOSE!!!")
    #    xp -= 20
    #elif qenemyhp < hp:
        #time.sleep(1)
        #print("YOU WIN!!!")
       # gold += 2
   # else:
    #    time.sleep(1)
     #   print("YOU LOSE!!!")
      #  xp -= 20
#######################################################chance
def chance():
    global xp
    global hp
    global atk
    global gold
    global potion
    sure = input("Are you sure you want to take a chance? You might lose more than you gain.\n")
    if sure in yes:
        randxp = random.randint(-30,30)
        randhp = random.randint(-5,5)
        randatk = random.randint(-5,5)
        randgold = random.randint(-5,5)
        randpotion = random.randint(-2,2)

        xp += randxp
        hp += randhp
        atk += randatk
        gold += gold
        potion += randpotion
        
        print("The odds have given you:")
        time.sleep(2)
        print("{} XP".format(randxp))
        time.sleep(1)
        print("{} HP".format(randhp))
        time.sleep(1)
        print("{} Attack".format(randatk))
        time.sleep(1)
        print("{} Gold".format(randgold))
        time.sleep(1)
        print("{} Potion".format(randpotion))
        time.sleep(1)
    if sure not in yes:
        pass
        
    
    
#######################################################home
#enemy(xppri, xpsec, nmehp, nmeatk1, nmeatk2, difficulty, goldpri, goldsec)
def home():
    global level
    global xp
    global hp
    global atk
    global potion
    global gold
    
    global answers
    while True:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        time.sleep(1)
        print("Type 'fight' to fight.")
        time.sleep(1)
        print("Type 'shop' to go to the shop.")
        time.sleep(1)
        print("Type 'stats' to see stats.")
        time.sleep(1)
        print("Type 'info' to see info on the game.")
        time.sleep(1)
        if level > 1:
            print("Type 'quickfight' for a quick fight.")
            time.sleep(1)
            print("Type 'oracle' to speak to the oracle.")
            time.sleep(1)
            print("Type 'medfight' for a fight with medium difficulty")
            time.sleep(1)
            
        if level > 2:
            print("Type 'hardfight' for a fight with hard difficulty")
            time.sleep(1)
            print("Type 'chance' to try and get a free stat boost!")
            time.sleep(1)
            
        if potion > 0:
            print("Type 'potion' to drink a potion and get a random boost!")

        if level > 4:
            print("Congratulations! You have finished the league of sworos!")
            time.sleep(1)
            print("Your efforts have not gone unnoticed, the king has recognised your dediction and has appointed you to commander!")
            time.sleep(1)
            enderty = input("Continue or finish")
            if enderty == 'continue':
                pass
            else:
                quit()
        
        do = input("What to do?\n")
        
        if do == 'fight':
            enemy(1, 30, 50, 10, 30, 'easy', 0, 3)

        elif do == 'info':
            info()
            
        elif level > 1 and do == 'medfight':
            enemy(30, 60, 100, 15, 50, 'medium', 3, 6)
            
        elif level > 2 and do == 'hardfight':
            enemy(60, 120, 150, 20, 100, 'hard', 6, 12)
            
        elif do == 'shop':
            shop()
            
        elif do == 'stats':
            stats()
            
        elif level > 1 and do == 'quickfight':
            quickfight()
            
        elif level > 1 and do == 'oracle':
            oracle()

        elif level > 2 and do == 'chance':
            chance()
            
        elif potion > 0 and do == 'potion':
            potionlist = ["xp","gold","atk","hp"]
            xpr = random.randint(0,100)
            hpr = random.randint(0,20)
            atkr = random.randint(0,20)
            goldr = random.randint(0,10)
            potionr = random.choice(potionlist)
            
            if potionr == "xp":
                xp += xpr
                print("XP + {}".format(xpr))
            if potionr == "hp":
                hp += hpr
                print("HP + {}".format(hpr))
            if potionr == "atk":
                atk += atkr
                print("ATTACK + {}".format(atkr))
            if potionr == "gold":
                gold += goldr
                print("GOLD + {}".format(goldr))
            potion -= 1
            
        else:
            print("You can't do that...")
##############################################################oracle
def oracle():
    words1 = ["They","You","We"]
    words2 = ["have","are","will be","can be","aren't"]
    words3 = ["n enormous"," gigantic"," stinky"," dark","n evil"," selfish"," greedy"," slimey"," fluffy"," mouldy"]
    words4 = ["turd","goat","sworos","moron","fishmaster","eye","runtchild","demon","monster","king"]
    word1 = random.choice(words1)
    word2 = random.choice(words2)
    word3 = random.choice(words3)
    word4 = random.choice(words4)
    sentence = word1 + " " + word2 + " a" + word3 + " " + word4 + "."
    print(sentence)
    time.sleep(2)
    
##############################################################shop
def shop():
    global gold
    global shopstuff
    global xp
    global hp
    global atk
    global level
    global potion
    print("This is what you can buy:")
    time.sleep(1)
    print(shopstuff)
    time.sleep(1)
    print('''
  _________
/| GOLD| {}|
/| XP| {}  |
/|________|
///////////
  __________________
/| 10 health = 5g   |
/| 10 attack = 5g   |
/| 50 XP = 5g       |
/| 1 potion = 5g    |
/| level 2 = 200 XP |
/| level 3 = 400 XP |
/| level 4 = 800 XP |
/|__________________|
////////////////////

Type 'exit' to leave shop.
'''.format(gold, xp))
    time.sleep(1)
    print("Potions give you a random amount of hp/atk/xp/gold")
    while True:
        time.sleep(1)
        print("What would you like to buy?")
        buy = input(">")
        if buy not in shopstuff:
            print("You can't buy that...")
        if buy == 'health': #hp
            print("That'll be 5 gold please.")
            if gold > 4:
                gold -= 5
                hp += 10
                time.sleep(1)
                print("HP +10")
                time.sleep(1)
                print("Thank You!")
            else:
                print("You don't have enough money, sorry!")
        elif buy == 'attack': #atk
            print("That'll be 5 gold please.")
            if gold > 4:
                gold -= 5
                atk += 10
                time.sleep(1)
                print("ATTACK +10")
                time.sleep(1)
                print("Thank You!")
            else:
                print("You don't have enough money, sorry!")
        elif buy == 'xp': #xp
            print("That'll be 5 gold please.")
            if gold > 4:
                gold -= 5
                xp += 50
                time.sleep(1)
                print("XP +50")
                time.sleep(1)
                print("Thank You!")
            else:
                print("You don't have enough money, sorry!")
        elif buy == 'potion': #potion
            print("That'll be 5 gold please.")
            if gold > 4:
                gold -= 5
                potion += 1
                time.sleep(1)
                print("POTION +1")
                time.sleep(1)
                print("Thank You!")
            else:
                print("You don't have enough money, sorry!")
        elif buy == 'upgrade' and level == 1: #upgrade1
            print("That'll be 200 xp for a new level...")
            if xp > 199:
                xp -= 200
                level += 1
                time.sleep(1)
                print("LEVEL +1")
                time.sleep(1)
                print('Now you have level {}!'.format(level))
        elif buy == 'upgrade' and level == 2: #upgrade1
            print("That'll be 400 xp for a new level...")
            if xp > 399:
                xp -= 400
                level += 1
                time.sleep(1)
                print("LEVEL +1")
                time.sleep(1)
                print('Now you have level {}!'.format(level))
        elif buy == 'upgrade' and level == 3: #upgrade1
            print("That'll be 800 xp for a new level...")
            if xp > 799:
                xp -= 800
                level += 1
                time.sleep(1)
                print("LEVEL +1")
                time.sleep(1)
                print('Now you have level {}!'.format(level))
        elif buy == 'exit':
            "Bye!!!"
            break
        else:
            print("Yeh can't do dat yeh eejiot!")
###################################################################           

stats()
home()


    

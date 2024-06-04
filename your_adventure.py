import random
import time

php = 100
mhp = 200
pdpt = 50
mdpt = 30
turn = 0
pas_dpt = 0
epas_dpt = 0
turn_count = 0
coins = 0
diffricalty = 0
nurf = 0


game_start = input("1 to start game, 2 for game info, 3 to exit game: ")

if game_start == "3":
    exit()

if game_start == "2":
    print("info: the monster will attack you, you can heal yourself and attack")
    print("you can attack or defend, attacking is done by typing 'atk' it deals player attack to the enemy you can defend by typing 'def' giving you +10 base attack and +20 health")
    print(" ")


p_class = ["knight", "archer", "wizard"]
anemy_class_options = ["zombie", "golem", "skeleton", "dark mage"]

diffricalty = input ("select your diffricalty, easy: ,normal: , hard:")

if diffricalty == "easy":
		nurf = 0
if diffricalty == "normal":
	nurf = 1.3
if diffricalty == "hard":
	nurf = 1.7
	

print("")
print("class choices", p_class)
print("")
print("class stats: knight")
print("attack per turn: 50, hp: 150")
print("")
print("class stats: archer")
print("attack per turn: 110, hp: 90")
print("")
print("class stats: wizard")
print("attack per turn: 100, hp:70: passive attack per turn: 30")
print("")
print("passive attack is delt by magic classes as a result of their presence in the area")
print("")
p_class = input ("select your class by typing in your prefered class here: ")


if p_class == "knight":
    k_hp = 150
    php = 150
    pdpt = 50

if p_class == "archer":
    a_hp = 90
    php = 90
    pdpt = 110

if p_class == "wizard":
    w_hp = 70
    php = 70
    pdpt = 100
    pas_dpt = 30

e_class = random.randint(1,4)

if e_class == 1:
    print("your fighting a zombie!")
    mhp = 200
    mdpt = 20
if e_class == 2:
    print("your fighting a golem!")
    mhp = 150
    mdpt = 35
if e_class == 3:
    print("your fighting a skeleton!")
    mhp = 60
    mdpt = 10
if e_class == 4:
    print("your fighting a dark mage!")
    mhp = 60
    mdpt = 15
    epas_dpt = 10

while php >= 0:
	
		
    print("turn:", turn_count)
    mi = random.randint(1, 2)
    if mhp <= 30:
        mi = 1
    if mhp <= 10:
        mi = 2
    turn = 1
    print(mi)
    time.sleep(2)
    if turn >= 1:
        if mi == 1:
            print("___________________")
            print("enemy heals")
            mhp = mhp + 30
            mhp = mhp - pas_dpt
            print("enemy now has: ", mhp)
            turn = turn - 1
            if pas_dpt > 0:
                print("passive attack delt", pas_dpt)
                print("")
            print("player status:")
            print("player hp: ", php)
            print("player dpt ", pdpt)
            print("")
            print("monster status:")
            print("monster hp: ", mhp)
            print("___________________")
            turn_count = turn_count + 1
        if mi == 2:
            print("___________________")
            print("enemy attacks!")
            php = php - mdpt
            mhp = mhp - pas_dpt
            print("enemy hits you for: ", mdpt)
            print("you now have: ", php, "health")
            turn = turn - 1
            if pas_dpt > 0:
                print("passive attack delt", pas_dpt)
                print("")
            print("player status:")
            print("player hp: ", php)
            print("player dpt ", pdpt)
            print("")
            print("monster status:")
            print("monster hp: ", mhp)
            print("___________________")
            turn_count = turn_count + 1

    if turn <= 0:
        print("___________________")
        pc = input("will you atk or def?")

        if pc == "atk":
            print("you hit")
            mhp = mhp - pdpt
            php = php - epas_dpt
            print("you hit enemy for:", pdpt)
            print("enemy now has:", mhp)
            if pas_dpt > 0:
                print("passive attack delt to you", pas_dpt)
                print("")
            print("player status:")
            print("player hp: ", php)
            print("player dpt ", pdpt)
            print("")
            print("monster status:")
            print("monster hp: ", mhp)
            print("___________________")
            turn = turn + 1
            turn_count = turn_count + 1
        if pc == "def":
            print("___________________")
            print("you defend yourself you now deal +10 damnage and gain +20hp")
            php = php - epas_dpt
            pdpt = pdpt + 10
            php = php + 20
            turn = turn + 1
            if pas_dpt > 0:
                print("passive attack delt to you", pas_dpt)
                print("")

            print("player status:")
            print("player hp: ", php)
            print("player dpt ", pdpt)
            print("")
            print("monster status:")
            print("monster hp: ", mhp)
            print("___________________")
            turn_count = turn_count + 1

    if mhp <= 0:
        print("you win!")
        coins = coins + 50
        pdpt = pdpt / nurf
        print("you gained 50 coins! you now have: ", coins)
       
        buy = input ("welcome to the shop you can either buy: 100 health for (50 coins)   by pressing 1, attack bonus for (100 coins) by pressing 2, or save your money by typing 3")
        if buy == "3":
            print("thank you for stopping by!")
        if buy == "2":
            if coins >= 100:
                print("you now have +30 atk")
                pdpt = pdpt + 30
            if coins < 100:
                print("declined nice try FED!")
        if buy == "1":
            if coins >= 50:
                print("you have now been given +100 hp")              
                php = php + 100
            if coins < 50:
                 print("declined nice try FED!")

        print("engaging new enemy...")
        print("enemy found")
        print("|--------------------|")
        e_class = random.randint(1, 4)
        if e_class == 1:
            print("your fighting a zombie!")
            mhp = 200 * 1.5
            mdpt = 10
        if e_class == 2:
            print("your fighting a golem!")
            mhp = 150 + 50
            mdpt = 30
        if e_class == 3:
            print("your fighting a skeleton!")
            mhp = 60 * 2
            mdpt = 15
        if e_class == 4:
            print("your fighting a dark mage!")
            mhp = 60 * 2
            mdpt = 10
            epas_dpt = 10
        print("new enemy is", e_class)

    if php <= 0:
        print("you lose!")
        break
























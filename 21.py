import random
import click
import time
import os

os.system('cls')

winner = ["Du bist Sieger, Glückwunsch!", "Winner Chicken Dinner!", "DU hast gewonnen!"]
looser = ["Du hast leider verloren!", "Du hast kein Glück!", "Das war wohl nix!"]
weiter = ["Machst du weiter? ", "Noch einmal? ", "Versuchst du es weiter? "]

x = random.choice(winner)
y = random.choice(weiter)
z = random.choice(looser)

p = 0
c = 0
e = []
s = [1000]


print("----------------------------------------")
print("--------- Willkommen bei -21- ----------")
print("----------------------------------------")
print("")
print("- Wer 21 trifft gewinnt.")
print("- Wer über 21 kommt verliert.")
print("- CPU geht nicht über 17.")
print("- Die höhere Zahl gewinnt.")
print("- Einsatz gibt es zurück bei Draw.")
print("- 11 zählt auch als 1.")
print("- [1000] Credits beim Start")
print("")
print("----------------------------------------")
print("----------------------------------------")
print("-------------Highscoreliste-------------")
print("----------------------------------------")
h1 = [0]
n1 = [0]
try:
    with open("./score.txt", "r") as b2:
        for i2 in b2:
            splitted = i2.split(",")
            if int(splitted[1]) > sum(h1):
                h1[0] = (int(splitted[1]))
                n1[0] = (str(splitted[0]))
        print("1. Platz: " + str(n1[-1]) + " mit " + str(h1[-1]) + " Credits!")
except FileNotFoundError:
    print("Noch keine Einträge vorhanden!")
print("----------------------------------------")
print("----------------------------------------")
print("")


while sum(s) > 0:
    
    b = 10
    d = 10
    k = 10
    
    a = [
    2, 2, 2, 2, 
    3, 3, 3, 3, 
    4, 4, 4, 4, 
    5, 5, 5, 5, 
    6, 6, 6, 6, 
    7, 7, 7, 7, 
    8, 8, 8, 8, 
    9, 9, 9, 9, 
    10, 10, 10, 10, 
    b, b, b, b, 
    d, d, d, d, 
    k, k, k, k, 
    11, 11, 11, 11
    ]
    
    def rnd_zahl():
        return random.choice(a)
    
    r = rnd_zahl()
    
    time.sleep(2)
    
    print("Du hast " + str(s) + " Credits")
    print("")

    while True:
        try:
            f = input("Wieviel willst du setzten? Tippe stop zum beenden! ")
            os.system('cls')
            if str(f) == "stop":
                print("")
                print("Du hast das Spiel mit " + str(s) + " Credits beendet!")
                print("----------------------------------------")
                print("----------------------------------------")
                print("Endstand: DU = " + str(p) + " und CPU = " + str(c))
                print("----------------------------------------")
                print("----------------------------------------")
                n = input("Wie ist dein Name? ")
                print("")
                print("Danke " + str(n) + ",")
                print("dein Score von " + str(s) + " wurde gespeichert")
                print("")
                print("----------------------------------------")
                print("----------------------------------------")
                print("-------------Highscoreliste-------------")
                print("----------------------------------------")
                h1 = [0]
                n1 = [0]
                with open("./score.txt", "a+") as a1:
                    for i in range(1):
                        a1.write(str(n) + "," + str(sum(s)) + "\r")

                with open("./score.txt", "r") as b1:
                    for i2 in b1:
                        splitted = i2.split(",")
                        if int(splitted[1]) > sum(h1):
                            h1[0] = (int(splitted[1]))
                            n1[0] = (str(splitted[0]))
                    print("1. Platz: " + str(n1[-1]) + " mit " + str(h1[-1]) + " Credits!")
                print("----------------------------------------")
                print("----------------------------------------")
                input("Enter zum beenden!")
                break
                
            if int(f) < 1:
                print("")
                print("Du kannst keine [" + str(f) + "] Credits setzten!")
                print("")
                continue
                
            if int(f) > sum(s):
                print("")
                print("Du besitzt keine [" + str(f) + "] Credits!")
                print("")
                continue
                
            if int(f) > 0 and int(f) < sum(s):
                False
                
        except ValueError:
            print("")
            print("Gib eine Zahl von [1] bis " + str(s) + " ein,")
            print("oder stop zum beenden!")
            print("")
            continue
        else:
            break
            
    try:
        s[0] -= int(f)
        print("")
        print("Du setzst: " + str(f))
        print("Du hast noch " + str(s) + " Credits")
    except ValueError:
        break
    
    if s[0] == 0:
        print("All-In, viel Glück!")
    print("")
    
    l1 = []
    l2 = []

    print("Du würfelst: " + str(r))
    l1.append(r)
    a.remove(r)
    r = rnd_zahl()
    
    print("Du würfelst: " + str(r))
    l1.append(r)
    a.remove(r)
    r = rnd_zahl()
    time.sleep(1)
    
    if str(l1[0]) == str(l1[1]):
        
        
        if click.confirm("Willst du Splitten? ", default = False):
            
            print("")
            print("Du splittest: " + str(l1[0]))
            print("")
        
            l3 = []
            l4 = []
            l3.append(l1[0])
            l1.remove(l1[0])
            time.sleep(1)
            
            while sum(l3) < 21:
                
                y = random.choice(weiter)
                if click.confirm(y, default = False):

                    y = random.choice(weiter)
                    l3.append(r)
                    a.remove(r)

                    if 11 in l3 and sum(l3) > 21:
                        l3.remove(11)
                        l3.append(1)

                    print("")
                    print("Du würfelst: " + str(r))
                    time.sleep(1)              
                    print("")
                    print(l3)
                    print("Du hast jetzt insgesamt: " + str(sum(l3)))
                    r = rnd_zahl()
                    print("")
                else:
                    print("")
                    print("-Du bleibst bei " + str(sum(l3)) + " stehen!-")
                    break
                    
                if sum(l3) == 21:
                    x = random.choice(winner)
                    print("")
                    print("21 Glückwunsch!")
                    print("")

                if sum(l3) > 21:
                    print("")
                    print(z)
                    print("")
                    continue
                
            print("----------------------------------------")
            print("")
            print("CPU ist dran!")
            print("")
            input("Starte CPU mit Enter ")

            r = rnd_zahl()
            print("CPU würfelt: " + str(r))
            l4.append(r)
            a.remove(r)

            r = rnd_zahl()
            print("CPU würfelt: " + str(r))
            l4.append(r)
            a.remove(r)
            time.sleep(1)

            if sum(l4) == 22:
                l4 = [11, 1]

            print("")
            print("CPU hat jetzt insgesamt: " + str(sum(l4)))
            time.sleep(1)


            while sum(l4) < 17:
                
                if sum(l4) >= sum(l3):
                    break


                r = rnd_zahl()
                l4.append(r)
                a.remove(r)

                if 11 in l4 and sum(l4) > 21:
                    l4.remove(11)
                    l4.append(1)

                print("CPU würfelt: " + str(r))
                time.sleep(1)
                print("")
                print(l4)
                print("CPU hat jetzt insgesamt: " + str(sum(l4)))
                print("")
            else:
                print("")
                print("-CPU bleibt bei " + str(sum(l4)) + " stehen!-")
                
                if sum(l3) > sum(l4) and sum(l3) <= 21:
                    print("")
                    x = random.choice(winner)
                    print(x)
                    p += 1
                    s[0] += (int(f) * 2)
                    e.append(1)
                    print("Du hast den doppelten Einsatz bekommen")
                    print("")
                    print("Du hast " + str(s) + " Credits")
                    print("----------------------------------------")
                    print("Stand: DU = " + str(p) + " und CPU = " + str(c))
                    print("----------------------------------------")

                if sum(l3) < sum(l4) and sum(l4) > 21 and sum(l3) <= 21:
                    print("")
                    x = random.choice(winner)
                    print(x)
                    p += 1
                    s[0] += (int(f) * 2)
                    e.append(1)
                    print("Du hast den doppelten Einsatz bekommen!")
                    print("")
                    print("Du hast " + str(s) + " Credits")
                    print("----------------------------------------")
                    print("Stand: DU = " + str(p) + " und CPU = " + str(c))
                    print("----------------------------------------")

                if sum(l4) > sum(l3) and sum(l4) <= 21:
                    print("")
                    print("CPU gewinnt!")
                    c += 1
                    e.append(1)
                    print("Du hattest leider kein Glück,")
                    print("vielleicht beim nächsten Versuch!")
                    print("")
                    print("----------------------------------------")
                    print("Stand: DU = " + str(p) + " und CPU = " + str(c))
                    print("----------------------------------------")

                if sum(l4) < sum(l3) and sum(l3) > 21 and sum(l4) <= 21:
                    print("")
                    print("CPU gewinnt!")
                    c += 1
                    e.append(1)
                    print("Du hattest leider kein Glück,")
                    print("vielleicht beim nächsten Versuch!")
                    print("")
                    print("----------------------------------------")
                    print("Stand: DU = " + str(p) + " und CPU = " + str(c))
                    print("----------------------------------------")

                if sum(l3) == sum(l4) or sum(l3) > 21 and sum(l4) > 21:
                    print("")
                    print("Draw!")
                    p += 1
                    c += 1
                    s[0] += int(f)
                    print("Du bekommst deinen Einsatz zurück!")
                    print("")
                    print("Du hast " + str(s) + " Credits")
                    print("----------------------------------------")
                    print("Stand: DU = " + str(p) + " und CPU = " + str(c))
                    print("----------------------------------------")
        else:
            print("Es geht normal weiter...")
    print(l1)
    if sum(l1) == 22:
        l1 = [11, 1]

    print("")
    print("Du hast jetzt insgesamt: " + str(sum(l1)))  

    while sum(l1) < 21:
        
        y = random.choice(weiter)
        if click.confirm(y, default = False):
            
            y = random.choice(weiter)
            l1.append(r)
            a.remove(r)
            
            if 11 in l1 and sum(l1) > 21:
                l1.remove(11)
                l1.append(1)
                
            print("")
            print("Du würfelst: " + str(r))
            time.sleep(1)              
            print("")
            print(l1)
            print("Du hast jetzt insgesamt: " + str(sum(l1)))
            r = rnd_zahl()
            print("")
        else:
            print("")
            print("-Du bleibst bei " + str(sum(l1)) + " stehen!-")
            break                
    
    if sum(l1) == 21:
        x = random.choice(winner)
        print("")
        print("21 Glückwunsch!")
        print("")
        
    if sum(l1) > 21:
        print("")
        print(z)
        print("")
        continue

    print("----------------------------------------")
    print("")
    print("CPU ist dran!")
    print("")
    input("Starte CPU mit Enter ")

    r = rnd_zahl()
    print("CPU würfelt: " + str(r))
    l2.append(r)
    a.remove(r)

    r = rnd_zahl()
    print("CPU würfelt: " + str(r))
    l2.append(r)
    a.remove(r)
    time.sleep(1)

    if sum(l2) == 22:
        l2 = [11, 1]

    print("")
    print("CPU hat jetzt insgesamt: " + str(sum(l2)))
    time.sleep(1)
    

    while sum(l2) < 17:
        
        if sum(l2) >= sum(l1):
            break
        
            
        r = rnd_zahl()
        l2.append(r)
        a.remove(r)
        
        if 11 in l2 and sum(l2) > 21:
            l2.remove(11)
            l2.append(1)
            
        print("CPU würfelt: " + str(r))
        time.sleep(1)
        print("")
        print(l2)
        print("CPU hat jetzt insgesamt: " + str(sum(l2)))
        print("")
    else:
        print("")
        print("-CPU bleibt bei " + str(sum(l2)) + " stehen!-")

    if sum(l1) > sum(l2) and sum(l1) <= 21:
        print("")
        x = random.choice(winner)
        print(x)
        p += 1
        s[0] += (int(f) * 2)
        e.append(1)
        print("Du hast den doppelten Einsatz bekommen!")
        print("")
        print("----------------------------------------")
        print("Stand: DU = " + str(p) + " und CPU = " + str(c))
        print("----------------------------------------")
        
    if sum(l1) < sum(l2) and sum(l2) > 21 and sum(l1) <= 21:
        print("")
        x = random.choice(winner)
        print(x)
        p += 1
        s[0] += (int(f) * 2)
        e.append(1)
        print("Du hast den doppelten Einsatz bekommen!")
        print("")
        print("----------------------------------------")
        print("Stand: DU = " + str(p) + " und CPU = " + str(c))
        print("----------------------------------------")
        
    if sum(l2) > sum(l1) and sum(l2) <= 21:
        print("")
        print("CPU gewinnt!")
        c += 1
        e.append(1)
        print("Du hast deinen Einsatz verloren!")
        print("")
        print("----------------------------------------")
        print("Stand: DU = " + str(p) + " und CPU = " + str(c))
        print("----------------------------------------")
        
    if sum(l2) < sum(l1) and sum(l1) > 21 and sum(l2) <= 21:
        print("")
        print("CPU gewinnt!")
        c += 1
        e.append(1)
        print("Du hast deinen Einsatz verloren!")
        print("")
        print("----------------------------------------")
        print("Stand: DU = " + str(p) + " und CPU = " + str(c))
        print("----------------------------------------")
        
    if sum(l1) == sum(l2) or sum(l1) > 21 and sum(l2) > 21:
        print("")
        print("Draw!")
        p += 1
        c += 1
        s[0] += int(f)
        print("Du bekommst deinen Einsatz zurück!")
        print("")
        print("----------------------------------------")
        print("Stand: DU = " + str(p) + " und CPU = " + str(c))
        print("----------------------------------------")
else:
    print("----------------------------------------")
    print("")
    print("Du hast leider keine Credits Mehr!")
    print("")
    print("----------------------------------------")
    print("----------------------------------------")
    print("Endstand: DU = " + str(p) + " und CPU = " + str(c))
    print("----------------------------------------")
    print("----------------------------------------")
    print("-GAME OVER-")
    print("----------------------------------------")
    print("----------------------------------------")
    print("-------------Highscoreliste-------------")
    print("----------------------------------------")
    h1 = [0]
    n1 = [0]
    try:
        with open("./score.txt", "r") as b2:
            for i2 in b2:
                splitted = i2.split(",")
                if int(splitted[1]) > sum(h1):
                    h1[0] = (int(splitted[1]))
                    n1[0] = (str(splitted[0]))
            print("1. Platz: " + str(n1[-1]) + " mit " + str(h1[-1]) + " Credits!")
    except FileNotFoundError:
        print("Noch keine Einträge vorhanden!")
    print("----------------------------------------")
    print("----------------------------------------")
    input("Enter zum beenden!")

import math
import time
import click


pi = math.pi


def Plus_rechnen(a, b):
    return print(round(float(a) + float(b), 5))

def Minus_rechnen(a, b):
    return print(round(float(a) - float(b), 5))

def Mal_rechnen(a, b):
    return print(round(float(a) * float(b), 5))

def Geteilt_rechnen(a, b):
    try:
        return print(round(float(a) / float(b), 5))
    except ZeroDivisionError:
        print("Du kannst nicht durch 0 teilen!")

def Hoch_rechnen(a, b):
    return print(round(float(a) ** float(b), 5))

def Dezi_bin(a):
    return print(format(a, "b"))

def Bmi_rechnen(a, b):
    a = a / 100
    return print(round(float(b) / float(a) **2, 5))

print("-----------------------------------------------")
print("------------------- Rechner -------------------")
print("-----------------------------------------------")
time.sleep(2)
print("- Zum Plus rechnen = + ")
print("- Zum Minus rechnen = -")
print("- Zum Mal rechnen = *")
print("- Zum Geteilt rechnen = /")
print("- Zum Hoch rechnen = h")
print("- Dezimal in Binär umrechnen = b")
print("- BMI ausrechnen = bmi")
print("- Zum beenden tippe stop")
print("-----------------------------------------------")
time.sleep(2)
while True:
    
    try:
        print("")
        f = input("Was möchtest du rechnen? ")

        if str(f) == "+":
            print("")
            print("- Plus rechnen")
            time.sleep(1)
            while True:
                try:
                    a = float(input("Tippe den ersten Wert "))
                    b = float(input("Tippe den zweiten Wert "))
                    print("")
                    print(str(a) + " + " + str(b) + " =")
                    Plus_rechnen(a, b)
                    print("")
                    if click.confirm("Weiter mit y oder zurück mit n ", default = False):
                        continue
                    else:
                        break
                except ValueError:
                    print("Gib richtige Zahlen ein!")
                    continue

        elif str(f) == "-":
            print("")
            print("- Minus rechnen")
            time.sleep(1)
            while True:
                try:
                    a = float(input("Tippe den ersten Wert "))
                    b = float(input("Tippe den zweiten Wert "))
                    print("")
                    print(str(a) + " - " + str(b) + " =")
                    Minus_rechnen(a, b)
                    print("")
                    if click.confirm("Weiter mit y oder zurück mit n ", default = False):
                        continue
                    else:
                        break
                except ValueError:
                    print("Gib richtige Zahlen ein!")
                    continue
                    
        elif str(f) == "*":
            print("")
            print("- Mal rechnen")
            time.sleep(1)
            while True:
                try:
                    a = float(input("Tippe den ersten Wert "))
                    b = float(input("Tippe den zweiten Wert "))
                    print("")
                    print(str(a) + " * " + str(b) + " =")
                    Mal_rechnen(a, b)
                    print("")
                    if click.confirm("Weiter mit y oder zurück mit n ", default = False):
                        continue
                    else:
                        break
                except ValueError:
                    print("Gib richtige Zahlen ein!")
                    continue
                    
        elif str(f) == "/":
            print("")
            print("- Geteilt rechnen")
            time.sleep(1)
            while True:
                try:
                    a = float(input("Tippe den ersten Wert "))
                    b = float(input("Tippe den zweiten Wert "))
                    print("")
                    print(str(a) + " / " + str(b) + " =")
                    Geteilt_rechnen(a, b)
                    print("")
                    if click.confirm("Weiter mit y oder zurück mit n ", default = False):
                        continue
                    else:
                        break
                except ValueError:
                    print("Gib richtige Zahlen ein!")
                    continue
                    
        elif str(f) == "h":
            print("")
            print("- Hoch rechnen")
            time.sleep(1)
            while True:
                try:
                    a = float(input("Tippe den ersten Wert "))
                    b = float(input("Tippe den zweiten Wert (Hoch) "))
                    print("")
                    print(str(a) + " ^" + str(b) + " =")
                    Hoch_rechnen(a, b)
                    print("")
                    if click.confirm("Weiter mit y oder zurück mit n ", default = False):
                        continue
                    else:
                        break
                except ValueError:
                    print("Gib richtige Zahlen ein!")
                    continue
                except OverflowError:
                    print("Die Werte waren zu hoch!")
                    continue
                    
        elif str(f) == "b":
            print("")
            print("- Dezimal in Binär umrechnen")
            time.sleep(1)
            while True:
                try:
                    a = int(input("Tippe eine Dezimalzahl zum umrechnen in Binär "))
                    print("")
                    print("Die Dezimalzahl " + str(a) + " ist in Binär =")
                    Dezi_bin(a)
                    print("")
                    if click.confirm("Weiter mit y oder zurück mit n ", default = False):
                        continue
                    else:
                        break
                except ValueError:
                    print("")
                    print("Gib richtige Zahlen ein!")
                    continue
                    
        elif str(f) == "bmi":
            print("")
            print("- BMI ausrechnen!")
            time.sleep(1)
            while True:
                try:
                    a = float(input("Wie groß bist du in Zentimeter? "))
                    b = float(input("Wieviel Kg wiegst du? "))
                    print("")
                    print(str(b) + " Kg / " + str(a) + " ^2 =")
                    Bmi_rechnen(a, b)
                    print("")
                    if click.confirm("Weiter mit y oder zurück mit n ", default = False):
                        continue
                    else:
                        break
                except ValueError:
                    print("")
                    print("Gib richtige Zahlen ein!")

        elif str(f) == "stop":
            break
        
        else:
            print("")
            print("- Zum Plus rechnen = + ")
            print("- Zum Minus rechnen = -")
            print("- Zum Mal rechnen = *")
            print("- Zum Geteilt rechnen = /")
            print("- Zum Hoch rechnen = h")
            print("- Dezimal in Binär umrechnen = b")
            print("- Mit stop kommt man wieder zurück oder beendet")

    except ValueError:
        print("")
        print("Gib richtige Zahlen ein!")
        time.sleep(1)
        continue
        
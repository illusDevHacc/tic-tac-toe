from art import text2art
from os import system
from colorama import Fore

print(text2art("Tic Tac Toe"))
print(Fore.RED+"oynamak istediğiniz yerdeki numarayı girerek o bölgeye karakter yerleştirebilirsiniz")
input(Fore.WHITE+"Başlatmak için enter basınız:")

tictactoe = {
    1:" ",2:" ",3:" ",
    4:" ",5:" ",6:" ",
    7:" ",8:" ",9:" "
}
simdikioyuncu, siradakioyuncu = "x","o"
def showtictactoe(t):
    print(f"""

{t[1]}-1 | {t[2]}-2 | {t[3]}-3
-------------------
{t[4]}-4 | {t[5]}-5 | {t[6]}-6
-------------------
{t[7]}-7 | {t[8]}-8 | {t[9]}-9


""")
    
    
def kazananibul(t,o):
    if(t[1] == t[2] == t[3] == o):
        print(f"{o} oyunu kazandı")
        return True
    elif (t[1] == t[5] == t[9] == o):
        print(f"{o} oyunu kazandı")
        return True
    elif (t[4] == t[5] == t[6] == o):
        print(f"{o} oyunu kazandı")
        return True
    elif (t[7] == t[8] == t[9] == o):
        print(f"{o} oyunu kazandı")
        return True
    elif (t[3] == t[5] == t[7] == o):
        print(f"{o} oyunu kazandı")
        return True
    elif (t[3] == t[6] == t[9] == o):
        print(f"{o} oyunu kazandı")
        return True
    elif (t[1] == t[4] == t[7] == o):
        print(f"{o} oyunu kazandı")
        return True
    elif (t[2] == t[5] == t[8] == o):
        print(f"{o} oyunu kazandı")
        return True
    if ((t[1] != " " and t[2] != " " and t[3] != " " and t[4] != " " and t[5] != " " and t[6] != " " and t[7] != " " and t[8] != " " and t[9] != " ")):
        print("Berabere")
        return True
        


while 1:
    try:
        system("cls")
        showtictactoe(tictactoe)
        choice = int(input(f"şuanki sıra {simdikioyuncu} ait:"))
        if (choice >9 or choice <1 or tictactoe[choice] != " "):
            print("Sen hilecisin :[")
            break
        tictactoe[choice] = simdikioyuncu
        if kazananibul(tictactoe,simdikioyuncu):
            showtictactoe(tictactoe)
            break
        simdikioyuncu,siradakioyuncu=siradakioyuncu,simdikioyuncu
    except ValueError:
        pass
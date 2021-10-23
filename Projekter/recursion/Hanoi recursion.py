# Vi bruger recursion til at løse Hanoi tower problemet

#Den lettese mulighed er kun med 1 ring
#Med to ringe er løsningen

#Hele ideen med dette er at hvis man kender løsningen for 1 ringer mindre end det man har kan man også finde løsningen for det antal ringe man har.
#Løsningen til 4 ringe er at bruge løsningen fra 3 ringe til at flytte de øverste 3 ringe til plads B via C, herefter flyttes den store ring fra A til C og nu bruges løsningen for 3 igen til flytte de tre ringe fra B til C via A
#Dette er gældene for alle antal ringe.
#Derfor bruger vi recursion, Vi bruger løsningen for 1 ring til at finde løsningen for 2 ringe, og vi bruger løsningen for 2 ringe til at finde løsningen til 3 ringe osv...

#Vi laver en funktion der viser vores moves
def move(fra,til):
    print(f"Flyt ring fra {fra} til {til}.")


def hanoi(ringe,fra,til,via):
    if ringe == 0:#Når inge er lig 0 passer vi, dette gøres da vi ellers ville få negative ringen
        pass
    else:
        hanoi(ringe-1,fra=fra,til=via,via=til) #Første step er at bruge løsningen ringe-1 til at flytte ringe-1 til via pælen
        move(fra=fra,til=til) #Herefter flyttes den sidste ring fra den første pæl (fra) til den sidste pæl (til)
        hanoi(ringe-1,fra=via,til=til,via=fra) #Nu bruger vi ringe-1 løsningen igen for at flytte ringene fra via pælen til den sidste pæl (til)

hanoi(3,"A","C","B")

#Lad os sige vi vil løse med 3 ringe.
#Her når vi til linje 20 hvor funktionen kalder sig selv med 1 mindre ring, dette sker indtil antallet af ringe er 0 hvor der bliver passet
#ved 1 ring er variablerne fra = A, til = C, dette bruges til at flytte den øverste ring.


#Løsningen for 3 ringe er ryk 2 ringe til midten, nederste ring til højre, midterste 2 ringe til højre
#Vi ser denne løsning afhænger af løsningen af 2 ringe!
#Løsningen for 2 ringe er, Øverste ring til midten, nederste til højre, midterste til højre


#Vi ser vores svar er bygget op at 3 dele:
#Først flyt n-1 ringe til midten.
#Flyt nederste ring fra venstre til højre.
#Flyt n-1 ringe fra midten til højre
#Der er præcis på denne måde vi har bygget vores kode op!
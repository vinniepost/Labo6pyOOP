### Om de requirements.txt te maken gebruik je pip freeze > requirements.txt ###

# imports
import sys  # laat toe om sys.argv[] te gebruiken


# funtions
def Init() -> None:
    '''
    Runt bij het opstarten van het programma. Kijkt of de Serverlijst bestaat. Indien niet maakt hij deze aan
    '''
    serverlijst = []
    bestandsLocatie = "Serverlijst.txt"
    try:
        with open(bestandsLocatie, "r") as file:
            for line in file:
                serverlijst.append(line)
    except FileNotFoundError:
        open(bestandsLocatie, "w")


def Ping(IPaddress: str, timeout: int = 1, count: int = 1, silent: bool = False) -> bool:
    """
    Een functie die pingt naar een remote server om te kijken of die online is
    :param IPaddress: IP address van de remote server
    :param timeout: hoe lang moet de functie wachten op een antwoord
    :param count: hoe vaak moet de functie pingen
    :param silent: True of False, als True dan geen print statements
    :return: True of False    
    """
    pass


def ServerToevoegen():
    pass


def ServerVerwijderen():
    pass


def ServerlijstWeergeven():
    pass


def Main():
    Init()
    while True:
        print("Wat wilt u doen?\n1. Server toevoegen\n2. Server verwijderen\n3. Serverlijst weergeven\n4. Server pingen")
        keuze = input("1,2,3 of 4? (q: quit)\n")
        match keuze:
            case "1":
                print("Server toevoegen")
            case "2":
                print("Server verwijderen")
            case "3":
                print("Serverlijst weergeven")
            case "4":
                print("Server pingen")
                IPaddress = input("Welk ip-address wilt u pingen")
            case "q":
                exit()
            case _:
                print("Geef een geldige invoer in")

## wat is de __name__ als ik mijn programma run via python pingding argumenten

if __name__ == "__main__":
    Main()

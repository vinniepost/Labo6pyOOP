import sys  # laat toe om sys.argv[] te gebruiken
import json
from ping3 import ping


def Init() -> None:

    # Kijkt of de file gerunt wordt met of zonder agrumenten. Indien er argumenten zijn zal hij deze toekennen aan keuze

    if len(sys.argv) > 1:
        if sys.argv[1] == "1" or sys.argv[1] == "2" or sys.argv[1] == "3" or sys.argv[1] == "4":
            keuze = sys.argv[1]
            return keuze
        elif sys.argv[1] == "help" or sys.argv[1] == "h":
            print(
                "1: Server toevoegen\n2: Server verwijderen\n3: Serverlijst weergeven\n4: Server pingen")
            exit()
        else:
            print("Geef een geldige invoer in")
            exit()
    else:
        keuze = ""
        return keuze


def Ping():
    serverlijst = "files/serverlist.json"
    pingList = "files/pingList.json"
    with open(serverlijst, "r") as sl:
        pinglist = []
        for server in json.load(sl):
            print("----------------------------")
            print(f"Pingen van {server['naam']}...")
            if ping(server["adres"]) == False:
                print(f"{server['naam']} is offline")
                active = False
                dataForPinglist = {
                    "naam": server['naam'], "active?": active}
                pinglist.append(dataForPinglist)
            else:
                print(f"{server['naam']} is online")
                active = True
                dataForPinglist = {
                    "naam": server['naam'], "active?": active}
                pinglist.append(dataForPinglist)
        with open(pingList, "w") as pl:
            json.dump(pinglist, pl, indent=4)
    print("----------------------------")


def ServerToevoegen():
    serverlijst = "files/serverlist.json"
    if len(sys.argv) > 1:
        serverNaam = sys.argv[2]
        serverAdres = sys.argv[3]
    else:
        serverNaam = input("Wat is de naam van de server?\n")
        serverAdres = input("Wat is het adres (bv facebook.com)\n")
    with open(serverlijst, "r") as sl:
        serverlist = json.load(sl)
    newServer = {'naam': serverNaam, 'adres': serverAdres}
    serverlist.append(newServer)
    print("------------------------------------")
    with open(serverlijst, "w") as sl:
        json.dump(serverlist, sl, indent=4)


def ServerVerwijderen():
    serverlijst = "files/serverlist.json"
    if len(sys.argv) > 1:
        toBeRemoved = sys.argv[2]
    else:
        toBeRemoved = input(
            "Wat is de naam van de server die je wilt verwijderen?\n")
    with open(serverlijst, "r") as sl:
        serverlist = json.load(sl)
    indexToRemove = None
    for i, entry in enumerate(serverlist):
        if entry["naam"] == toBeRemoved:
            indexToRemove = i
            break
    if indexToRemove is not None:
        del serverlist[indexToRemove]
        print("entry deleted")
        print("------------------------------------")
    else:
        print("site not found in list")
        print("------------------------------------")

    with open(serverlijst, "w") as sl:
        json.dump(serverlist, sl, indent=4)


def ServerlijstWeergeven():
    serverlijst = "files/serverlist.json"
    print("------------------------------------")
    print("De serverlijst is als volgt:")
    with open(serverlijst) as sl:
        for server in json.load(sl):
            print(server['naam'])
    print("------------------------------------")


def Main():
    keuze = Init()

    while True:
        print("Wat wilt u doen?\n1. Server toevoegen\n2. Server verwijderen\n3. Serverlijst weergeven\n4. Server pingen")
        if keuze == "":
            keuze = input("1,2,3 of 4? (q: quit)\n")
        match keuze:
            case "1":

                ServerToevoegen()
            case "2":
                ServerVerwijderen()
            case "3":
                ServerlijstWeergeven()
            case "4":
                Ping()
            case "q":
                exit()
            case _:
                print("Geef een geldige invoer in")

        keuze = ""


if __name__ == "__main__":
    Main()

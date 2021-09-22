import json

# Dit alleen gebruiken om Json aan te maken.
#productenvar = [
#    {"naam": "mars", "prijs": 1.00, "aantal": 10, "verkocht": 0},
#    {"naam": "snicker", "prijs": 1.20, "aantal": 8, "verkocht": 0},
#    {"naam": "kitkat", "prijs": 0.9, "aantal": 0, "verkocht": 0},
#]


# bestand openen
jsonBestand = open ("producten.json")
json_array = json.load(jsonBestand)

# lege lijst aanmaken.
producten = []

# importeer json naar de multi array
for item in json_array:
    slaDetailsOp = {"naam":None, "prijs":None, "aantal":None, "verkocht":None}
    slaDetailsOp["naam"] = item["naam"]
    slaDetailsOp["prijs"] = item["prijs"]
    slaDetailsOp["aantal"] = item["aantal"]
    slaDetailsOp["verkocht"] = item["verkocht"]

    producten.append(slaDetailsOp)



def apparaatBijvullen():
    print("Welk product wil je bijvullen.")
    for product in producten:
        print(product["naam"][0].upper() + product["naam"][1:] + ' Aantal: '+ product["aantal"])

    # kijken of product bestaat.
    productInput = input("Welk product wil je bijvullen? ").lower()
    for product in producten:
        if product["naam"] == productInput:
            print("U heeft " + product + "gekozen.")
            bijvulInput = int(input("Hoeveel wilt u bijvullen? Moet een int zijn dus geen punt getal."))
            product["aantal"] = product["aantal"] + bijvulInput
            print(f"Het bijvullen is gelukt!\n")
        elif product["naam"] != productInput and product["naam"] == producten["naam"][-1]:
            print("Dit product is niet gevonden...")




# functie voor uitlezen van apparaat. Je kan het uitlezen als je bij welk product wil je kopen? uitlezen invult.
def apparaatUitlezen():
    totaalVerdient = 0.0
    for product in producten:
        print("Naam: " + product['naam'][0].upper() + product['naam'][1:])
        print("Prijs:  $" + str(f"{product['prijs']:.2f}"))
        print("Aantal: " + str(product['aantal']))
        print("Verkocht: " + str(product['verkocht']))
        # uitrekenen van verdient en totaal verdient
        verdient = product['prijs'] * product['verkocht']
        print("Verdient: "+ str(verdient)+ f"\n")
        totaalVerdient = totaalVerdient + verdient
    print("In totaal verdient: $" + str(f"{totaalVerdient:.2f}") + f"\n" )


def productToevoegen():
    print(f"\nDeze producten met waardes zitten er al in: ")
    apparaatUitlezen()

    print(f"\nproduct toevoegen")

    # check of product bestaat
    while True:
        try:
            naam = input("Wat is de naam van het product dat je wil toevoegen? ").lower()
            # check of product al bestaat.
            for product in producten:
                magDoorgaan = True
                if product["naam"] == naam:
                    print("Dit product bestaat al en kan niet worden toegevoegd.")
                    magDoorgaan = False
            if magDoorgaan == True:
                break
        except ValueError:
            print("Niet een goede naam. Je hebt een getal ingevuld.")

    while True:
        try:
            prijs = float(input("Hoe duur is het product? (in punt getal dus float) "))
            break
        except ValueError:
            print("Het getal is geen float. Gebruik een . dus 8.0 en niet 8,0")
    while True:
        try:
            aantal = float(input("Hoeveel van dit product voeg je toe? "))
            break
        except ValueError:
            print("Het getal is geen float. Gebruik een . dus 8.0 en niet 8,0")

    # maak de lijst aan met variable.
    producten.append({'naam': naam, 'prijs': prijs, 'aantal': aantal, 'verkocht': 0})

    # UNDER CONSTRUCTION
    #permanentInput = input("Wil je dit product voor altijd toevoegen? ja/nee (Dan onthoudt die het product ook na een reboot?)").lower()


    #if permanentInput == 'ja':
    with open("producten.json", 'w') as outfile:
        json.dump(producten, outfile, indent=4, separators=(',', ':'))
        print(f'Toevoegen is gelukt en hij zal het permanent onthouden.\n')
    #elif permanentInput == 'nee':
    #    print('Oke, alleen onthouden voor deze sessie.')
    #else:
    #    print("Instructie niet duidelijk. Alleen voor deze sessie onthouden.")


print("Eerste boot...")
print("1: product toevoegen")
print("2: normaal opstarten")
print("3: apparaat uitlezen (dit kan je ook tijdens dat het apparaat draait doen dooer uitlezen in te vullen.)")
print("4: apparaat bijvullen")
bootUp = int(input("Wil je een product toevoegen of de machine normaal opstarten? "))


if bootUp == 1:
    while True:
        productToevoegen()
        nogEenProduct = input("Wil je nog een product toevoegen? (ja/nee) ").lower()
        if nogEenProduct == "nee":
            break
        # typfout opvangen en feedback geven aan user.
        elif nogEenProduct != "ja":
            print("Instructie onduidelijk, ik zal stoppen met toevoegen.")
            break

elif bootUp == 3:
    print(f"uitlezen...\n")
    apparaatUitlezen()

elif bootUp == 4:
    print(f"aparaat bijvullen\n")
    apparaatBijvullen()

else:
    # gaat dan door naar de onderste loop.
    print(f"normaal opstarten\n")






# Functie om betaling te behandelen. Hiervoor heeft die dus de prijs van het gekozen product nodig.
def betalingen(productPrijs, product):
    while True:
        try:
            gegevenGeld = float(input("Hoeveel geld heb je?"))
            break
        except ValueError:
            print("Geen correct getal gebruik geen kommas maar punten")
    if productPrijs == gegevenGeld:
        print("Betaling is gelukt")
        # Roept alleen functie aan als product is betaald
        ontvangProduct(product)

    elif productPrijs > gegevenGeld:
        print("Te weinig geld voor dit product. Uw heeft $" + str(f"{gegevenGeld:.2f}") + " gegeven maar u heeft $" + str(f"{productPrijs:.2f}") + f" nodig\n")


    elif productPrijs < gegevenGeld:
        geldTerug = gegevenGeld - productPrijs
        print("teveel geld gegeven. Je krijgt $" + str(F"{geldTerug:.2f}") + " terug")
        ontvangProduct(product)


def vraagProduct():
    print("Welkom bij dit snoepautomaat, je kunt kiezen uit de volgende producten:")
    for product in producten:
        print(product["naam"][0].upper() + product["naam"][1:])
    productInput = input("Welk product wil je kopen? ").lower()
    for product in producten:
        if product["naam"] == productInput:
            # checkt op voorraad
            if product["aantal"] > 0:
                print("We hebben "+ product["naam"][0].upper() + product["naam"][1:] + " op voorraad en de prijs is: $" + str(f"{product['prijs']:.2f}"))
                # Gaat door naar funcite betaling
                betalingen(product['prijs'], product)
                break
            else:
                print("We hebben het product "+ product['naam'][0].upper() + product['naam'][1:] + f" helaas niet op voorraad\n")
                break

        # Checkt of de naam er niet in zit en of die op het laatste woordt van de lijst is. Zodat die eerst alles controleert en niet na de eerste stopt.
        elif product['naam'] != productInput and product == producten[-1]:
            # uitzondering voor uitlezen.
            if productInput == "uitlezen":
                apparaatUitlezen()
            else:
                print("Het product: " + productInput + " Bestaat niet of is verkeerd getypt. Probeer het opnieuw " + f"\n")
                break


def ontvangProduct(gekozenProduct):
    print("Hier is uw product: " + gekozenProduct['naam'][0].upper() + gekozenProduct['naam'][1:])
    gekozenProduct['aantal'] = gekozenProduct['aantal'] -1
    gekozenProduct['verkocht'] = gekozenProduct['verkocht'] + 1
    with open("producten.json", 'w') as outfile:
        json.dump(producten, outfile, indent=4, separators=(',', ':'))
    # \n voor extra enter.
    print(f"volgende klant!\n")


# altijd in een loop zodat het blijft draaien.
while True:
    vraagProduct()


import translator as tr

t = tr.Translator()

active = True

dizAlienoItaliano, dizItalianoAlieno = t.loadDictionary("dictionary.txt")

while(active):

    t.printMenu()

    txtIn = input("digita numero per selezionare: ")

    if txtIn in ["1", "2", "3", "4"]:

        # Add input control here!

        if int(txtIn) == 1:
            newParolaAliena = input("Ok, quale parola aliena devo aggiungere? ")
            newTraduzione = input("qual'è la sua traduzione italiana ")
            entry = [newParolaAliena, newTraduzione]
            t.handleAdd(entry)
            print(f"{entry} Aggiunta!\n")
            continue

        if int(txtIn) == 2:
            newParolaDaCercare = input("Ok, quale parola aliena devo cercare? ")
            risultato = t.handleTranslate(newParolaDaCercare, dizAlienoItaliano)
            print(f"{risultato}\n")
            continue

        if int(txtIn) == 3:
            wildParola = input("Ok, quale parola aliena con wildcard devo cercare? ")
            risultato = t.handleWildCard(wildParola, dizAlienoItaliano)
            print(f"{risultato}\n")

        if int(txtIn) == 4:
            break



import string


class Translator:

    def __init__(self):
        pass

    def printMenu(self):
        print("1. Aggiungi nuova parola\n2. Cerca una traduzione\n3. Cerca con wildcard\n4. Exit")


    dizAlienoItaliano = {}
    dizItalianoAlieno = {}

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        with open(dict, "r", encoding="utf-8") as file:
            for line in file:
                parole = line.strip().split()
                if len(parole) == 2:
                    alienWord = parole[0]
                    italianWord = parole[1]
                    self.dizAlienoItaliano[alienWord] = [italianWord]
                    self.dizItalianoAlieno[italianWord] = [alienWord]
        return self.dizAlienoItaliano, self.dizItalianoAlieno


    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        alienWord = entry[0]
        italianWord = entry[1]
        if alienWord in self.dizAlienoItaliano.keys():
            self.dizAlienoItaliano[alienWord].append(italianWord)
        else:
            self.dizAlienoItaliano[alienWord] = [italianWord]



    def handleTranslate(self, query, dizAlienoItaliano):
        # query is a string <parola_aliena>
        out = dizAlienoItaliano.get(query, "Parola aliena non trovata")
        return out

    def handleWildCard(self, query, dizAlienoItaliano):
        # query is a string with a ? --> <par?la_aliena>
        out = []
        try:
            index = query.index("?")
            for letter in string.ascii_letters:
                #print(letter)
                parola = query.replace("?", letter)
                #print(parola)
                trad = dizAlienoItaliano.get(parola, None)
                if trad != None:
                    out.append(trad)

        except ValueError:
            out.append(self.handleTranslate(query, dizAlienoItaliano))
        return out



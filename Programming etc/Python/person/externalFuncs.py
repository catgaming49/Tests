def formatList(list):
    unwantedChars = ["{", "}","'","[","]"]
    dicnt=str(list)
    for i in unwantedChars:
        dicnt=dicnt.replace(str(i),"")
    return dicnt


    
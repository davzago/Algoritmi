from Lab5.source.Printer import TwoCurvesPrinter
from Lab5.source.Printer import OneCurvePrint



def resultParser():
    f = open('../risultati.csv', 'r', encoding='ISO-8859-1')
    question = 0
    title = ''
    arrayY1 = []
    arrayY2 = []
    arrayX = []
    f.readline()
    cond = True
    while cond:
        line = f.readline().strip('\n').split(',')
        if line[0] == "DOMANDA":
            if question == 1:
                TwoCurvesPrinter(title, "Numero di Punti", "Seriale", "Parallelo", arrayY1, arrayY2, arrayX)
            elif question == 2:
                TwoCurvesPrinter(title, "Numero di Cluster", "Seriale", "Parallelo", arrayY1, arrayY2, arrayX)
            elif question == 3:
                TwoCurvesPrinter(title, "Numero di Iterazioni", "Seriale", "Parallelo", arrayY1, arrayY2, arrayX)
            question += 1
            title = "Domanda " + str(question)
            arrayX = []
            arrayY1 = []
            arrayY2 = []
        if question == 1:
            if line[0] == "Seriale":
                arrayY1.append(int(line[6]))
                arrayX.append(int(line[1]))
            elif line[0] == "Parallelo":
                arrayY2.append(int(line[6]))
        if question == 2:
            if line[0] == "Seriale":
                arrayY1.append(int(line[6]))
                arrayX.append(int(line[2]))
            elif line[0] == "Parallelo":
                arrayY2.append(int(line[6]))
        if question == 3:
            if line[0] == "Seriale":
                arrayY1.append(int(line[6]))
                arrayX.append(int(line[3]))
            elif line[0] == "Parallelo":
                arrayY2.append(int(line[6]))
        if question == 4:
            if line[0] == "Parallelo":
                arrayX.append(int(line[5]))
                arrayY1.append(int(line[6]))
        if line[0] == '':
            OneCurvePrint(title, "Cutoff", arrayY1, arrayX)
            cond = False


resultParser()



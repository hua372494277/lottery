from generalFunc import readFileIntoDictTimeasKey, translateToStr

def writeNGramDictToFile(fileName, ngramDict, n):
    fw = open(fileName, 'w')

    for i in range(0, pow(10, n + 1)):
        formatS = "%0" + str(n+1) + "d"
        key = formatS % i

        if key in ngramDict:
            for item in key:
                fw.write(item + '\t')

            fw.write(str(ngramDict[key]) + "\n")

    fw.close()

def  calculateNGram(hundred, tens, digit, target, n, flag):
    ngramDictHundred = {}
    ngramDictTens = {}
    ngramDictDigit = {}

    for i in range(0, len(hundred) - n):
        keyHund = ""
        keyTens = ""
        keyDig = ""

        for j in range(0, n):
            keyHund += hundred[i + j]
            keyTens += tens[i + j]
            keyDig += digit[i + j]

        keyHund += target[i + n]
        keyTens += target[i + n]
        keyDig += target[i + n]

        if not keyHund in ngramDictHundred:
            ngramDictHundred.setdefault(keyHund, 0)
        if not keyTens in ngramDictTens:
            ngramDictTens.setdefault(keyTens, 0)
        if not keyDig in ngramDictDigit:
            ngramDictDigit.setdefault(keyDig, 0)

        ngramDictHundred[keyHund] += 1
        ngramDictTens[keyTens] += 1
        ngramDictDigit[keyDig] += 1

    writeNGramDictToFile('../' + str(n) + 'hundgramFor' + flag + '.txt', ngramDictHundred, n)
    writeNGramDictToFile('../' + str(n) + 'tensgramFor'  + flag + '.txt', ngramDictTens, n)
    writeNGramDictToFile('../' + str(n) + 'digitgramFor' + flag + '.txt', ngramDictDigit, n)
    return (ngramDictHundred, ngramDictTens, ngramDictDigit)

def normalization(ngramDict):
    result = {}
    sums = 0

    for i in range(930, 940):
        key = str(i)
        if key in ngramDict:
            sums += ngramDict[key]

    for i in range(930, 940):
        key = str(i)
        if key in ngramDict:
            result[key] = float(ngramDict[key])/float(sums)

    return result

def calculatePercent(H, T, D):
    result = {}
    for i in range(930, 940):
        key = str(i)
        if key in H and key in T and key in D:
            result[key] = float(H[key]) * float(T[key]) * float(D[key])
    return result


records = []

#read all sums of three numbers into dict according to year
for year in range(2002, 2017):
    records.extend( readFileIntoDictTimeasKey('../' + str(year) + '.txt', translateToStr))

hundredList = []
tensList = []
digitList = []

for item in records:
    hundredList.append(item[0])
    tensList.append(item[1])
    digitList.append(item[2])

(HH, TH, DH) = calculateNGram(hundredList, tensList, digitList, hundredList, 2, 'H')
HH = normalization(HH)
TH = normalization(TH)
DH = normalization(DH)

print calculatePercent(HH, TH, DH)
print "H"

(HT, TT, DT) = calculateNGram(hundredList, tensList, digitList, tensList, 2, 'T')
HT = normalization(HT)
TT = normalization(TT)
DT = normalization(DT)

print calculatePercent(HT, TT, DT)
print "T"


(HD, TD, DD) = calculateNGram(hundredList, tensList, digitList, digitList, 2, 'D')
HD = normalization(HD)
TD = normalization(TD)
DD = normalization(DD)

print calculatePercent(HD, TD, DD)
print "D"

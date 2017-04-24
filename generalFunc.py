#data format: 2002001 2002-01-01 0 7 3
#Time as key
#Read into Dict: {'2002001': (0, 7, 3), ....... }
def readFileIntoDictTimeasKey(fileName, func):
    fread = open(fileName, 'r')
    listR = []
    line = "begin"
    while line:
        line = fread.readline()
        if len(line) < 1:
            break
        items = line.split();

        listR.append(func(items[1], items[2], items[3]))

    fread.close()
    return listR

#Number as key, but the number in order 465 => 456, 321 => 123
def makeInOrder(key1, key2, key3):
    num1 = int(key1)
    num2 = int(key2)
    num3 = int(key3)
    key = ""

    if num1 > num2:
        if num2 > num3:
            key = key3 + key2 + key1
        else:
            if num1 > num3:
                key = key2 + key3 + key1
            else:
                key = key2 + key1 +  key3
    else:
        if num1 > num3:
            key = key3 + key1 + key2
        else:
            if num2 > num3:
                key = key1 + key3 + key2
            else:
                key = key1 + key2 + key3

    return key


#Number as key
#if using the original numbers, the results as { '073': [], ....... }
#if using the numbers in order, the results as { '037': [], ....... }
#if using the sum of numbers, the results as { 10: [], ....... }
def readFileIntoDictNumberasKey(fileName, func):
    fread = open(fileName, 'r')
    dict = {}
    line = "begin"
    lineCount = 0
    while line:
        line = fread.readline()
        if len(line) < 1:
            break

        lineCount += 1
        items = line.split();

        key = func(items[1], items[2], items[3])
        # print key
        # print items[0]

        if(not key in dict):
            dict.setdefault(key, [])
        dict[key].append(items[0])

    fread.close()

    checkLineCount = 0
    for key in dict:
        checkLineCount += len(dict[key])

    if(lineCount == checkLineCount):
        return dict
    else:
        return {}


#Seperate the whole file into pieces according to time (year)
def seperateFileIntoPieces(fileName):
    fread = open(fileName, 'r')
    dict = {}
    line = "begin"
    preYear = ""
    fwrite = ""

    while line:
        line = fread.readline()
        if len(line) < 1:
            break

        items = line.split();

        year = items[0][:4]

        if(preYear != "" and preYear != year):
            fwrite.close()

        if(preYear == "" or preYear != year):
            fwrite = open('../' + year + '.txt', 'w')
            preYear = year

        fwrite.write(items[0] + "\t" + items[2] + "\t" + items[3] + "\t" + items[4] + "\n")


    fread.close()
    fwrite.close()

def translateToStr(item1, item2, item3):
    return item1 + item2 + item3

#calculate the sum of three numberSet
def calculateSum(item1, item2, item3):
    num1 = int(item1)
    num2 = int(item2)
    num3 = int(item3)

    return num1 + num2 + num3

#verify if it is zu 3
def verifyZu3(item1, item2, item3):
    if item1 == item2 and item1 != item3:
        return True

    if item1 == item3 and item1 != item2:
        return True

    if item2 == item3 and item1 != item2:
        return True

    return False

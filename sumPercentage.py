from generalFunc import readFileIntoDictTimeasKey, calculateSum

def writeGramToFile(fileName, dictGram):
    fw = open(fileName, 'w')
    for i in range(0, 10):
        fw.write( str(item) + "-" + str(dictGram[item]) + "\n")
    fw.close()

sumlist = []

#read all sums of three numbers into dict according to year
for year in range(2002, 2016):
    sumlist.extend( readFileIntoDictTimeasKey('../' + str(year) + '.txt', calculateSum))

#gram2
gram2 = {}
gram3 = {}
gram4 = {}

# for i in range(0, len(sumlist) - 1):
#     key = (sumlist[i], sumlist[i+1])
#
#     if not key in gram2:
#         gram2.setdefault(key, 0)
#
#     gram2[key] += 1
#
# print len(gram2)
#
# writeGramToFile('../gram2.txt', gram2)

for i in range(0, len( sumlist) - 2):
    key = (sumlist[i], sumlist[i+1], sumlist[i+2])

    if not key in gram3:
        gram3.setdefault(key, 0)

    gram3[key] += 1

fw = open('../gram3.txt', 'w')
for i in range(0, 28):
    for j in range(0, 28):
        for k in range(0, 28):
            if (i, j, k) in gram3:
                fw.write( str(i) + "\t" + str(j) + "\t" + str(k) + "\t" + str(gram3[(i, j, k)]) + "\n")
fw.close()


for i in range(0, len(sumlist) - 3):
    key = (sumlist[i], sumlist[i+1], sumlist[i+2], sumlist[i+3])

    if not key in gram4:
        gram4.setdefault(key, 0)

    gram4[key] += 1

fw = open('../gram4.txt', 'w')
for i in range(0, 28):
    for j in range(0, 28):
        for k in range(0, 28):
            for l in range(0, 28):
                if (i, j, k, l) in gram4:
                    fw.write( str(i) + "\t" + str(j) + "\t" + str(k) + "\t" + str(l) + "\t" + str(gram4[(i, j, k, l)]) + "\n")
fw.close()

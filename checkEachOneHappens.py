from generalFunc import readFileIntoDictTimeasKey, makeInOrder

dictYear ={}

allNumber = {}

for i in range(0, 10):
    for j in range(i, 10):
        for k in range(j, 10):
            allNumber[str(i) + str(j) + str(k)] = 1

numHappenedTotal = 90+120+10

for fileN in range(2002, 2016):
    dictYear[fileN] = readFileIntoDictTimeasKey('../' + str(fileN) + '.txt')

    numHappenedTotal += len(dictYear[fileN])

    for item in dictYear[fileN]:
        allNumber[makeInOrder(item[0], item[1], item[2])] += 1

fw = open('../groupSelectNumberPercent.txt', 'w')
for i in range(0, 10):
    for j in range(i, 10):
        for k in range(j, 10):
            fw.write(str(i) + str(j) + str(k) + ',')

            # print allNumber[str(i) + str(j) + str(k)]
            # print numHappenedTotal
            percent = float(allNumber[str(i) + str(j) + str(k)]) / float(numHappenedTotal)
            # print percent
            # raw_input()
            fw.write("%.9f\n" % (percent))

fw.close()

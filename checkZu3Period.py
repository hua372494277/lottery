from generalFunc import readFileIntoDictTimeasKey, translateToStr, verifyZu3

recordList = []

#read all sums of three numbers into dict according to year
for year in range(2002, 2016):
    recordList.extend( readFileIntoDictTimeasKey('../' + str(year) + '.txt', verifyZu3))

period = []
count = 0
sumPeriod = 0
maxPeriod = 0
minPeriod = 0

#print  recordList

for i in range(0, len(recordList)):
    if not recordList[i]:
        count += 1
    else:
        period.append(count)
        sumPeriod += count

        if i == 0:
            maxPeriod = count
            minPeriod = count
        else:
            if maxPeriod < count:
                maxPeriod = count
            if minPeriod > count:
                minPeriod = count

        count = 0

print period
print "\n"
print "average Period:", sumPeriod/len(period), "\n"
print "maxPeriod", maxPeriod, "\n"
print "minPeriod", minPeriod, "\n"

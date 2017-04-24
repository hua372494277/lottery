from generalFunc import readFileIntoDictNumberasKey, calculateSum

dictYear ={}

#read all sums of three numbers into dict according to year
for fileN in range(2002, 2016):
    dictYear[fileN] = readFileIntoDictNumberasKey('../' + str(fileN) + '.txt', calculateSum)

#the period of sum
fw = open('../sumOfNumbers.txt', 'w')
# fw.write("Year\t")
# for sum in range(0, 28):
#     fw.write( str(sum) + "\t")
# fw.write("\n")

for sum in range(0, 28):
    for year in range(2002, 2016):
        if sum in dictYear[year]:
            fw.write( str(len(dictYear[year][sum])) + "\t")
        else:
            fw.write( "0\t")
    fw.write("\n")
fw.close()

# #the time between two same sum
# fw = open('../periodBetweenSameSum.txt', 'w')
# for sum in range(0, 28):
#     fw.write("SUM: " + str(sum) + "\n")
#     for year in range(2002, 2016):
#         # print dictYear[year]
#
#         if not sum in dictYear[year]:
#             continue
#
#         if len(dictYear[year][sum]) < 2:
#             continue
#
#         for i in range(0, len(dictYear[year][sum]) - 1):
#             fw.write(str( int(dictYear[year][sum][i+1]) - int(dictYear[year][sum][i]) ) + "\t")
#
#         fw.write( "\n")
#
#     fw.write("\n")
# fw.close()

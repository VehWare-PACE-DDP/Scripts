from datetime import datetime

with open("log.txt") as sound_file :
    arrayS = []
    for line in sound_file:
        arrayS.append(line)

with open("timeLog.txt") as blink_file :
    arrayB = []
    for line in blink_file:
        arrayB.append(line)

fh = open("Delays.txt","w")

#print((len(arrayS)))
#print((len(arrayB)))

for i in range(len(arrayS)):
    a = arrayS[i]
    b = arrayB[i]
    a= int(a)
    b=int(b)
    c= b - a
    fh.write("Delay = %s"%c)

fh.close()
blink_file.close()
sound_file.close()

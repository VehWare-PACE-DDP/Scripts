from datetime import datetime

with open("timeLog.txt") as blink_file :
    lines_blink = blink_file.readlines()

with open("log.txt") as sound_file :
    lines_sound = sound_file.readlines()


for i in range(len(lines_blink)):
    tmp = lines_blink[i].split()
    times_blink = tmp[4]

for i in range(len(lines_sound)):
    tmp_2 = lines_sound[i].split()
    times_sound = tmp_2[4]


for i in range(len(times_sound)):
    #delays = int()  - int()
    datetime_object_1 = datetime.strptime(times_blink[i],'%b %d %Y %I:%M%p')
    datetime_object_2 = datetime.strptime(times_sound[i],'%b %d %Y %I:%M%p')

    time_1 = round(time.mktime(datetime_object_1.timetuple()))
    time_2 = round(time.mktime(datetime_object_2 .timetuple()))

    delays = time_1 - time_2

for i in range(len(delays)):
    print(delays[i])
    print(" ")

blink_file.close()
sound_file.close()

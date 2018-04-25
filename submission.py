# submission.py 

# Level2 - korrekte Loesung ermitteln
# for x in range(1,11,3):

# abgabe = "10:00:00 3 1 10:20:00 wrong 1 10:45:00 correct 2 10:20:01 correct"
abgabe = "00:59:22 24 656 06:24:33 correct 798 05:37:06 wrong 26 01:01:52 correct 202 17:02:50 wrong 8 04:31:10 wrong 397 04:40:04 correct 134 12:26:33 correct 312 06:52:25 correct 728 03:18:44 correct 895 01:05:06 correct 575 12:37:41 wrong 727 21:36:54 correct 371 11:45:19 correct 314 19:32:39 wrong 785 18:51:27 correct 845 08:35:08 wrong 549 04:25:28 correct 697 21:06:15 correct 385 04:35:47 wrong 618 06:12:13 correct 656 09:16:48 correct 964 16:53:33 wrong 901 05:19:55 correct 227 20:25:07 correct"
t = abgabe.split(" ")

startzeit = t[0]
submissions = t[1]
bestezeit = "23:59:59"
besteruser = -1

for position in range(2, len(t), 3):
    user = t[position]
    zeit = t[position+1]
    loesung = t[position+2]
    print("Abgabe: ",user, zeit, loesung)
    if (zeit < bestezeit and loesung == "correct"):
        bestezeit = zeit
        besteruser = user

print(besteruser, bestezeit)
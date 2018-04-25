# zeiten.py 

import sys

def zeitInSekunden(h, m, s):
    gesamt = 0
    gesamt += h * 3600
    gesamt += m * 60
    gesamt += s
    return gesamt

beginnZeit = sys.argv[1] # input("Beginnzeit: ")
endeZeit = sys.argv[2] # input("Endezeit: ")

# Zeit im Format HH:MM:SS
beginn = beginnZeit.split(":")
ende = endeZeit.split(":")
h = int(beginn[0])
m = int(beginn[1])
s = int(beginn[2])
beginnSekunden = zeitInSekunden(h, m, s)

h = int(ende[0])
m = int(ende[1])
s = int(ende[2])
endeSekunden = zeitInSekunden(h,m,s)

gesamt = endeSekunden - beginnSekunden
print(gesamt)
# diffzeit.py 

def zeitInSekunden(h, m, s):
    gesamt = 0
    gesamt += h * 3600
    gesamt += m * 60
    gesamt += s
    return gesamt

def diffzeit(beginnZeit, endeZeit):
    beginn = beginnZeit.split(":")
    ende = endeZeit.split(":")
    h = int(beginn[0])
    m = int(beginn[1])
    s = int(beginn[2])
    h1 = int(ende[0])
    m1 = int(ende[1])
    s1 = int(ende[2])

    beginnSekunden = zeitInSekunden(h, m, s)
    endeSekunden = zeitInSekunden(h1, m1, s1)
    differenz = endeSekunden - beginnSekunden
    return differenz

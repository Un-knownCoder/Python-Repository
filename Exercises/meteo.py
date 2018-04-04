# Controllo precipitazioni nevose

class Snow:
    def check(self):
        precipitazioni = []
        cm = 1
        while(cm != 0):
            if(cm != 0): # per non inserire lo 0 finale
                cm = int(input("Quantita' neve caduta[cm]... "))
                precipitazioni.append(cm)

        print("")

        MAX = max(precipitazioni)
        print("La precipitazione piu' abbondante e' stata di: " + str(MAX) + "cm")

        abbondanti = []
        for i in range(0, len(precipitazioni)):
            if(precipitazioni[i] >= 150):
                abbondanti.append(precipitazioni[i])

        if(len(abbondanti) > 0):
            somma = 0
            for i in range(0, len(abbondanti)):
                somma +=  abbondanti[i]
            print("La media delle precipitazioni abbondanti[ > 150cm] e' di: " + str(somma / len(abbondanti)))
                

snow = Snow()
snow.check()

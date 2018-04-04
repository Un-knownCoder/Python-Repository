
class Banca:
    def prelievo(self, type, conto):
        if(type == 0):
            if(conto >= 250):
                conto -= 250
            else:
                print("Non hai abbastanza soldi per effettuare il prelievo")
        else:
            if(conto >= 2500):
                conto -= 2500
            else:
                print("Non hai abbastanza soldi per effettuare il prelievo")
        return conto
#----------------------------------------------------------------------------

b = Banca()
conto = 20000

while(conto > 0):
    type = int(input("Che tipo di prelievo vuoi fare?[0, 1] "))
    if(type != 0 and type != 1):
        print("Error!!!")
    else:
        conto = b.prelievo(type, conto)
        print("Il tuo conto attuale ammonta a: " + str(conto))

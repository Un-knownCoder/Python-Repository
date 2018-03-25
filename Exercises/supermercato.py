# Supermercato

class Market:
    def calculateItem(self, Type, cost):
        out = 0;
        if(Type == 0):
            out = cost - (cost * 0.04)
            print("Il costo del prodotto e' di: " + str(out))
        elif(Type == 1):
            if(cost > 50):
                out = 50 - (50 * 0.04)
                out += (cost - 50) - ((cost - 50) * 0.08)
            else:
                out = cost - (cost * 0.4)
            print("Il costo del prodotto e' di: " + str(out))
        else:
            print("Errore... il prodotto selezionato non puo' essere venduto!!!")
# --------------------------------------------------------------------------------

market = Market()
t = int(input("Tipo prodotto[1,0]... "))
c = int(input("Tipo prodotto[euro]... "))

market.calculateItem(t, c)

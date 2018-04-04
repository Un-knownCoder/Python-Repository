# Calcolare se un numero e' primo

class Primo:
    def calculate(self, num):
        for i in range(3, (num/2)+1):
            if(num % i == 0):
                print("Il numero " + str(num) + " NON e' primo")
                return
        print("Il numero " + str(num) + " E' primo")
        return
# ------------------------------------------------------------

p = Primo()
n = int(input("Inserisci num... "))

p.calculate(n)



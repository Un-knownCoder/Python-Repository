# Il fattoriale di un numero (N!) indica il prodotto di tutti
#  i numeri minori uguali a N.
#  percio': 3! = 1 x 2 x 3 = 6

class Fattoriale:
    def calculate(self, num):
        out = 1
        for i in range(1, num+1):
            out *= i

        print(out)

#----------------------------------------------------------------

f = Fattoriale()
num = int(input("Inserisci un numero... "))
f.calculate(num)

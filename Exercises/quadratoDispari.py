# Si tratta di calcolare il quadrato di un numero N
#  sommando fra loro N numeri dispari partendo da 1

class Quadrato:
    def calculate(self, cont):
        n = 1
        out = 0
        for i in range(0, cont):
            out += n
            n += 2

        print(out)
#----------------------------------------------------

q = Quadrato()
num = int(input("Inserisci un numero... "))
q.calculate(num)

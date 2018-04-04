# Per stabilire se un numero e' perfetto bisogna
#  calcolare se e' dato dalla somma dei suoi divisori

class Perfetto:
    def calculate(self, num):
        P = Perfetto()
        value = p.getDivisori(num)
        out = 0
        for i in range(0, len(value)):
            out += value[i]

        if(out == num):
            return True
        else:
            return False


    def getDivisori(self, num):
        array = []
        for i in range(1, (num/2)+1):
            if(num % i == 0):
                array.append(i)
        return array

p = Perfetto()
Number = int(input("Inserisci num... "))
print(p.calculate(Number))

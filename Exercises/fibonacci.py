# sequenza di Fibonacci

# L'unica cosa da fare e' memorizzare due valori inizializzati a 1 e
#  - stampare la loro somma
#  - settare il primo uguale al secondo
#  - settare il secondo uguale alla somma
#  ... ripetere per X volte

class Fibonacci:
    def sequence(self, length):
        if(length > 0):
            first = 1;
            print(first)
        if(length > 1):
            second = 1;
            print(second)

            for i in range(0, length-2):
                out = first + second
                first = second
                second = out

                print(out)

# ---------------------------------------

f = Fibonacci()
l = int(input("Length... "))

f.sequence(l)

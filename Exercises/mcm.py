# Minimo comune Multiplo (m.c.m.)
# Il trucco consiste nel moltiplicare il maggiore tra i 2 numeri per il minore fino a che non si arriva al numero divisibile per entrambi

class Mcm:
    def calculate(self, num1, num2):
        MAX = max(num1, num2) # Trova il MAGGIORE tra i due numeri
        MIN = min(num2, num1) # Trova il MINORE tra i due numeri
        
        while(not(MAX % num1 == 0 and MAX % num2 == 0)): # Continua fino a quando non si trova il primo numero divisibile per entrambi
            MAX *= MIN 
        
        print("Il minor comune multiplo tra " + str(num1) + " e " + str(num2) + " e': " + str(MAX))
    
# ------------------------------------------------------------------------------------------------------------------------------------------

mcm = Mcm()

NUM1 = int(input("Inserisci numero... "))
NUM2 = int(input("Inserisci numero... "))

mcm.calculate(NUM1, NUM2)


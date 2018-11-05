import os
clear = lambda: os.system('cls')
clear()

## ## ## ## ## ## ## ## ## ## ##

def getC(exp):
   if(exp == 0):
      return [1]

   arr = [1, 1]
   for i in range(1, exp):
      narr = [1]*(len(arr)+1)
      for j in range(0, len(arr)-1):
         narr[j+1] = arr[j] + arr[j+1]

      arr = narr

   return arr

def calculate(coeff, a, b, exp):
   l = len(coeff)
   final = [1] * l
   final[0] = a**exp
   final[l-1] = b**exp
   for i in range(1, l-1):
     final[i] = coeff[i] * b**(i) * a**(l-1-i)
   
   return final

def printAll(final):
   tot = 0
   for i in range(0, len(final)):
      tot += final[i]

   print(str(final) + " = " + str(tot))

## ## ## ## ## ## ## ## ## ## ##

exp = int(input("Inserisci l'esponente... "))
a = int(input("Inserisci il primo numero... "))
b = int(input("Inserisci il secondo numero... "))
print("- - - - - - - - - -")

printAll(calculate(getC(exp), a, b, exp))

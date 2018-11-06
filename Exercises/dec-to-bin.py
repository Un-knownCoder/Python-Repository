import os
clear = lambda: os.system('cls')
clear()

## ## ## ## ## ## ## ## ## ## ##

def calculateBin(dec):
   d = dec
   res = []
   while(dec >= 1):
      res.append(dec % 2)
      dec = int(dec/2)
   
   cout(reverse(res), d)

def reverse(arr):
   nArr = [0] * len(arr)
   for i in range(0, len(nArr)):
      nArr[i] = arr[len(arr)-1-i]

   return nArr

def cout(arr, dec):
   string = "bin(" + str(dec) + ") = "
   for i in range(0, len(arr)):
      string += str(arr[i])

   print(string)

## ## ## ## ## ## ## ## ## ## ##

dec = int(input("Inserisci un numero in base 10: "))
print("- - - - - - - - - -")

calculateBin(dec)

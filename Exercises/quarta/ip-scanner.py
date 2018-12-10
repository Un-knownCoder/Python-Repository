import os
clear = lambda: os.system('cls')
clear()

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 

def calculateBin(dec):
   
	if(dec == 0):
		return 0
	
	d = dec
	res = []
	while(dec >= 1):
		res.append(dec % 2)
		dec = int(dec/2)

	while(len(res) < 8 or len(res) == 0):
		res.append(0)

	return get(reverse(res), d)

def reverse(arr):
   nArr = [0] * len(arr)
   for i in range(0, len(nArr)):
      nArr[i] = arr[len(arr)-1-i]

   return nArr

def get(arr, dec):
   string = ""
   for i in range(0, len(arr)):
      string += str(arr[i])

   return(string)

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 

IPAddress = input("<Input>:  Indirizzo IP = ")
ip = []

string = ""

for i in range (0, len(IPAddress)):
    if(IPAddress[i] == '.'):
        ip.append(int(string))
        string = ''
    elif(i == len(IPAddress)-1):
        string = string + IPAddress[i]
        ip.append(int(string))
    else:
        string = string + IPAddress[i]


## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
# Ricerca di errori nell'input
if(len(ip) != 4):
    print("<Error>:  Invalid ip address!")
    quit()

if((ip[0] > 255 or ip[0] < 0) or (ip[1] > 255 or ip[1] < 0) or (ip[2] > 255 or ip[2] < 0) or (ip[3] > 255 or ip[3] < 0)):
    print("<Error>:  Invalid ip address!")
    quit()
# Ricerca di errori nell'input
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 


t = ""
p = ""

ipString = str(ip[0]) + '.' + str(ip[1]) + '.' + str(ip[2]) + '.' + str(ip[3])
ipBinString = str(calculateBin(ip[0])) + "." + str(calculateBin(ip[1])) + "." + str(calculateBin(ip[2])) + "." + str(calculateBin(ip[3]))


if((ip[0] == 10) or (ip[0] == 172 and ip[1] == 16) or (ip[0] == 192 and ip[1] == 168)):
    p = "(privato) "
elif(ip[0] == 127):
    p = "(riservato [loopback]) "


if (ip[0] < 127):
	print()
	print("Address:   " + ipString + " >> " + ipBinString)
	print("- - - - -")
	print("NetMask:   255.0.0.0     >> 11111111.00000000.00000000.00000000")
	print("WildCard:  0.255.255.255 >> 00000000.11111111.11111111.11111111")
	print("- - - - -")
	print("Network:   " + str(ip[0]) + ".0.0.0       >> " + str(calculateBin(ip[0])) + ".00000000.00000000.00000000")
	print("HostMin:   " + str(ip[0]) + ".0.0.1       >> " + str(calculateBin(ip[0])) + ".00000000.00000000.00000001")
	print("HostMax:   " + str(ip[0]) + ".255.255.254 >> " + str(calculateBin(ip[0])) + ".11111111.11111111.11111110")
	print("BroadCast: " + str(ip[0]) + ".255.255.255 >> " + str(calculateBin(ip[0])) + ".11111111.11111111.11111111")
	print("Hosts/Net: " + str(2**24))
	print("")
   
	if(ip[1] == 0 and ip[2] == 0 and ip[3] == 0):
		t = ", ed e' un indirizzo di rete"
	elif (ip[1] == 255 and ip[2] == 255 and ip[3] == 255):
		t = ", ed e' un indirizzo di broadcast"

	print("<Explain>: " + str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + "." + str(ip[3]) + " e' un indirizzo " + p + "di classe A" + t)

elif (ip[0] < 192):
	print()
	print("Address:   " + ipString + " >> " + ipBinString)
	print("- - - - -")
	print("NetMask:   255.255.0.0     >> 11111111.11111111.00000000.00000000")
	print("WildCard:  0.0.255.255     >> 00000000.00000000.11111111.11111111")
	print("- - - - -")
	print("Network:   " + str(ip[0]) + "." + str(ip[1]) + ".0.0     >> " + str(calculateBin(ip[0])) + "." + str(calculateBin(ip[1])) + ".00000000.00000000")
	print("HostMin:   " + str(ip[0]) + "." + str(ip[1]) + ".0.1     >> " + str(calculateBin(ip[0])) + "." + str(calculateBin(ip[1])) + ".00000000.00000001")
	print("HostMax:   " + str(ip[0]) + "." + str(ip[1]) + ".255.254 >> " + str(calculateBin(ip[0])) + "." + str(calculateBin(ip[1])) + ".11111111.11111110")
	print("BroadCast: " + str(ip[0]) + "." + str(ip[1]) + ".255.255 >> " + str(calculateBin(ip[0])) + "." + str(calculateBin(ip[1])) + ".11111111.11111111")
	print("Hosts/Net: " + str(2**16))
	print("")
   
	if(ip[3] == 0 and ip[2] == 0):
		t = ", ed e' un indirizzo di rete"
	elif (ip[3] == 255 and ip[2] == 255):
		t = ", ed e' un indirizzo di broadcast"

	print("<Explain>: " + str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + "." + str(ip[3]) + " e' un indirizzo " + p + "di classe B" + t)
elif (ip[0] < 224):
	print()
	print("Address:   " + ipString + " >> " + ipBinString)
	print("- - - - -")
	print("NetMask:   255.255.255.0 >> 11111111.11111111.00000000.00000000")
	print("WildCard:  0.0.0.255     >> 00000000.00000000.11111111.11111111")
	print("- - - - -")
	print("Network:   " + str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + ".0   >> " + str(calculateBin(ip[0])) + "." + str(calculateBin(ip[1])) + "." + str(calculateBin(ip[2])) + ".00000000")
	print("HostMin:   " + str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + ".1   >> " + str(calculateBin(ip[0])) + "." + str(calculateBin(ip[1])) + "." + str(calculateBin(ip[2])) + ".00000001")
	print("HostMax:   " + str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + ".254 >> " + str(calculateBin(ip[0])) + "." + str(calculateBin(ip[1])) + "." + str(calculateBin(ip[2])) + ".11111110")
	print("BroadCast: " + str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + ".255 >> " + str(calculateBin(ip[0])) + "." + str(calculateBin(ip[1])) + "." + str(calculateBin(ip[2])) + ".11111111")
	print("Hosts/Net: " + str(2**8))
	print()
   
	if(ip[3] == 0):
		t = ", ed e' un indirizzo di rete"
	elif (ip[3] == 255):
		t = ", ed e' un indirizzo di broadcast"

	print("<Explain>: " + str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + "." + str(ip[3]) + " e' un indirizzo " + p + "di classe C" + t)
elif(ip[0] < 240):
	print()
	print("Address:   " + ipString + " >> " + ipBinString)
	print("- - - - -")
	print("NetMask:   255.255.255.0 >> 11111111.11111111.00000000.00000000")
	print("WildCard:  0.0.0.255     >> 00000000.00000000.11111111.11111111")
	print("- - - - -")
	print("Network:   " + str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + ".0   >> " + str(calculateBin(ip[0])) + "." + str(calculateBin(ip[1])) + "." + str(calculateBin(ip[2])) + ".00000000")
	print("HostMin:   " + str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + ".1   >> " + str(calculateBin(ip[0])) + "." + str(calculateBin(ip[1])) + "." + str(calculateBin(ip[2])) + ".00000001")
	print("HostMax:   " + str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + ".254 >> " + str(calculateBin(ip[0])) + "." + str(calculateBin(ip[1])) + "." + str(calculateBin(ip[2])) + ".11111110")
	print("BroadCast: " + str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + ".255 >> " + str(calculateBin(ip[0])) + "." + str(calculateBin(ip[1])) + "." + str(calculateBin(ip[2])) + ".11111111")
	print("Hosts/Net: " + str(2**8))
	print()
   
	if(ip[3] == 0):
		t = ", ed e' un indirizzo di rete"
	elif (ip[3] == 255):
		t = ", ed e' un indirizzo di broadcast"

	print("<Explain>: " + str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + "." + str(ip[3]) + " e' un indirizzo " + p + "di classe D" + t)
else:
	print()
	print("Address:   " + ipString + " >> " + ipBinString)
	print("- - - - -")
	print("NetMask:   255.255.255.0 >> 11111111.11111111.00000000.00000000")
	print("WildCard:  0.0.0.255     >> 00000000.00000000.11111111.11111111")
	print("- - - - -")
	print("Network:   " + str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + ".0   >> " + str(calculateBin(ip[0])) + "." + str(calculateBin(ip[1])) + "." + str(calculateBin(ip[2])) + ".00000000")
	print("HostMin:   " + str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + ".1   >> " + str(calculateBin(ip[0])) + "." + str(calculateBin(ip[1])) + "." + str(calculateBin(ip[2])) + ".00000001")
	print("HostMax:   " + str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + ".254 >> " + str(calculateBin(ip[0])) + "." + str(calculateBin(ip[1])) + "." + str(calculateBin(ip[2])) + ".11111110")
	print("BroadCast: " + str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + ".255 >> " + str(calculateBin(ip[0])) + "." + str(calculateBin(ip[1])) + "." + str(calculateBin(ip[2])) + ".11111111")
	print("Hosts/Net: " + str(2**8))
	print()
   
	if(ip[3] == 0):
		t = ", ed e' un indirizzo di rete"
	elif (ip[3] == 255):
		t = ", ed e' un indirizzo di broadcast"

	print("<Explain>: " + str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + "." + str(ip[3]) + " e' un indirizzo " + p + "di classe E" + t)
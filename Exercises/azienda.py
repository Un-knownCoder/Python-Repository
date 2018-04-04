
class Azienda:
    def bolletta(self, KwH):
        costo = 0
        if(KwH > 0 and KwH < 500):
            costo = 20
        elif(KwH < 1000):
            costo += 20
            costo += (KwH - 500) * 0.8
        else:
            costo += 20
            costo += 500 * 0.8
            costo += (KwH - 1000) * 0.5

        return costo

#-----------------------------------------------------------------------------

a = Azienda()
kwh = int(input("Inserire KW/h... "))
print(a.bolletta(kwh))

from enum import Enum
import random


class Karta:
    def __init__(self, figura, kolor):
        self.figura = figura
        self.kolor = kolor
        self.moc = 0 
    
    def kartatostring(self):
        return str(self.kolor) + ' ' + str(self.figura)

    def kolortoString(self):
        kolor = ""
        if self.kolor == 0:
            kolor = "Kier"
        elif self.kolor == 1:
            kolor = "Pik"
        elif self.kolor == 2:
            kolor = "Karo"
        elif self.kolor == 3:
            kolor = "Trefl"
        return kolor

    def getMoc(self):
        if self.figura == 1:
            self.moc == -1
        elif self.figura == 2:
            self.moc == 1
        elif self.figura == 3:
            self.moc == 1
        elif self.figura == 4:
            self.moc == 1
        elif self.figura == 5:
            self.moc == 1
        elif self.figura == 6:
            self.moc == 0
        elif self.figura == 7:
            self.moc == 0
        elif self.figura == 8:
            self.moc == 0
        elif self.figura == 9:
            self.moc == -1
        elif self.figura == 10:
            self.moc == -1
        elif self.figura == 11:
            self.moc == -1
        elif self.figura == 12:
            self.moc == -1
        elif self.figura == 13:
            self.moc == -1
        return self.moc

    def figuratoString(self):
        figura = ""
        if self.figura in range(2,11):
            figura = str(self.figura)
        elif self.figura == 1:
            figura = "As"
        elif self.figura == 11:
            figura = "Walet"
        elif self.figura == 12:
            figura = "Dama"
        elif self.figura == 13:
            figura = "Król"
        return figura

    def getFigura(self):
        return self.figura

    def getWartosc(self):
        wartosc = 0
        if self.figura > 1 and self.figura < 11:
            wartosc += self.figura
        elif self.figura == 1:
            wartosc += 11
        else:
            wartosc += 10
        return wartosc
    def getFigura(self):
        return self.figura


class Talia:
    def __init__(self):
        self.talia = []
       
    def generuj(self,liczbaTalii):
        for l in range(liczbaTalii):
            for i in range(4):
                for j in range(1,14):
                    self.talia.append(Karta(j, i))

    def tasuj(self):
        random.shuffle(self.talia)
    
    def rozdaj(self,n):
        karty = []
        for i in range(n):
            wydana = self.talia.pop(0)
            karty.append(wydana)
        return karty
    
    
    ######taliadogry.append(karta)

class Uczestnik:
    def __init__(self):
        self.parametrReki = random.randint(15,20)
        self.reka = []
        self.sumaReki = 0
        self.flagaReki = 0
        
    
    def getSumaReki(self):
        asy = 0
        sumaReki = 0
        for karta in self.reka:
            if karta.getFigura() == 1:
                asy += 1
            sumaReki += karta.getWartosc()
        
        while asy != 0 and sumaReki > 21:
            asy -= 1
            sumaReki -= 10
        return sumaReki 
    
    def getParametrReki(self):
        return self.parametrReki
    
    def getSumaMocy(self):
        sumaMocy = 0
        for karta in self.reka:
            sumaMocy += karta.getMoc()
        return sumaMocy

    #def SprawdzReke(self):
        if self.parametrReki < self.getSumaReki():
            self.flagaReki = False
        else:
            self.flagaReki = True
        return self.flagaReki
   

    def clearReka(self):
        self.reka.clear()
 

class Gracz(Uczestnik):
    def __init__(self,talia):
        super().__init__()
        self.imie = ""
        self.bank = 100
        self.parametrStolu = random.randint(-5,5)
        self.talia = talia

    def pokazKartyG(self):
        print("Karty gracza " + self.imie + ":" + "\n")
        for karta in self.reka:
            print(str(karta.getFigura()) + ' ' + str(karta.kolortoString()) + "\n")
        print("\n")

    def getParametrStolu(self):
        return self.parametrStolu
    
    def wygrana(self):
        print("Gracz " + self.imie + " wygrywa!" + "\n")
        self.bank += 10

    def przegrana(self):
        print("Gracz " + self.imie + " przegrywa!" + "\n")
        self.bank -= 10 

    def rozdajG(self):
        print("Rozdaję" + "\n")
        self.reka.extend(self.talia.rozdaj(2))
    
    def uderzG(self):
        print("Gracz " + self.imie + " dobiera")
        self.reka.extend(self.talia.rozdaj(1))   
        

class Dealer(Uczestnik):
    def __init__(self, talia):
        self.talia = talia
        super().__init__()
        
    def rozdajD(self):
        print("Rozdaję" + "\n")
        self.reka.extend(self.talia.rozdaj(2))
    
    def uderzD(self):
        print("Dealer dobiera!" + "\n")
        self.reka.extend(self.talia.rozdaj(1))

    def pokazKartyD(self):
        print("Karty Dealera: " + "\n")
        for karta in self.reka:
            print(karta.figuratoString() + ' ' + karta.kolortoString())
        print("\n")


class BlackJack:
    def __init__(self, liczbaTalii):
        self.liczbaTalii = liczbaTalii
        self.talia = Talia()
        self.talia.generuj(liczbaTalii)
        self.talia.tasuj()
        self.gracze = []
        self.grajacy = []
        self.dealer = Dealer(self.talia)
        self.wynikStolu = 0
        #self.trueWynikStolu = 0
        self.flagaTalii = False

    

    def przygotujRozgrywke(self,liczbaGraczy):
        if self.liczbaTalii != 1:
            self.flagaTalii = True
        for i in range(liczbaGraczy):
            self.gracze.append(Gracz(self.talia))
            self.gracze[i].imie = input("Podaj imię gracza: " + "\n")          

    def Gra(self,liczbaIteracji):
        for i in range(liczbaIteracji):
            print(50 * "=")
            print("Iteracja nr" + str(i) + "\n")
    
            for gracz in self.gracze:
                if gracz.getParametrStolu() > self.wynikStolu and gracz.bank > 0:
                    self.grajacy.append(gracz)
            
                self.dealer.rozdajD()
                self.dealer.pokazKartyD()
                for grajacy in self.grajacy:
                    grajacy.rozdajG()
                    grajacy.pokazKartyG()

                for gracz in self.grajacy:
                    sumaReki = gracz.getSumaReki()
                    mocReki = gracz.getSumaMocy()
                
                    if sumaReki < gracz.getParametrReki() and self.wynikStolu > gracz.getParametrStolu(): 
                        while self.wynikStolu > gracz.getParametrStolu() and gracz.sprawdzReke() == True:
                            gracz.uderz()
                            gracz.pokazKartyG()
                            if gracz.sprawdzReke() > 21:
                                gracz.przegrana()
                                self.grajacy.remove(gracz)
                    else:
                        continue

                while self.dealer.getSumaReki() < self.dealer.getParametrReki():
                    self.dealer.uderzD()
                    self.dealer.pokazKartyD()
                    if self.dealer.getSumaReki() > 21:
                        print("Dealer przekroczył 21!" + "\n")
                        
                        for gracz in self.grajacy:
                            gracz.wygrana()
                            gracz.clearReka()

                self.dealer.clearReka()
                print("Karty zostały spalone" + "\n")
                self.grajacy.clear()
            for gracz in self.gracze:
                print("Saldo gracza " + gracz.imie + ": " + str(gracz.bank))
            
            print("\n" + "Skończyłem Symulację " + "\n")




if __name__ == "__main__":
    gra = BlackJack(2)
    gra.przygotujRozgrywke(3)
    gra.Gra(5)
                    

                
                


        


        


    


        
         




    
    
    

        



    





    

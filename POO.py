
class Voituree:
    def __init__(self):
        self.essence=100
        
    def affiche_reservoir(self):
        print(f"la voiture contient {self.essence} littre d'essence")
        
    def  roule(self,km):
       if self.essence<=0:
           print("vous n'est plus d'essence")
        
       self.essence=self.essence-km*5/100
       if self.essence<10:
           print("vous n'avez plus d'esenec")
        
       
       self.affiche_reservoir()
     
    def faire_le_peilne(self):
         self.essence=100
         print("vous pouvvez repartir")
        
           
voitur=Voituree()  
voitur.roule(4)   
       
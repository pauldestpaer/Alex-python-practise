class Cats:
    _rating = 50

    def opinion():
        return "cats are great"
    def Rating(self):  
        return self._rating 
    def Better(self, ratingnumber):
        self._rating = self._rating + ratingnumber
        print("rating improved by ", ratingnumber)
    def Worse(self):
        self._rating = self._rating - 25
        print("rating reduced")

print(Cats.opinion())
splodge = Cats()
timtam = Cats()
splodge.Better(25)
timtam.Worse()
print(splodge.Rating(),timtam.Rating())
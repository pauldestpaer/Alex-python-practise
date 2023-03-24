class Cats:
    _rating = 50

    def opinion():
        return "cats are great"
    def Rating(self):  
        if self._rating > 50:
           print("this cat is good")
        elif self._rating == 50:
           print("this cat is mid")
        else:
            print("this cat sucks")
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
splodge.Rating
timtam.Rating
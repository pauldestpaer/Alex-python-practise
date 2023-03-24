class Cats:
    _rating = 50

    def opinion():
        return "cats are great"
    def Rating(self):  
        if self._rating > 50:
           print("this cat is good its rating is ",self._rating)
        elif self._rating == 50:
           print("this cat is mid its rating is ",self._rating)
        else:
            print("this cat sucks its rating is ",self._rating)
    def Better(self, ratingnumber):
        self._rating = self._rating + ratingnumber
        print("rating improved by ", ratingnumber)
    def Worse(self, ratingnumber):
        self._rating = self._rating - ratingnumber
        print("rating reduced by ", ratingnumber)

print(Cats.opinion())
splodge = Cats()
timtam = Cats()
mob = Cats()
splodge.Better(25)
mob.Worse(50)
splodge.Rating()
timtam.Rating()
mob.Rating()
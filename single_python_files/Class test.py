class Cats:
    _rating = 50

    def opinion():
        return "cats are great"
    def Rating(self):  
        if self._rating > 50:
           return "this cat is good its rating is " + str(self._rating)
        elif self._rating == 50:
           return "this cat is mid its rating is " + str(self._rating)
        else:
            return "this cat sucks its rating is " + str(self._rating)
    def Better(self, ratingnumber):
        self._rating = self._rating + ratingnumber
        return "rating improved by " + str(ratingnumber)
    def Worse(self, ratingnumber):
        self._rating = self._rating - ratingnumber
        return "rating reduced by " + str(ratingnumber)

print(Cats.opinion())
splodge = Cats()
timtam = Cats()
mob = Cats()
splodge.Better(25)
mob.Worse(50)
splodge.Rating()
timtam.Rating()
mob.Rating()

my_cats = []
my_cats.append(splodge)
my_cats.append(timtam)
my_cats.append(mob)

for cat in my_cats:
    rating = cat.Rating()
    print(rating)
class India():
    def type(self):
        print("India is a developing country.\n")

class USA():
    def type(self):
        print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()

for country in (obj_ind, obj_usa):
    country.type()
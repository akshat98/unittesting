from collections import namedtuple
Car = namedtuple('Car',['price', 'mileage', 'brand'])



car = Car(5000,200, "BMW")

print(car[0], car[1], car[2])
print(car.price, car.brand, car.mileage)



# but wont wont work if you want to cahnge the value again ,
#because tuple are immutable
# price defined is read only
# car.price = 10


car1 = Car(25000, 2000, "BMW")
assert car1.price == 25000
assert car1.mileage == 2000
assert car1.brand == "BMW"
assert isinstance(car1, tuple)

# Note that indexing works also!
# This means that if you change a tuple into a namedtuple,
# the change will be backwards compatible.
assert car1[2] == "BMW"

print("All good!")
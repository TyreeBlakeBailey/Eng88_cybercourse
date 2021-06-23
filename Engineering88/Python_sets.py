# sets are data collections but the difference is that they are unordered
#Syntax name = {}
# the data is given back in a random ordered


car_parts = {"wheels", "doors", "engine"}
print(car_parts)

# used to add an item
car_parts.add("windows")
print(car_parts)
# both used to remove an item from the list
car_parts.discard("doors")
car_parts.remove("doors")


#Frozen sets
frozen_set = ([1,3,5,6])
print(frozen_set) # frozen sets are always printed in the same ordered
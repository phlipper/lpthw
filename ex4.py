# number of cars
cars = 100

# number of seats per car
space_in_a_car = 4

# total number of drivers
drivers = 30

# total number of passengers
passengers = 90

# the number of cars _not_ driven
cars_not_driven = cars - drivers

# the total number of cars driven
cars_driven = drivers

# the total number of passengers who can travel today
carpool_capacity = cars_driven * space_in_a_car

# the average number of passengers per car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# extra credit

# Traceback (most recent call last):
#   File "ex4.py", line 8, in <module>
#     average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined

# ^^ The NameError above is due to the fact that the author typed
# `car_pool_capacity` but the actual variable is `carpool_capacity`, no
# underscore character between 'car' and 'pool'. NameError means the 'name'
# of the variable is unknown.

# > I used 4.0 for space_in_a_car, but is that necessary?
# > What happens if it's just 4?

# ^^ If the integer `4` was used vs. `4.0`, the `carpool_capacity` would be
# integer `120` vs. floating point `120.0`. The floating point is not
# necessary here in this case, but it doesn't hurt and is good practice to
# consider.
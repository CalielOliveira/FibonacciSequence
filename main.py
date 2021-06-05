# Getting the Fibonacci Sequence from rabbits and breeding
"""
The idea is to create the rabbit class and the breeding class,
make the rabbits procreate and as the population grows the Fibonacci shows :D

----Introduction to Fibonacci and his rabbits----
We start with a pair of rabbits,
they procreate a new pair of rabbits that also can procreate in the same way.
Every month all the rabbits procreate a new pair of rabbits,
but when a new pair is made, they take 1 month to start procreating and 1 month to give birth.
Then we want to know how the quantity of pairs grows monthly
We should get something like 1, 1, 2, 3, 5, 8 ...
"""

from breeding import Breeding

new_breeding = Breeding()

for _ in range(8):
    new_breeding.add_month()

print(list(new_breeding.rabbits_per_month.values()))

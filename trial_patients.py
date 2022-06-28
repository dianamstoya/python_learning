# trial_1 = {'Bob', 'Charley', 'Georgia', 'John'}
# trial_2 = {'Anne', 'Charley', 'Eddie', 'Georgia'}
#
# check_set = trial_1.intersection(trial_2)
# print(check_set)

wild_animals = {"sheep",
                "hen",
                "cow",
                "horse",
                "goat",
                }
farm_animals = {"panther",
                "lion",
                "elephant",
                "tiger",
                "goat",
                "horse",
                }
potential_rides = {"donkey",
                   "horse",
                   "camel"
                   }
intersection = farm_animals & wild_animals & potential_rides
print(intersection)
mounts = farm_animals.intersection(potential_rides,
                                   wild_animals)
print(mounts)
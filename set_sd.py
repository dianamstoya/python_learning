morning = {'a', 'b', 'c', 'd'}
afternoon = {'b', 'c', 'd', 'e'}

# not_in_both = morning.symmetric_difference(afternoon)

# the method works with lists as well
# the operator requires sets
not_in_both = morning ^ afternoon
print(not_in_both)
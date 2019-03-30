def unique_names(names1, names2):
    return list(set(names1).union(set(names2)))

################ CODE ENDS HERE ###################


# test cases
names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2))
# should print Ava, Emma, Olivia, Sophia

names3 = ["Ava", "Emma", "Olivia", 3, 5, (1, 2, 3)]
names4 = ["Olivia", "Sophia", "Emma", 5, 3, 6, (1, 2, 3), (1, 3, 2), (1, 2)]
print(unique_names(names3, names4))
# should print [(1, 2), 3, 5, 'Ava', 6, (1, 3, 2), (1, 2, 3), 'Emma', 'Sophia', 'Olivia']

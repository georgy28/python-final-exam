def unique_names(names1, names2):
    return list(set(names1).union(set(names2)))


# test case
names1 = ["Ava", "Emma", "Olivia", 3, 5, (1, 2, 3)]
names2 = ["Olivia", "Sophia", "Emma", 5, 3, 6, (1, 2, 3), (1, 3, 2), (1, 2)]
print(unique_names(names1, names2))
# should print Ava, Emma, Olivia, Sophia

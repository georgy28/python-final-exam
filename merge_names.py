def unique_names(names1, names2):
    return list(set(names1).union(set(names2)))


# test case
names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2))
# should print Ava, Emma, Olivia, Sophia

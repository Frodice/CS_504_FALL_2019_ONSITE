def first(n):
    return n[0]

def sort_list_first(tuples):
    return sorted(tuples, key=first)

a =[(5, 2), (2, 1), (4, 4), (3, 2), (1, 2)]
print(sort_list_first(a))
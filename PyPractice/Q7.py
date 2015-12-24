def overlapping(li1, li2):
	
    for elem1 in li1:
        for elem2 in li2:
            if elem1 == elem2:
                return True
    return False


print overlapping([1, 2], [3, 4])
print overlapping([1, 2], [2, 3])
print overlapping(['a', 'b', 'c'], ['c', 'd'])
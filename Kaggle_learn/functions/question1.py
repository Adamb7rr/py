def get_expected_cost(beds, baths):
    value = 80000
    while beds > 0:
        value += 30000
        beds -= 1
    while baths > 0:
        value += 10000
        baths -= 1
    
    return value

test1 = get_expected_cost(0,0)
print(test1)
test2 = get_expected_cost(1,2)
print(test2)
test3 = get_expected_cost(2,0)
print(test3)
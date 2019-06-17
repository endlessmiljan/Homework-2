import random
test_list1 = []
for i in range(10):
    r = random.randint(1, 10)
    if r not in test_list1: test_list1.append(r)
i = iter(test_list1)
print(list(zip(i, i)))
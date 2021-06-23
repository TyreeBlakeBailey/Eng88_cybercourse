list = [ 1, 2, 3, 4, 5, 6, 7 ]
a = 0
sum_num = []
for item in list:
    if a % 3 == 0:
        print(item)
        sum_num.append(item)
    a += 1

print(sum(sum_num))
    #print(a)

print(range())
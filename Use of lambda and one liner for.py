lst = list(range(1,11))

n = int(input("Enter The Number You Want Table of: "))

lst_2 = map(lambda x : x*n , lst)
for i in lst_2 :print(i)

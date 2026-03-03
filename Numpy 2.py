import numpy as np

rng = np.random.default_rng()

arr1 = np.arange(1,51)
#arr3 = []
#for i in range(50):
#    face = np.random.randint(0,2)
#    arr1.append(face)
sampleSpace = 10000
arr3 = rng.binomial(n=1, p = 0.5, size= sampleSpace)
#print(arr3)
#print()
numsam = rng.choice(arr1, size=8, replace=False)
print(numsam)
print()
ones = arr3[arr3 == 1]
zeros = arr3[arr3 == 0]
print(f"{ones.size/sampleSpace :.2f}")
print()
print(f"{zeros.size/sampleSpace :.2f}")
#arr2 = np.array(arr1)
#condition1= arr2 == 1
#condition0 = arr2 == 0
#ones = arr2[ condition1]
#zeros = arr2[condition0]
#print(ones.size)
#print()
#print(zeros.size)
#print()
#print(ones)
#print()
#print(zeros)
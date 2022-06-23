A = [10,20,30]
for i in range(len(A)):
    revindex = (i * -1)-1
    A[i] = A[revindex]
print(A)
A = input().split()
max = min = 0
for index in range(1,int(A[0])+1):
    A[index] = num = int(A[index])
    if num > max:
        max = num
    if min == 0 or num < min:
        min = num
print(max,min)
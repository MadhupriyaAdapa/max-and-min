a=[1,2,3,1,2,3,4,45,1,2,3]
max=a[0]
n=len(a)
for i in range(n):
    if a[i]>max:
        max=a[i]
print(max)
min=a[0]
for i in range(n):
    if a[i]<min:
        min=a[i]
print(min)
print(n)

# 1.Linear Search

def l_s(arr1,num):
    n=len(arr1)

    for i in range(n):
        if arr1[i]==num:
            return i
        
    return -1

arr1 = [10, 20, 30, 40, 50]
num = 30

result = l_s(arr1, num)

print("Element found at index:", result)

print( "-----------------------------------------------------------------------------------------")

# 2. Largest Element

arr2 = [10, 20, 30, 40, 50]
n=len(arr2)

largest = arr2[0]

# For largest element

for i in range(n):
    if arr2[i] > largest:
        largest = arr2[i]

print("Largest element:", largest)

# For second largest element

secondlargest = -1

for i in range(n):
    if arr2[i] > secondlargest and arr2[i] != largest:
        secondlargest = arr2[i]

print("Second largest element:", secondlargest)

print( "-----------------------------------------------------------------------------------------")

# 3. Maximum Consecutive 1s

num = [1, 1, 0, 1, 1, 1, 0, 1]

maxi = 0
cnt = 0

for i in range(len(num)):
    if num[i] == 1:
        cnt += 1
        maxi = max(maxi, cnt)
    else:
        cnt = 0

print("Maximum consecutive 1s:", maxi)

print( "-----------------------------------------------------------------------------------------")

# 4.Left Rotate Array by One

arr = [10, 20, 30, 40, 50]
n = len(arr)

temp = arr[0]

for i in range(1, n):
    arr[i - 1] = arr[i]

arr[n - 1] = temp

print("Left rotated array:", arr)

print( "-----------------------------------------------------------------------------------------")

# 5. Left Rotate Array by K

arr = [10, 20, 30, 40, 50]
n = len(arr)
d = 2

d = d % n

temp = []

for i in range(d):
    temp.append(arr[i])

for i in range(d, n):
    arr[i - d] = arr[i]

for i in range(n - d, n):
    arr[i] = temp[i - (n - d)]

print("Left rotated array:", arr)

print( "-----------------------------------------------------------------------------------------")

# 6. Move zero to end

arr = [1, 0, 3, 0, 5, 0, 2]
n = len(arr)

# Step 1
temp = []

for i in range(n):
    if arr[i] != 0:
        temp.append(arr[i])

# Step 2
for i in range(len(temp)):
    arr[i] = temp[i]

# Step 3
for i in range(len(temp), n):
    arr[i] = 0

print(arr)

print( "-----------------------------------------------------------------------------------------")

# 6. Find missing Number

arr = [1, 2, 4, 5]
n = 5

total = n * (n + 1) // 2

s2 = 0
for i in range(len(arr)):
    s2 += arr[i]

missing = total - s2

print("Missing number:", missing)

print( "-----------------------------------------------------------------------------------------")

# 7. find the leader 

a = [10, 22, 12, 3, 0, 6]
n = len(a)

leaders = []

for i in range(n):
    leader = True

    for j in range(i + 1, n):
        if a[j] > a[i]:
            leader = False
            break

    if leader == True:
        leaders.append(a[i])

print("Leaders:", leaders)

print( "-----------------------------------------------------------------------------------------")

# 8. Find the duplicate number

arr = [1, 2, 3, 2, 4, 5, 3]
n = len(arr)

duplicates = []

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] == arr[j] and arr[i] not in duplicates:
            duplicates.append(arr[i])

print("Duplicate numbers:", duplicates)

print( "-----------------------------------------------------------------------------------------")

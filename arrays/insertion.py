import array
arr = array.array('i', [1,2,3])
print('The newly created array is: ')
for i in range(0, 3):
    print(arr[i], end=" ")
print("\r")
arr.append(4)
print('The newly created array is: ')
for i in range(0, 4):
    print(arr[i], end = " ")

arr.insert(2,5)
print('array after insertion is: ')
for i in range(0, 5):
    print(arr[i], end=" ")

print('array after pop is: ')
arr.pop(2)
for i in range(0, 4):
    print(arr[i], end = " ")
arr.append(1)
print('array after remove is: ')
arr.remove(1)
for i in range(0, 4):
    print(arr[i], end = " ")














































































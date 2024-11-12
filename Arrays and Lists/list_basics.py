a = [4,8,6,4,9,8]

# print("max", max(a))
# print("min", min(a))

def find_max(arr):
    max_val = arr[0] # initialise max variable with first element
    for i in range(1, len(arr)): # range second element to last
        if max_val < arr[i]: # compare max variable with each element
            max_val = arr[i] # update the max variable
    return max_val

print("Custom max:", find_max(a))

# O(n)

def find_min(arr):
    min_val = arr[0] # initialise min variable with first element
    for i in range(1, len(arr)): # range second element to last
        if min_val > arr[i]: # compare min variable with each element
            min_val = arr[i] # update the min variable
    return min_val

print("Custom min:", find_min(a))

# reversing a list using loop

def reverse_list(arr):
    revered_list = []
    for item in range(1, len(arr)+1):
        revered_list.append(arr[-1*item])
    return revered_list
# O(n)

print("Revered list", reverse_list(a))


a = [4,8,6,4,9,8,10]

def reverse_list_optimised(arr):
    left = 0
    right = len(arr)-1
    while left <= right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

# n -> n/2
# O(n)

print("Revered list opt", reverse_list(a))



# output = a = [4,8,6,4,9,8,10]
# rotate the list by k positions
def rotate_right_by_k(arr, k):
    for item in range(k):
        last_element = arr.pop()
        arr.insert(0, last_element)

    return arr
print("rotate by right ",rotate_right_by_k(a,15))

# n^2
# #
# # def rotate_left_by_k(arr, k):
# #     arr[:3]
#
# a = [10,20,30,40,50] len()
# k = 6,1
# k%len(a)
# output = [50,10,20,30,40]

for i in range(1,5): # 1,2,3,4
    print(10%i)


























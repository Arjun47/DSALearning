# Write a function to calculate the sum of all elements in an array.
from itertools import count


def get_sum(arr):
    sum=0
    for i in arr:
        sum += i
    return sum



# print("Sum: ", get_sum(a))

# Given a list and a target element, count how many times the element appears in the list.

def count_x(arr, target):
    count=0
    for i in arr:
        if i == target:
            count +=1
    return count

def count_x_by_dict(arr,t):
    count_dict={}
    for i in arr:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return count_dict.get(t,0)

# Write a function to remove all duplicates from a list and return a list of unique elements.
# looping/primitive
def remove_duplicates(arr):
    seen = []
    for item in arr:
        if item not in seen:
            seen.append(item)
    return seen


# using built-in
def remove_duplicates1(arr):
    return list(set(arr))

a = [1,5,7,8,9,4,3,2,5,7,4,5]
# print("Unique items: ", remove_duplicates(a))
# print("Unique items: ", remove_duplicates1(a))


# Given two sorted lists, merge them into one sorted list.
x = [1,3,5,9]
y = [2,4,6,8]
def merge_two_lists(x,y):
    output=x+y
    output.sort()
    return output
# Write a function to find the second largest and second smallest element in a list.

a_ = [9,5,7,10,9,4,9,2,5,9,4,9]

def find_second_largest(arr):
    pass

# find the occurence of largest number in a list

def find_max_occ(arr):
    max_val = arr[0] # initialise max variable with first element
    count = 1
    for i in range(1, len(arr)): # range second element to last
        if max_val < arr[i]: # compare max variable with each element
            max_val = arr[i] # update the max variable
            count = 0
        if max_val == arr[i]:
            count+=1
    return max_val, count

print("Custom max:", find_max_occ(a_))

def count_x_by_dict_max(arr):
    count_dict={}
    for i in arr:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    sorted_dict = sorted(count_dict.items(), key=lambda m: m[0])
    return sorted_dict[-1][0], sorted_dict[-1][1]

print("Custom max:", count_x_by_dict_max(a_))

# Given an array and a target sum, find all pairs of elements that add up to the target sum.

a1 = [4,5,1,5,3,4,6,9,7,11]
t_sum = 14
def get_all_pairs(arr, t):
    pairs = set()
    for e in arr:
        diff = t-e
        if diff in arr and diff != e and (diff,e) not in pairs:
            pairs.add(tuple(sorted([diff,e])))
    return pairs
# O(n)
print("all pairs: ", get_all_pairs(a1,t_sum))


def find_all_pairs(arr, target):
    pairs = set()       # To store unique pairs
    seen = set()        # To track numbers we've already encountered

    for i in arr:
        difference = target - i
        if difference in seen:
            # Add the pair in a sorted tuple format to avoid duplicate pairs
            pairs.add(tuple(sorted((i, difference))))
        seen.add(i)

    return pairs

# print("count_by_min__________ ", find_all_pairs(a1, 14))

# Given an array of integers, move all even numbers to the front and odd numbers to the back while preserving the order of even and odd numbers.

def rearrange_by_parity(arr):
    even, odd = [],[]  # create two lists even and odd
    for el in arr: # iterate array and check for even and odd
        if el%2 == 0:  # if even append it in even list and vice versa
            even.append(el)
        else:
            odd.append(el)
    return even + odd  # combine both lists
print("Rearrange by parity: ", rearrange_by_parity(a1))

# Given an array of positive integers and a target sum, find a continuous subarray (subset of consecutive elements) that sums up to the target sum.


a2 = [3, 4, 1, 8, 7, 11,5, 1, 5, 15]
# sliding window
def get_sum_sub_array_continuous(arr,t):
    left = 0
    right = 0
    while left < len(arr):
        if sum(arr[left:right+1]) == t:
            return arr[left:right+1]
        elif sum(arr[left:right+1])<t:
            right+=1
        else:
            left+=1
            right = left
    return -1

print("target sub array sum: ", get_sum_sub_array_continuous(a2,14))

seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
seq2 = ['a', 'b', 'c', 'd', 'e', 'f']

a = [seq2[2 * j] for j in range(len(seq2)//2)]


# Python program to find if there are
# two elements with given sum
 
# function to check for the given sum
# in the array
 
 
def printPairs(arr, arr_size, sum):
 
    # Create an empty hash map
    # using an hashmap allows us to store the indices
    hashmap = {}
 
    for i in range(0, arr_size):
        temp = sum-arr[i]
        if (temp in hashmap):
            print('Yes')
            return
        hashmap[arr[i]] = i
    print("No")
 
 
# driver code
A = [1, 4, 45, 6, 10, 8]
n = 16
printPairs(A, len(A), n)



tuple_list = [(200, 1), (300, 5), (500, 1)]
print(max(tuple_list, key=lambda item: item[1]))
print(tuple_list)
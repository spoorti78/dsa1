# program to find all pairs of an integer array whose sum is equal to a given number

def find_pairs(arr, n, sum_of_no):
    n = len(arr)
    sum_of_no = 9
    pairs_count = 0
    for i in range(0, n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == sum_of_no:
                pairs_count += 1
                print("Pairs count = ", pairs_count)
arr = [0, 2, 1, 4, 6, 5 ,-2, 8, 9]
find_pairs(arr, n=arr, sum_of_no=8)

from array import array


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]

    print(left)
    print('.')
    print(right)
    print('.')

    left = merge_sort(left)
    right = merge_sort(right)

arr = [1,2,3,4,5,6,7,8,9,10]
merge_sort(arr)
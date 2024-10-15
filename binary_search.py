def binary_search(list, target):
    first = 0
    ''' 
    "First" is equal to the first index in the list, hence 0 
    '''
    
    last = len(list) - 1
    ''' 
    "Last" is equal to the last index in the list, hence the list length minus 1 (list starts at 0 and not 1) 
    '''

    while first <= last:
        '''
        Inside the loop, find the point in the middle of the list to later discard the non-used indexes.
        '''
        midpoint = (first + last) // 2

        if list[midpoint] == target:
            '''
            If the midpoint value is equal to the target, return the result and end the loop.
            '''
            return midpoint
        elif list[midpoint] < target:
            '''
            Else if the midpoint is smaller than the target, only continue to search the rest - excluding the "lesser" half of the list.
            '''
            first = midpoint + 1
        else:
            '''
            Else if the midpoint is bigger than the target, only continue to search the rest - excluding the "bigger" half of the list.
            '''
            last = midpoint - 1
    '''
    If this part of the code is reached, that means nothing is returned so far - which leaves only the possibility that the target does not exist in the loop
    '''
    return None

def verify(index):
    if index is not None:
        print(f"Target found at index {index}")
    else:
        print("Target not in list")

list_length: int = int(input("Enter the length that the list should be: "))
nums = [x for x in range(list_length)]

nums.sort()
'''
Binary search requires the list to be sorted, otherwise the algorithm would not work!
'''

target: int = int(input("Enter a target to search for using linear search: "))
result = binary_search(nums, target)
verify(result)
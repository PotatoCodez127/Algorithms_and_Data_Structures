'''
This algorithm is merely a binary_search but instead of returning the index of where the target lies, 
we are returning True or False ( if the target exists or not )

The reason that the algorithm of recursive_binary_search and binary_search is so different, is because the word
"recursive" in terms of a function, just means that an function calls itself - which means that instead of a while loop, 
we call the function within itself to create a recurring function.
'''

'''
O(log n)
N()
'''

def recursive_binary_search(list, target):
    '''
    In the previous binary search algorithm, we had a while loop that excecutes if first >= last, 
    where if the case was that the list was empty, first would be 0 and last would be -1 ([length of list = 0] -1).
    '''
    if len(list) == 0:
        return False

    else:        
        midpoint = len(list) // 2
        '''
        Get the middle of the list - while theres no use for first and last because we are only searching if the target exists, 
        and not where it is if it does exist
        ''' 

        if list[midpoint] == target:
            return True
            '''
            If the midpoint value is equal to the target, return the result [True].
            '''
    
        else:
            if list[midpoint] < target:
                '''
                If the mid-value of the list is less than the target, we can rerun the function with a different input.
                This time we use the input of the mid-value's index + 1 (since we already know that the mid-value is not equal to the target),
                up to the end of the list, discarding the "lesser" half of the list.
                '''
                return recursive_binary_search(list[midpoint + 1:], target)
            else:
                '''
                Else if the mid-value of the list is more than the target, we can rerun the function with a different input.
                This time we use the input of list[0] up to the midpoint of the list, discarding the "greater" half of the list.
                '''
                return recursive_binary_search(list[:midpoint], target)

def verify(result):
    print(f"Target found: {result}")

list_length: int = int(input("Enter the length that the list should be: "))
nums = [x for x in range(list_length)]

nums.sort()
''' 
Recursive Binary search requires the list to be sorted, otherwise the algorithm would not work!
'''

target: int = int(input("Enter a target to search for using linear search: "))
result = recursive_binary_search(nums, target)
verify(result)
def linear_search(list, target):
    for index in range(0, len(list)):
        if list[index] == target:
            return list[index]
    return None

def verify(index):
    if index is not None:
        print(f"Target found at index {index}")
    else:
        print("Target not in list")

list_length: int = int(input("Enter the length that the list should be: "))
nums = [x for x in range(list_length)]
target: int = int(input("Enter a target to search for using linear search: "))
result = linear_search(nums, target)
verify(result)
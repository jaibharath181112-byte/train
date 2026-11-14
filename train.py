seat_numbers = [101, 104, 108, 112, 115, 120, 125, 130, 135, 140, 145, 150]
target_seat = 130
print("train seat finder")
print("seats avilable:", seat_numbers)
print("find seat:", target_seat)
def binary_search(seats, target):
    low = 0
    high = len(seats) - 1
    steps = 0
    while low <= high:
        steps = steps + 1
        mid = (low + high) // 2
        print("Checking middle seat:", seats[mid])
        if seats[mid] == target:
            return mid, steps
        elif target < seats[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1, steps
index, steps = binary_search(seat_numbers, target_seat)
print("search result:")
if index != -1:
    print("seat avilable at index:", index)
else:
    print("Seat not found.")
print("tteps taken:", steps)
print("time complexity: O(log n)")
print("space complexity: O(1)")
def recursive_binary_search(seats, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    print("recursive check:", seats[mid])
    if seats[mid] == target:
        return mid
    elif target < seats[mid]:
        return recursive_binary_search(seats, target, low, mid - 1)
    else:
        return recursive_binary_search(seats, target, mid + 1, high)
recursive_index = recursive_binary_search(
    seat_numbers,
    target_seat,
    0,
    len(seat_numbers) - 1
)
print("Recursive Binary Search Result:")
if recursive_index != -1:
    print("Seat found at index:", recursive_index)
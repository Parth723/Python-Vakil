def find_duplicate(nums):
    tortoise = nums[0]
    hare = nums[0]

    while True:
        tortoise = nums[tortoise]  
        hare = nums[nums[hare]]     
        if tortoise == hare:
            break

    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return hare

input_array = [1, 3, 4, 2, 2]
print(find_duplicate(input_array))  

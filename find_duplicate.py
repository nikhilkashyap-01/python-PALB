nums = [1, 3, 4, 2, 2]

# Phase 1: Detect cycle
slow = nums[0]
fast = nums[0]

while True:
    slow = nums[slow]
    fast = nums[nums[fast]]
    if slow == fast:
        break

# Phase 2: Find entrance of cycle
slow = nums[0]

while slow != fast:
    slow = nums[slow]
    fast = nums[fast]

print("Duplicate number:", slow)
#Solution of Problem 2
def minimum_steps(nums, k):
    rem = nums[0] % k
    for num in nums:
        if num % k != rem:
            return -1
    arr = [(num - rem) // k for num in nums]
    arr.sort()
    median = arr[len(arr) // 2]
    steps = 0
    for val in arr:
        steps += abs(val - median)

    return steps

n = int(input())
nums = list(map(int, input().split()))
k = int(input())

print(minimum_steps(nums, k))

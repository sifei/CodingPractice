import sys
def main(nums, target):
    nums.sort()
    result = 0
    minGap = sys.maxint
    
    for i in range(0, len(nums)):
        j = i + 1
        k = len(nums) - 1

        while j < k:
            Sum = nums[i] + nums[j] + nums[k]
            Gap = abs(Sum - target)
            if Gap < minGap:
                result = Sum
                MinGap = Gap
            if Sum < target:
                j += 1
            else:
                k -= 1
        

        
    return result

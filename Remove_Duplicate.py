def main(nums):
    if len(nums) == 0:
        return 0
    index = 1
    for i in range(1,len(nums)):
        if nums[i] != nums[index-1]:
            nums[index] = nums[i]
            index += 1
    return index

def main(nums, target):
    index = 0
    for i in range(0,len(nums)):
        if nums[i] != target:
            nums[index] = nums[i]
            index += 1
                
    return index

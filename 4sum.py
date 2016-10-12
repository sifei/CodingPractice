def main(nums, target):
    nums.sort()
    result = []
    
    for i in range(0, len(nums)-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums)-2):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            k = j + 1
            l = len(nums) -1
            while k < l:
                Sum = nums[i] + nums[j] + nums[k] + nums[l]
                if Sum < target:
                    k += 1
                    while nums[k] == nums[k-1] and k < l:
                        k += 1
                elif Sum > target:
                    l -= 1
                    while nums[l] == nums[l+1] and k < l:
                        l -= 1
                else:
                    result.append([nums[i],nums[j],nums[k],nums[l]])
                    k += 1
                    l -= 1
                    while nums[k] == nums[k-1] and k < l:
                        k += 1
                    while nums[l] == nums[l+1] and k < 1:
                        l -= 1           
    return result
    
    
def main1(nums, target):
    if len(nums) < 4:
        return nums
    result = []
    nums.sort()
    cache = {}
    for i in range(0,len(nums)):
        for j in range(i+1, len(nums)):
            key = nums[i] + nums[j]
            if key in cache:
                cache[key].append([i,j])
            else:
                cache[key] = [[i,j]]

    used = {}
    for i in range(0,len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums)-2):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            try:
                value = cache[target - nums[i]-nums[j]]
            except:
                value = []
            if len(value) == 0:
                continue
            for pair in value:
                print j,pair
                if j >= pair[0]:
                    continue
                sol = [nums[i],nums[j],nums[pair[0]],nums[pair[1]]]
                sol.sort()
                if not str(sol) in used:
                    result.append(sol)
                    used[str(sol)] = 1
    return result    
    

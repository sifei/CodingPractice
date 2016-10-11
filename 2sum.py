def main(nums, target):
    dic = {}
    idx = 1
    for num in nums:
        dic[num] = idx
        idx += 1
    for key in dic.keys():
        if target-key in dic:
            return dic[key], dic[target-key]
    return None

def main(nums):
    dic = {}
    for num in nums:
        dic[num] = 1
    longest = 0
    for key in dic.keys():
      length = 1
        up = key+1
        while up in nums:
            length += 1
            dic.pop(up,None)
            up += 1
        down = key-1
        while down in nums:
            length += 1
            dic.pop(down,None)
            down -= 1
        longest = max(longest, length)
    return longest

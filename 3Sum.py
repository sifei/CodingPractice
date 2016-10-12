def main(s):
    s.sort()
    target = 0
    result = []
    for i in range(0,len(s)-2):
        if i>0 and s[i] == s[i-1]:
            continue
        j = i + 1
        k = len(s) - 1
        while (j<k):
            if s[i]+s[j]+s[k] < target:
                j += 1
                while s[j] == s[j-1] and j < k:
                    j += 1
            elif s[i]+s[j]+s[k] > target:
                k -= 1
                while s[k] == s[k+1] and j < k:
                    k -= 1
            else:
                result.append([s[i],s[j],s[k]])
                j += 1
                k -= 1
                while s[j] == s[j-1] and j < k:
                    j += 1
                while s[k] == s[k+1] and j < k:
                    k -= 1
    return result
    

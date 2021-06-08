def min_max(num):
    minor = num[0]
    mayor = num[0]
    for x in num:
        if x < minor:
            minor = x
        if x > mayor:
            mayor = x
    return minor, mayor

data = [5, 6, 8, 2]
print(min_max(data))

data_new = [1, 2, 3]
print(min(data_new))
print(max(data_new))


def miniMaxSum(nums):
    s = 0
    maximun = 0
    minimun = 9999999999999
    n = len(nums)
    for x in range(n):
        s += nums[x]
        minimun = min(minimun, nums[x])
        maximun = max(maximun, nums[x])
    print(s-maximun, s-minimun)
    

print(miniMaxSum([1,3,4]))


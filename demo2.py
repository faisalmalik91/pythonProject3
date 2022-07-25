def singleNumber(nums):
    # applying the formula.
    res = nums[0]
    for i in range(0,len(nums)):
        res = res^nums[i]
        print('count of {} is {}'.format(nums[i],nums.count(nums[i])))

    return res
    #return 2 * sum(set(nums)) - sum(nums)


from collections import Counter
def coutOfEachChar(nums):
    a = Counter(nums)
    print(a)
    print(type(a))
    print(a.most_common())

# driver code
a = [2, 3, 5, 4, 5, 3, 4,4,4,5]
#a = ['a','b', 'c', 'a', 'b', 'c','d']
#print((coutOfEachChar(a)))
print(int(singleNumber(a)))

a = [15, 18, 16, 18, 16, 15, 89]
print(int(coutOfEachChar(a)))
#print(int(singleNumber(a)))



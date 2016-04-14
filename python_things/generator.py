def simple_gen(nums):
    for i in nums:
        yield (i+i)

my_nums = simple_gen([1,2,3,4,5])
for i in range(0,5):
    print next(my_nums)

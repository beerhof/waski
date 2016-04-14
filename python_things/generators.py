def square_numbs(numbs):
    for i in numbs:
        yield (i)
my_numbs = square_numbs ([1,2,3,4,5])
print "-NEXT GENERATOR ELEMENT-".center(40)
for i in range(0,5):
    print next(my_numbs)


def len_elements(numbs):        #-----how-to-count-elements-from-generator
    for i in numbs:
        yield (i)
my_numbs_len = len_elements ([1,2,3,4,5])
print "-GENERATOR ELEMENTS COUNT-".center(40)
print len(list(my_numbs_len))


def for_state():
    numbs_list = [1,2,3,4,5]
    print "-FOR STATEMENT-".center(40)
    for numb in numbs_list:
         print numb
for_state()

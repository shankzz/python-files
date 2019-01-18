def sum_all(*args):    #using *args
    """ this uses all arguements as a tuple"""
    total=0
    for num in args:
        total+=num
    return total

print(sum_all(1,2,3,4,5,6,6))
print(sum_all(2,4,6,8,10))
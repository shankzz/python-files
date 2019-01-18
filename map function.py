nums = [1,2,3,4,5,6]

sq = map(lambda x: x**2,nums)
print(sq)
ls = list(sq)
print(ls)

people = ["hari","swatz","asha","sudhir"]
upper = list(map(lambda name: name.upper(),people))
print(upper)
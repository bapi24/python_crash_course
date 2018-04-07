list1 = [23, 32, 24, 4243, 242, 241]

list2 = ['jana', 'jeeib', 'reid', 'carl', 'max']

contents = dict(zip(list2, list1))

def myfunction(s):
    return s[-1]

s_list1 = sorted(list1)

s_list2 = sorted(list2, key = myfunction)
print(s_list1)
print(s_list2)
print(contents)

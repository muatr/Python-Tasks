# 1- Write a function that flattens a list. Its elements can consist of multi-layered lists (such as [[3],2]) or non-scalar data. For example:
# sample input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# sample output: [1,'a','cat',2,3,'dog',4,5]

def flat(l):
    flatten = []
    for i in l:
        if type(i) == list:
            flatten.extend(flat(i))
        else:
            flatten.append(i)
    return flatten
list1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flat(list1))

# 2- Write a function that reverses the elements in the given list. If the elements inside the list also contain the list, reverse their elements as well. For example:
# sample input: [[1, 2], [3, 4], [5, 6, 7]]
# sample output: [[7, 6, 5], [4, 3], [2, 1]]

def rev(l):
    l.reverse()
    for i in l:
        if type(i) == list:
            i.reverse()
    return l
list2 = [[1, 2], [3, 4], [5, 6, 7]]
print(rev(list2))


list1 = []
list1 = [1,3,5]
list2 = [1,2,3,4]
list3 = list1 + list2
print('d) list3 is:',list3)
print('e) list3 contains a 3:',3 in list3)
print('f) list3 contains',list3.count(3),'3s')
print('g) The index of the first 3 contained in list3 is',list3.index(3))
first3 = list3.pop(1)
print('h) first3 =',first3)
list4 = sorted(list3)
print('j) list3 is now:',list3,'\nj) list4 is:',list4)
print('k) Slice of list3 is:',list3[2:5])
print('l) Length of list3 is',len(list3))
print('m) The max value in list3 is', max(list3))
print('n) Sorted list3 is:', sorted(list3))
list5 = [list1]+[list2]
print('o) list5 is:',list5)
print('p) Value 4 from list5: ',list5[1][3])



a = 9
b = 14

print('a) binary of a =', bin(a),'\nb) binary of b =', bin(b))
print('c) binary of a & b =',bin(a&b))
print('d) binary of a | b =',bin(a|b))

'''
Execution results:
a) binary of a = 0b1001 
b) binary of b = 0b1110
c) binary of a & b = 0b1000
d) binary of a | b = 0b1111
'''


'''
Second Script – question e: Examine the results. Can you see how they were arrived at?
a = 9, binary of a = 0b1001. Here ‘0b’ means binary.
a 0b1000
b 0b1111
---------- a & b output is one only if a and b are both one
  0b1000

a 0b1000
b 0b1111
---------- a | b output is zero only if a and b are both zero
  0b1111
'''

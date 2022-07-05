

import re

#
# if __name__=='__main__':
#     print(*filter(None, r'[.,]+', input()), sep='/n')

#split
# txt="welcome to jungle"
# x=txt.split()
# # print(x)
# li=[]
# for i in range(2):
#     i=input("Enter any Name:--")
#     li.append(i)
#
#
# print(li)

m=re.search('(?<=abc)def','abcdef')
print(m.group(0))


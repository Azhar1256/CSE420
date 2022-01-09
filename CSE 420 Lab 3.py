import re

re_nums=int(input())
re_list=[]
for i in range(re_nums):
    re_list.append(input())
txt_nums=int(input())
txt_list=[]
for i in range(txt_nums):
    txt_list.append(input())

for i in range(len(txt_list)):
    for j in range(len(re_list)):
        x = re.search(re_list[j], txt_list[i])
        if x !=None:
            print('YES,',str(j+1))
            break
        if j==len(re_list)-1 and x ==None:
            print('NO, 0')
            break

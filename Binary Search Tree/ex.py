students=[]
students_num= int(input())
for i in range(0,students_num-1) :
    students.append(list(map(int,input().split())))
f_benchers=int(input())
f_benchers_pos=[]
for i in range(f_benchers):
    f_benchers_pos.append(list(map(int,input().split())))

adjacent_list=[]
for data in students:

    if data[0]==(data[1]-1) and data[0] not in f_benchers_pos[0] and data[1] not in f_benchers_pos[0]:
        adjacent_list.append(data)
print(len(adjacent_list))

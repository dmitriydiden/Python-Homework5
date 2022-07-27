'''
Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. 
Порядок элементов менять нельзя.

Пример:
[1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
[1, 5, 2, 3, 4, 1, 7] => [1, 5]
'''
list =[1, 5, 2, 4, 0, 1, 7, 9, 8]
with open("data.txt", 'a') as data:
    data.writelines(str(list))
    data.writelines(' => ')
while len(list)!=0:
    max_n = max(list)
    list1 = [max_n]
    list.remove(max_n)
    for i in range(len(list)):
        for i in list:
            if i==max_n or i==max_n-1:
                list1.append(i)
                max_n=i
                list.remove(i)
    list2=[min(list1), max(list1)]           
    with open("data.txt", 'a') as data:
        data.writelines(str(list2))
path = 'data.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close() 





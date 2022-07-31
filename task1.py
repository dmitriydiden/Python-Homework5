'''
Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов. Это не просто сумма всех коэффициентов.
Сумма многочленов равна многочлену, членами которого являются все члены данных многочленов.
например, в 1 файле было 3*x^3 + 5*x^2+10*x+11, в другом 7*x^2+55
то в итоге будет, 3*x^3 + 12*x^2+10*x+66
'''


from importlib.resources import path

with open("file1.txt", 'a') as data:
    data.writelines('3*x^3 + 5*x^2 + 10*x^1 + 11')
with open("file2.txt", 'a') as data:
    data.writelines('7*x^2 + 55')
path = 'file1.txt'
data = open(path, 'r')
s1 = ''
for line in data:
    s1+=line
data.close()

path = 'file2.txt'
data = open(path, 'r')
s2 = ''
for line in data:
    s2+=line
data.close()
print(f"Многочлен 1: {s1}")
print(f"Многочлен 2: {s2}")

ssfinal=[]
def convert(s1):
    ss1=[]
    s = ''
    for i in s1:
        if i in ['+', '-']:
            ss1.append(s)
            s=''
            ss1.append(i)
        else:
            s+=i
    ss1.append(s)
    return ss1        
ss1 = convert(s1)
ss2 = convert(s2)

if (int(ss1[0].split('^')[-1])) > int((ss2[0].split('^')[-1])):
    start = ss1
    maxst = int(ss1[0].split('^')[-1])
kk1 = 1
kk2 = 1

for st in range(maxst, 0, -1):
    k1=0
    try:
        if int(ss1[0].split('^')[-1]) == st:
            k1 = int(ss1[0].split('*')[0])
            ss1.pop(0)
            #ss1.pop(0)
    except:
        k1=0       
    k2=0
    try:
        if int(ss2[0].split('^')[-1]) == st:
            k2 = int(ss2[0].split('*')[0])
            ss2.pop(0)
            #ss2.pop(0)           
    except:
        k2=0
    if ((k1*kk1)+(k2*kk2))>0:
        ssfinal.append("+")
    else:
        ssfinal.append("-")
    ssfinal.append(f"{abs((k1*kk1)+(k2*kk2))}*x^{st}")


    if ss1[0] == '+':
        kk1 = 1
        ss1.pop(0)
    elif ss1[0 == '-']:
        kk1 = -1
        ss1.pop(0)
    if ss2[0] == '+':
        kk2 = 1
        ss2.pop(0)
    elif ss2[0] == '-':
        kk2 = -1
        ss2.pop(0)

k1, k2 = int(ss1[0]), int(ss2[0])
if (k1+k2)>0:
    ssfinal.append("+")
else:
    ssfinal.append("-")   
ssfinal.append(str(k1+k2))
ssfinal.pop(0)

with open("file3.txt", 'w') as data:
    data.writelines(ssfinal)
s3=''
path = 'file3.txt'
data = open(path, 'r')
for line in data:
    s3+=line
data.close()   
print(f"Сумма многочленов: ({s1}) + ({s2}) = {s3}")





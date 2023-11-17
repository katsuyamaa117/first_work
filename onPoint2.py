import matplotlib.pyplot as plt

f = open("PZ_Mon_v_radia_1.dat", "r")
file = f.readlines()

list_x = []
list_y = []
for i in range(1,len(file)):
    list1 = file[i].split()
    list_x.append(float(list1[0]))
    list_y.append(float(list1[1]))

plt.scatter(list_x, list_y)
plt.xlabel('MJD')
plt.ylabel('Vr')
plt.title('График зависимости лучевой скорости от Юлианской даты')
plt.show()
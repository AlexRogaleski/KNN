# import PrepareDataSet as Pds
# from os import listdir, mkdir
# from os.path import isfile, join, exists
import numpy as np

FOLDER = "../Files/GesturePhasesDataset/workData/K"
k3_file = open((FOLDER + "3/acuracia.txt"), 'r')
k5_file = open((FOLDER + "5/acuracia.txt"), 'r')
k10_file = open((FOLDER + "10/acuracia.txt"), 'r')
k3 = k3_file.readlines()
k5 = k5_file.readlines()
k10 = k10_file.readlines()

# print(k3)
# print(k5)
# print(k10)
for i in range(len(k3)):
    char = k3[i].replace("\n", "")
    k3[i] = char
for i in range(len(k5)):
    char = k5[i].replace("\n", "")
    k5[i] = char
for i in range(len(k10)):
    char = k10[i].replace("\n", "")
    k10[i] = char
todo = [k3, k5, k10]

print("k = ", str(len(k3)))

tres = 0
cinco = 0
dez = 0
for i in range(len(k3)):
    if k3[i] > k5[i]:
        if k3[i] > k10[i]:
            tres += 1
        else:
            if k5[i] > k10[i]:
                cinco += 1
            else:
                dez += 1
    else:
        if k5[i] > k10[i]:
            cinco += 1
        else:
            if k3[i] > k10[i]:
                tres += 1
            else:
                dez += 1

print("k3 = ", tres, " k5 = ", cinco, " k10 = ", dez)

print(tres + cinco + dez)

# ('k3 = ', 9, ' k5 = ', 0, ' k10 = ', 3)

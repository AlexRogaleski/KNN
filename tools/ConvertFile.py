import PrepareDataSet as Pds
from os import listdir, mkdir
from os.path import isfile, join, exists
import numpy as np

FOLDER = "../" + Pds.PATH + "/"
SAVE_FOLDER = FOLDER + "converted/"

files = [f for f in listdir("../" + Pds.PATH) if isfile(join("../" + Pds.PATH, f)) and "windowed" in f]
files.sort()
# print(files)


def convert_file():
    # for i in range(len(files)):
    for i in range(1):
        file_x = open((FOLDER + files[i]), 'r')
        if not exists(SAVE_FOLDER):
            mkdir(SAVE_FOLDER)
        training_file = open((SAVE_FOLDER + "TR - " + files[i]), 'w')
        test_file = open((SAVE_FOLDER + "TE - " + files[i]), 'w')
        count_file = open((SAVE_FOLDER + "N - " + files[i]), 'w')
        lines_x = file_x.readlines()
        d, p, s, h, r = 0, 0, 0, 0, 0
        test = lines_x[0].split(",")
        w_line = []
        w_line.append(str(range(0, len(test) - 1)).replace("[", "").replace("]", "") + ", Phase\n")
        for index in range(len(lines_x)):
            # print(lines_x[index], "   " + str(len(lines_x[index])), "   ", lines_x[index][len(lines_x[index]) - 2:len(lines_x[index]) - 1])
            char = lines_x[index][len(lines_x[index]) - 2:len(lines_x[index]) - 1]
            if char == "D":
                d += 1
            if char == "P":
                p += 1
            if char == "S":
                s += 1
            if char == "H":
                h += 1
            if char == "R":
                r += 1
            w_line.append(lines_x[index].replace(char, Pds.convert_target_name(char)))

        count_line = ("D = " + str(d) + "\n" + "P = " + str(p) + "\n" + "S = " + str(s) + "\n" + "H = " + str(h) + "\n" + "R = " + str(r))
        count_file.write(count_line)
        count_file.close()

        for index in range(0, (int(len(w_line) * 0.7))):
            training_file.write(w_line[index])
        training_file.close()

        for index in range(int(len(w_line) * 0.7), len(w_line)):
            test_file.write(w_line[index])
        test_file.close()


convert_file()
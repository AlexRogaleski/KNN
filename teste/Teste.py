from facade import KNNClassifier as Knn
from os import listdir
from os.path import isfile, join
from tools import PrepareDataSet as Pds


x = [[2, 2, 2], [4, 4, 4], [5, 5, 5], [3, 3, 3], [5.1, 5.1, 5.1], [1, 1, 1]]
y = ['a', 'b', 'b', 'a', 'b', 'a']
test = [2, 2, 2]

clf = Knn.KNNClassifier(x, y, 2)
# for item in clf.classify(test):
#     print str(item.x) + " " + str(item.y)

print clf.classify(test)


files = [f for f in listdir("../Files/GesturePhasesDataset/workData/") if isfile(join(Pds.PATH, f)) and "windowed" in f]

print files
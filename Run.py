from tools import PrepareDataSet as Pds
from os import listdir
from os.path import isfile, join
from facade import KNNClassifier as Knn
import numpy as np
from sklearn.metrics import confusion_matrix


TRAINING = 0
TEST = 1

k = 5  # 3

files = [f for f in listdir(Pds.PATH) if isfile(join(Pds.PATH, f)) and "windowed" in f]  # b1_va3_windowed  windowed

files.sort()

print(files)
# print(len(files))

data = [Pds.get_dataset(Pds.PATH+"/"+file) for file in files]

data_x = [Pds.get_training_data(Pds.TRAINING_SLICE, data[index]['x'], type='x') for index in range(len(data))]
print(data_x)
data_y = [Pds.get_training_data(Pds.TRAINING_SLICE, data[index]['y'], type='y') for index in range(len(data))]


clfs = [Knn.KNNClassifier(data_x[index][TRAINING], data_y[index][TRAINING], k) for index in range(len(data))]
# clf = knn.KNNClassifier(data_x[1][1], data_y[1][1], k)


# results = []
# for index in range(len(clfs)):
#     predictions = []
#     for inner in range(len(data_x[index][1])):
#         predictions.append(clfs[index].classify(np.squeeze(np.asarray(data_x[index][TEST][inner]))))
#     results.append(predictions)
#
# print len(results)
#
# print len(data_y[index][TEST])
#
# print len(results[0])
#
# confusions_matrix = [confusion_matrix(data_y[index][TEST], results[index]) for index in range(len(results))]
#
# for index in range(len(confusions_matrix)):
#     with open(str(files[index])+"_confusion_matrix.txt", 'w') as f:
#         f.write(confusions_matrix[index])

# for item in results:
#     confusion_matrix(test_instances[]results[item]

acuracia = []
for i in range(len(files)):
    range_data = data_x[i][TEST].shape
    results = []
    # for index in range(len(clfs)):
    predictions = []
    for inner in range(len(data_x[i][TEST])):
        predictions.append(clfs[i].classify(np.squeeze(np.asarray(data_x[i][TEST][inner]))))
    #     print ("valor real, ", data_y[i][TEST][inner])
    #     print ("predicao",predictions[len(predictions)-1])
    #     print ("Iteracao", len(predictions))
    #
    # print('tampred', len(predictions))
    # print('tamy', len(data_y[i][TEST]))


    cm = confusion_matrix(data_y[i][TEST], predictions, Pds.TARGET_NAMES)

    acuracia.append(((np.sum(np.diag(cm))*100)/range_data[0]))

    print('acuracia', acuracia, ' %', str(i))

    Pds.plot_confusion_matrix(cm, files[i], k)

acuracia_file = open((Pds.PATH + "/K" + str(k) + "/acuracia.txt"), 'w')
for i in range(len(acuracia)):
    acuracia_file.write(str(acuracia[i]) + '\n')
acuracia_file.close()
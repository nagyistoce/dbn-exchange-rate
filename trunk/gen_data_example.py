import cPickle
import numpy as np



train_set_x = np.ndarray((60,3), dtype = 'float32')
train_set_y = np.ndarray((60,1), dtype = 'int64')
train_set_x[0] = [20,0,0]
train_set_x[1] = [20,2,1]
train_set_x[2] = [29,1,1]
train_set_x[3] = [21,0,0]
train_set_x[4] = [16,2,2]
train_set_x[5] = [23,0,1]
train_set_x[6] = [18,1,0]
train_set_x[7] = [11,1,0]
train_set_x[8] = [30,1,0]
train_set_x[9] = [25,2,0]
train_set_x[10] = [21,0,1]
train_set_x[11] = [19,1,0]
train_set_x[12] = [18,2,1]
train_set_x[13] = [24,1,0]
train_set_x[14] = [18,1,0]
train_set_x[15] = [11,1,0]
train_set_x[16] = [22,0,0]
train_set_x[17] = [29,1,0]
train_set_x[18] = [20,0,0]
train_set_x[19] = [21,1,1]   

for i in range(0,20):
	train_set_y[i] = 0

train_set_x[20] = [14,1,8]
train_set_x[21] = [26,9,9]
train_set_x[22] = [13,7,1]
train_set_x[23] = [29,6,6]
train_set_x[24] = [25,2,6]
train_set_x[25] = [12,6,0]
train_set_x[26] = [29,6,10]
train_set_x[27] = [11,10,6]
train_set_x[28] = [20,3,9]
train_set_x[29] = [11,4,1]
train_set_x[30] = [21,6,6]
train_set_x[31] = [12,1,5]
train_set_x[32] = [23,1,4]
train_set_x[33] = [23,7,5]
train_set_x[34] = [23,8,9]
train_set_x[35] = [24,5,1]
train_set_x[36] = [28,4,0]
train_set_x[37] = [18,0,9]
train_set_x[38] = [29,6,9]
train_set_x[39] = [22,5,1]
for j in range(20,40):
	train_set_y[j] = 1

train_set_x[40] = [2,0,2]
train_set_x[41] = [1,3,2]
train_set_x[42] = [1,9,5]
train_set_x[43] = [6,6,9]
train_set_x[44] = [3,6,4]
train_set_x[45] = [7,1,0]
train_set_x[46] = [9,2,0]
train_set_x[47] = [9,1,1]
train_set_x[48] = [2,7,10]
train_set_x[49] = [5,9,1]
train_set_x[50] = [9,7,5]
train_set_x[51] = [10,3,2]
train_set_x[52] = [2,0,8]
train_set_x[53] = [2,9,9]
train_set_x[54] = [7,6,7]
train_set_x[55] = [2,6,9]
train_set_x[56] = [6,3,2]
train_set_x[57] = [3,1,9]
train_set_x[58] = [7,9,1]
train_set_x[59] = [7,7,4]

for k in range(40,60):
	train_set_y[k] = 2

tuple_train_set = ((train_set_x),(train_set_y))
type(tuple_train_set)
data_file = open('input_data.pkl','wb')
cPickle.dump(tuple_train_set,data_file,-1)

 

valid_set_x = np.ndarray((60,3), dtype = 'float32')   
valid_set_y = np.ndarray((60,1), dtype = 'int64')
valid_set_x[0] = [20,1,1]
valid_set_x[1] = [21,0,1]
valid_set_x[2] = [23,1,1]
valid_set_x[3] = [25,1,1]
valid_set_x[4] = [18,2,2]
valid_set_x[5] = [29,1,1]
valid_set_x[6] = [23,0,2]
valid_set_x[7] = [17,0,1]
valid_set_x[8] = [22,2,2]
valid_set_x[9] = [11,1,0]
valid_set_x[10] = [28,1,2]
valid_set_x[11] = [25,2,1]
valid_set_x[12] = [19,0,1]
valid_set_x[13] = [24,0,2]
valid_set_x[14] = [18,1,0]
valid_set_x[15] = [19,1,1]
valid_set_x[16] = [29,1,0]
valid_set_x[17] = [19,2,1]
valid_set_x[18] = [28,2,0]
valid_set_x[19] = [14,1,1]   

for l in range(0,20):
	valid_set_y[l] = 0

valid_set_x[20] = [15,1,8]
valid_set_x[21] = [25,8,8]
valid_set_x[22] = [15,9,2]
valid_set_x[23] = [26,6,6]
valid_set_x[24] = [24,2,6]
valid_set_x[25] = [15,6,0]
valid_set_x[26] = [26,7,10]
valid_set_x[27] = [13,10,6]
valid_set_x[28] = [22,5,9]
valid_set_x[29] = [13,6,1]
valid_set_x[30] = [25,5,6]
valid_set_x[31] = [13,2,5]
valid_set_x[32] = [23,1,3]
valid_set_x[33] = [23,7,5]
valid_set_x[34] = [23,8,8]
valid_set_x[35] = [25,4,1]
valid_set_x[36] = [28,4,1]
valid_set_x[37] = [18,1,9]
valid_set_x[38] = [27,6,8]
valid_set_x[39] = [23,4,1]

for m in range(20,40):
	valid_set_y[m] = 1

valid_set_x[40] = [1,0,2]
valid_set_x[41] = [2,3,2]
valid_set_x[42] = [1,9,5]
valid_set_x[43] = [5,5,9]
valid_set_x[44] = [4,6,4]
valid_set_x[45] = [8,2,0]
valid_set_x[46] = [8,2,0]
valid_set_x[47] = [9,1,1]
valid_set_x[48] = [2,7,10]
valid_set_x[49] = [4,8,1]
valid_set_x[50] = [9,7,5]
valid_set_x[51] = [10,3,2]
valid_set_x[52] = [2,1,8]
valid_set_x[53] = [3,9,9]
valid_set_x[54] = [8,5,7]
valid_set_x[55] = [2,6,9]
valid_set_x[56] = [7,3,2]
valid_set_x[57] = [3,2,9]
valid_set_x[58] = [8,9,1]
valid_set_x[59] = [9,8,4]
for n in range(40,60):
	valid_set_y[n] = 2


tuple_valid_set = ((valid_set_x),(valid_set_y))
cPickle.dump(tuple_valid_set,data_file,-1)




test_set_x = np.ndarray((60,3), dtype = 'float32')
test_set_y = np.ndarray((60,1), dtype = 'int64')
test_set_x[0] = [21,0,1]
test_set_x[1] = [21,1,1]
test_set_x[2] = [28,2,1]
test_set_x[3] = [23,1,2]
test_set_x[4] = [18,0,2]
test_set_x[5] = [26,1,1]
test_set_x[6] = [17,1,0]
test_set_x[7] = [14,0,0]
test_set_x[8] = [29,1,0]
test_set_x[9] = [27,2,0]
test_set_x[10] = [21,1,1]
test_set_x[11] = [19,0,2]
test_set_x[12] = [16,2,1]
test_set_x[13] = [24,1,0]
test_set_x[14] = [19,0,1]
test_set_x[15] = [11,2,0]
test_set_x[16] = [22,1,1]
test_set_x[17] = [29,1,0]
test_set_x[18] = [22,2,0]
test_set_x[19] = [21,0,0]   
for o in range(0,20):
	test_set_y[o] = 0

test_set_x[20] = [15,2,9]
test_set_x[21] = [25,9,8]
test_set_x[22] = [12,8,1]
test_set_x[23] = [28,6,6]
test_set_x[24] = [28,3,5]
test_set_x[25] = [13,6,0]
test_set_x[26] = [29,6,10]
test_set_x[27] = [11,10,6]
test_set_x[28] = [21,3,9]
test_set_x[29] = [11,5,2]
test_set_x[30] = [21,6,6]
test_set_x[31] = [15,1,5]
test_set_x[32] = [22,2,5]
test_set_x[33] = [23,7,5]
test_set_x[34] = [23,8,9]
test_set_x[35] = [25,5,2]
test_set_x[36] = [28,4,3]
test_set_x[37] = [19,1,9]
test_set_x[38] = [28,5,7]
test_set_x[39] = [23,4,1]

for p in range(20,40):
	test_set_y[p] = 1

test_set_x[40] = [2,0,3]
test_set_x[41] = [3,4,2]
test_set_x[42] = [1,8,6]
test_set_x[43] = [5,6,9]
test_set_x[44] = [3,5,4]
test_set_x[45] = [7,1,2]
test_set_x[46] = [9,2,1]
test_set_x[47] = [8,2,1]
test_set_x[48] = [2,8,10]
test_set_x[49] = [8,9,1]
test_set_x[50] = [9,7,5]
test_set_x[51] = [10,3,2]
test_set_x[52] = [3,1,9]
test_set_x[53] = [2,9,9]
test_set_x[54] = [8,6,8]
test_set_x[55] = [3,5,9]
test_set_x[56] = [8,3,2]
test_set_x[57] = [4,2,8]
test_set_x[58] = [7,9,1]
test_set_x[59] = [9,8,5]

for q in range(40,60):
	test_set_y[q] = 2

tuple_test_set = ((test_set_x),(test_set_y))
cPickle.dump(tuple_test_set,data_file,-1)
data_file.close()



read_file = open('input_data.pkl','rb')
data1 = cPickle.load(read_file)
data2 = cPickle.load(read_file)
data3 = cPickle.load(read_file)
print data1
print data2
print data3
print type(data1)
print type(data2)
print type(data3)


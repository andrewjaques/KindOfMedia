import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
     32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
     61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
     90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114,
     115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137,
     138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160,
     161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183,
     184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206,
     207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229,
     230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252,
     253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
     276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298,
     299, 300]
s = [39.898377, 38.41193, 38.579061, 38.940253, 38.563966, 39.395165, 39.431984, 39.388321, 39.480425, 39.478229,
     39.458655, 40.71104, 40.711269, 40.709249, 41.103051, 41.091177, 41.083266, 41.174163, 41.181522, 41.157259,
     41.199376, 41.199312, 41.185283, 41.923802, 41.923553, 41.919996, 42.634913, 42.638312, 42.636022, 42.650923,
     42.64707, 30.140038, 37.497692, 37.03016, 35.587156, 37.236602, 37.236602, 37.206124, 37.67054, 37.810215,
     37.639248, 38.438658, 38.542629, 38.407533, 38.717923, 38.76099, 38.68479, 39.229915, 39.253961, 39.213938,
     39.689988, 40.824787, 39.672349, 39.731935, 40.582074, 39.715622, 39.942359, 39.94405, 39.939194, 41.148294,
     41.148356, 41.145746, 41.272084, 41.292642, 41.249757, 41.302213, 41.301877, 41.288791, 42.029143, 42.028259,
     42.023903, 42.740423, 42.74024, 42.737988, 42.847861, 42.851145, 42.846026, 42.848674, 42.844406, 30.353499,
     37.80694, 37.258556, 36.051674, 37.303236, 37.310591, 37.259251, 37.943934, 38.039213, 37.920914, 38.84216,
     38.776663, 38.727934, 39.631209, 39.681106, 39.280652, 39.568982, 39.567452, 39.529719, 39.650471, 39.718842,
     39.660515, 40.753305, 40.73389, 40.73664, 40.894306, 40.894442, 40.881593, 41.258287, 41.297406, 41.232946,
     41.335758, 41.334595, 41.307231, 41.351016, 41.350158, 41.338579, 41.982277, 41.982011, 41.977363, 42.762193,
     42.761988, 42.755107, 42.756854, 42.760254, 42.758882, 42.759882, 42.756678, 30.191126, 37.532242, 37.048636,
     35.653089, 37.252734, 37.263123, 37.225248, 37.889258, 37.999494, 37.880374, 38.694013, 38.835027, 38.687031,
     39.560111, 39.569017, 39.556879, 39.639156, 39.703626, 39.62168, 40.532826, 40.840992, 40.531143, 41.180655,
     40.651969, 40.746585, 40.735941, 40.853061, 40.73946, 40.971956, 40.988755, 40.952153, 41.336238, 41.347158,
     41.337827, 41.431302, 41.429664, 41.407444, 41.514288, 41.433808, 41.425384, 41.965804, 41.966228, 41.961698,
     42.042178, 42.022806, 42.017701, 42.050768, 42.027615, 30.299858, 35.128619, 36.293265, 34.717998, 37.082668,
     37.294496, 36.294457, 37.332569, 37.341486, 37.298061, 37.908038, 37.920102, 37.876469, 38.924913, 38.47837,
     38.466281, 39.361578, 39.373613, 39.358701, 39.516139, 39.514651, 39.495887, 40.747, 40.748366, 40.749634,
     41.10142, 41.162479, 41.098725, 41.220459, 41.207588, 41.177037, 41.001914, 41.189967, 41.159841, 41.348831,
     41.282665, 41.320385, 41.365722, 41.393451, 41.34234, 41.487326, 41.487744, 41.453361, 41.522488, 41.526529,
     41.505848, 41.53574, 41.534912, 30.299105, 36.29311, 36.873866, 34.716905, 37.127344, 37.130995, 37.128224,
     37.557814, 37.668926, 37.417624, 38.643961, 38.656786, 38.647755, 38.731245, 38.730846, 38.714496, 39.596939,
     39.6079, 39.593658, 39.75093, 39.749754, 39.731487, 40.936673, 40.934597, 40.939461, 41.345202, 41.345321,
     41.335434, 41.389143, 41.394542, 41.378359, 42.075754, 42.077331, 42.071593, 42.790967, 42.788879, 42.783864,
     42.853707, 42.853758, 42.660293, 42.66148, 42.650241, 42.860641, 42.63602, 42.890559, 42.871939, 42.894401,
     42.887476, 30.292455, 36.271183, 37.385141, 34.702535, 37.125016, 37.172902, 37.122229, 37.633064, 37.881628,
     37.622294, 38.674195, 38.690305, 38.673381, 38.851729, 39.226225, 38.837077, 39.684221, 39.684284, 39.678153,
     39.763165, 39.987148, 39.746141, 40.671996, 40.672766, 40.67081, 41.306664, 41.306458, 41.298844, 41.383738]

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='Frame number', ylabel='PSNRY',
       title='pqCapture - Frame by Frame PSNRY')
ax.grid()

fig.savefig("test.png")
plt.show()
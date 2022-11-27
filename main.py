'''
Author: SimonCK666 SimonYang223@163.com
Date: 2022-11-27 10:33:03
LastEditors: SimonCK666 SimonYang223@163.com
LastEditTime: 2022-11-27 11:20:15
FilePath: /DMDK1001_Group_Project/main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import os
import numpy as np
import cv2
from config import config_parser

'''
    load setup
'''
parser = config_parser()
args = parser.parse_args()

'''
    get base info
'''
# input image path
img_path = args.img
# number of clusters
K = args.clustersNum

# output folder, if the res forlder does not exist, create one
output_dir = 'res'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
img_name = str(img_path).split('/')[1]
res_name = 'res_' + 'K' + str(K) + "_" + img_name
res_path = output_dir + '/' + res_name

'''
    load input image
'''
img = cv2.imread(img_path)
print('Original image shape is: ' + str(img.shape))
Z = img.reshape((-1,3))
print('Reshape original image as: ' + str(Z.shape))
print("===")

# convert to np.float32
Z = np.float32(Z)

'''
    init K-means and using K-means
'''
# define criteria, number of clusters(K) and apply kmeans()
'''
K-means Parameters:

1. samples : It should be of np.float32 data type, and each feature should be put in a single column.

2. nclusters(K) : Number of clusters required at end

3. criteria : It is the iteration termination criteria. When this criteria is satisfied, algorithm iteration stops. Actually, it should be a tuple of 3 parameters. They are ( type, max_iter, epsilon ):
    3.a - type of termination criteria : It has 3 flags as below:
            cv2.TERM_CRITERIA_EPS - stop the algorithm iteration if specified accuracy, epsilon, is reached. 
            cv2.TERM_CRITERIA_MAX_ITER - stop the algorithm after the specified number of iterations, max_iter. 
            cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER - stop the iteration when any of the above condition is met.
    3.b - max_iter - An integer specifying maximum number of iterations.
    3.c - epsilon - Required accuracy

4. attempts : Flag to specify the number of times the algorithm is executed using different initial labellings. The algorithm returns the labels that yield the best compactness. This compactness is returned as output.

5. flags : This flag is used to specify how initial centers are taken. Normally two flags are used for this : cv2.KMEANS_PP_CENTERS and cv2.KMEANS_RANDOM_CENTERS.
'''
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
print("Starting K-Means...")
ret, label, center=cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
print("K-Means DONE!!...")
print("===")


'''
    get the result image
'''
# Now convert back into uint8, and make original image
center = np.uint8(center)
print("The center of each clusters are: ")
print(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

# write result image
cv2.imwrite(res_path, res2)
print("The result image is written as " + res_path)


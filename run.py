'''
Author: SimonCK666 SimonYang223@163.com
Date: 2022-11-27 17:09:31
LastEditors: SimonCK666 SimonYang223@163.com
LastEditTime: 2022-11-28 20:57:41
FilePath: /DMDK1001_Group_Project/test2.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import numpy as np
import numpy as np
from matplotlib import pyplot as plt
import PIL.Image as image
import cv2
from model import Kmeans
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

'''
    load input image
'''
img = cv2.imread(img_path, 0)

print('Original image shape is: ' + str(img.shape))
Z = img.reshape((-1,1))
print('Reshape original image as: ' + str(Z.shape))
print("===")

'''
    convert to np.float32
'''
Z = np.float32(Z)

'''
    Using Kmeans
'''
labels = Kmeans(K, Z)
print("Labels shape is: " + str(labels.shape))

'''
    reshape as final result image
'''
dst = labels.reshape((img.shape[0], img.shape[1]))
print("Result shape is: " + str(dst.shape))

'''
    show final result
'''
res_title = 'Kmeans Result' + '_k' + str(K)
titles = [u'Original Image', res_title]
images = [img, dst]
for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray'), 
    plt.title(titles[i])  
    plt.xticks([]),plt.yticks([])
    plt.show()
    
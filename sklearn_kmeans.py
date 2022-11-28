'''
Author: SimonCK666 SimonYang223@163.com
Date: 2022-11-27 12:23:56
LastEditors: SimonCK666 SimonYang223@163.com
LastEditTime: 2022-11-28 20:45:53
FilePath: /DMDK1001_Group_Project/test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from sklearn.cluster import KMeans
import PIL.Image as image
from PIL import ImageFilter
import numpy as np

img = image.open('img/a.jpeg')
row,col = img.size

img = img.convert('RGB') # 转RGB 否则会出现int不可以迭代的错误
print(row,col)
data = []

for x in range(row):
        for y in range(col):
            r,g,b = img.getpixel((x,y))
            data.append([r/256.0,g/256.0,b/256.0])

Data = np.mat(data)

label = KMeans(n_clusters=3).fit_predict(Data)
# (106800,)
print(label.shape)
label = label.reshape([row,col])
# (400, 267)
print(label.shape)
pic_new = image.new("L", (row, col))
for i in range(row):
    for j in range(col):
        pic_new.putpixel((i,j), int(256/(label[i][j]+1)))
        
pic_new.save("sklearn_res.jpg", "JPEG")

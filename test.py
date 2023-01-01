import os
import paddle
import random
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import paddle.nn.functional as F
import os
import random
import numpy as np
x_train = np.zeros((37459, 3, 224, 224))
class_dict = {}

class_id = 0 #一开始狗狗的编号是从0开始,也就是说狗狗是从第0类开始
path=r"D:\dir_train"
file_list=os.listdir(path)
file_list.sort(key=lambda x: int(x[0:4]))
for img_file in file_list:
    cur_path=os.path.join(path,img_file)
    if os.path.isdir(cur_path):
        imgs=os.listdir(cur_path)
        for img in imgs:
            if 'jpg' in img:
                dog_id = img_file
                if dog_id not in class_dict:
                    class_dict[dog_id]=class_id
                    class_id+=1
fege=[] #将改变了的图片提取出来用于val
other_imgs=[] #用于test的划分
total=[]
total_end=[]
for img_file in file_list:
    cur_path=os.path.join(path,img_file)
    if os.path.isdir(cur_path):
        imgs=os.listdir(cur_path)
        for img in imgs:
            if 'jpg' in img:
                dog_id = img_file
                last_path =cur_path+'/'+img
                line = '%s %s\n' % (last_path, class_dict[dog_id])
                total.append(line)
                fege=img.split('.')
                if(fege[0][-1]=='0'):
                    other_imgs.append(line)

print('all',len(total))
# random.seed(0)#保证每次产生相同的随机数
# random.shuffle(other_imgs)#打乱名称次序
length=len(other_imgs)
test= other_imgs[:int(length*0.06)]
print('test',len(test))
for index in total:
    if index not in test:
        total_end.append(index)
train = total_end
print('train',len(total_end))
with open(r'C:\Users\User\test.txt', 'w', encoding='UTF-8') as f:
    for line in train:
        f.write(line)
    
with open(r'C:\Users\User\test.txt', 'w', encoding='UTF-8') as f:
    for line in test:
        f.write(line)

import os
import cv2
import numpy as np
from paddle.io import Dataset
class MyDataset(Dataset):
    def __init__(self,label_path, transform=None):#初始化数据集，将样本和标签映射到列表中
        super(MyDataset, self).__init__()
        self.data_list = []
        with open(label_path,encoding='UTF-8') as f:
            for line in f.readlines():
                image_path, label = line.strip().split(' ')
                self.data_list.append([image_path, label])
        self.transform = transform
    def __getitem__(self, index):#定义指定index时如何获取数据,并返回单条数据（样本数据、对应的标签）
        global x_train,y_train
        # 根据索引，从列表中取出一个图像
        image_path, label = self.data_list[index]
        # 读取图片(以图片原本的形式加载)
        image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        # 飞桨训练时内部数据格式默认为float32，将图像数据格式转换为 float32
        image = image.astype('float32')
        image = image /255.
        if self.transform is not None:
            image = self.transform(image)
        label = np.array([int(label)])
        # 返回图像和对应标签
        return image, label
    def __len__(self):#返回数据集的样本总数
        return len(self.data_list)
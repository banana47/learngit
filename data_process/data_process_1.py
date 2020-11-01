"""
BasicDataloader对数据处理的基本步骤：
1.创建一个类，类里面需要包含torch的一个类:Dataset
e.g class Basicdataloader(Dataset):
2.然后需要进行初始化，继承
e.g:
    class Basicdataloader(Dataset):
        def __init(self, ,,,):
            #继承
            super(Basicdataloader, self).__init__()
            接下来是一些必要的设置
３．该部分返回数据的长度，是必须要的
    def __len__(self):
        return len(self.data)
4.这一部分是对数据的处理
    def process(self, data, label):
        "各种处理, 然后返回处理过的数据"
        return data, label

５．这一步的输入是数据(image, label), 输出是经过处理后，最终需要输出的数据
    也有可能输入的是数据的路径，需要先读从路径中读取数据，再处理
def __getitem__(self, index):
    "这部分也有可能输入的是数据的路径，需要先读取数据数据，然后在进行处理"
    img, label = self.data[index], self.label[index]
    img, label = self.process(img, label)
    "经过一些处理, 返回最终的数据"
    return img, label
"""
import os
import random
import numpy as np
# import cv2
from skimage.io import imread
from skimage.transform import resize
# import paddle.fluid as fluid
import torch.utils.data.dataloader
from torch.utils.data import Dataset

class Transform(object):
    def __init__(self, size):
        self.size = size
    def __call__(self, image, label):
        image =resize(image, (self.size, self.size))
        label = resize(label, (self.size, self.size))
        return image, label

class BasicDataloader(Dataset):
    def __init__(self,
                 image_folder,
                 image_list_file,
                 transform=None,
                 shuffle=True):
        super(BasicDataloader, self).__init__()
        self.image_foder = image_folder
        self.image_list_file = image_list_file
        self.transform = transform
        self.shuffle = shuffle

        self.data_list = self.read_list()
        self.data = []
        self.label = []

    def read_list(self):
        data_list = list()
        with open(self.image_list_file) as infile:
            for line in infile:
                data_path = os.path.join(self.image_foder, line.split()[0])
                label_path = os.path.join(self.image_foder, line.split()[1])
                data_list.append((data_path, label_path))
        return data_list

    def process(self, image, label):
        h, w, _ = image.shape
        gt_h, gt_w = label.shape

        assert h == gt_h
        assert w ==gt_w

        if self.transform is not None:
            data, label = self.transform(image, label)

        label = label[:, :, np.newaxis]

        return data, label

    def __len__(self):
        return len(self.data_list)

    def __getitem__(self, index):
        image_path = self.data_list[index][0]
        label_path = self.data_list[index][1]

        image = imread(image_path)
        label = imread(label_path)

        image, label = self.process(image, label)

	# 将数据[H, W, c] -> [C,h, w] 注意，此时数据为np.array()，这两行代码也可以放置到preprocess
	image = image.transpose((2, 0, 1))
        label = label.transpose((2, 0, 1))

        return image, label




# def main():
#     transform = Transform(256)
#     image = BasicDataloader(image_folder="./work/dummy_data",
#                                               image_list_file="./work/dummy_data/list.txt",
#                                               transform=transform,
#                                               shuffle=True)
#     print(image.data)
#
#
# if __name__ == "__main__":
#     main()
transform = Transform(256)
image = BasicDataloader(image_folder="./work/dummy_data",
                                          image_list_file="./work/dummy_data/list.txt",
                                          transform=transform,
                                          shuffle=True)
for idx, (data,label) in enumerate(image):
    print("idx", idx, "data.shape", data.shape, "label.shape", label.shape)

from torch.utils.data import DataLoader
train = DataLoader(dataset=image, batch_size=15, shuffle=True, drop_last=True)
for idx, (data,label) in enumerate(train):
    print("idx", idx, "data.shape", data.shape, "label.shape", label.shape)

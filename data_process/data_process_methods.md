#1.数据处理总体思路：
1.读取数据；
2.获取数据量
3.对数据进行预处理(分别对每队image and its label)
4.返回
5.如果想要对数据得到generator, 则直接将数据放入对应的API中（数据带标签和不带标签，都可以进行处理）

## 1.将训练数据和标签存路径存到一个文件中．例如(".txt"), file.txt
## 2.class dataLoader(object):（如果为torch话，应该改为class dataloader(Dataset)）
	def __init__(seld, image_folder, file_listdir, transform, shuffle):
		super(dataLoader, self).__init__()
		self.image_folder = image_folder
		self.file_listdir = file_listdir
		self.transform = transform
		self.shuffle = shuffle

	# 获得数据的数量
	def __len__(self):
		return len(len(data)) # 返回数据长度

	//对数据进行处理
	def pre_process(self, image, label):
		h, w, c = image.shape
		gt_h, gt_w = label.shape

		assert h == gt_h, "err:size is not match"
		assert w == gt_w, "err:size is not match"
		
		if self.transform:
			image, label = self.transorm(image, label)
		return image, label
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

# 2.搭建模型
## 1.了解模型整体架构（那些部分是并行的，那些部分是顺序执行的）
## 2.把模型整体架构顺序写出来，如果遇到需要实现的模块，先将该模块的名字以及输入输出确定，完成整体流程；
## 3.实现各部分的子模块；
## 4.设置一些与真实数据一样的类型，将其输入网络，如果网络正常运行，则说明搭建的网络没有问题．

# 3.设置损失函数
## 1.首先需要确定使用那类损失函数，如果有API，就直接调用；如果没有，就自己写，其输入为:pred和gt_label, 输出为损失；
## 2.如果是自己写的损失函数，则需要将一些数据设置成相似的类型，然后进行测试；

# 4.设置训练
# 1.train_流程
1.预测:pred = model(image)
2.计算损失:loss = criterion(pred, label)
3.反向传播:loss.backward()
4.梯度优化:optimizer.minimize(loss)
5.梯度清零:optimizer.clear_gradients()
## 2.有多个epoch话，先将整体epoch循环写出来，每次执行一个epoch;
## 3.定义一个epoch, 需要设置的有：
	1.learning_rate:lr
	2.optimizer:优化器
	3.model(相当于一个函数)
	4.dataset:数据

#5.整体流程(以一张图片为例)
1.输入一张图片
2.将图片进行transform(进行正则化前需要先除以255, (x-mean)/std)
3.将图片送入神经网络, 输出为NCHW(1, 59, 1024, 768)
4.进行softmax, 再进行argmax(), 选择概率最大的那个维度, 得到（1, argmax_idx, h, w）
5.再进行squeeze(), 去掉一维度的的维度



		

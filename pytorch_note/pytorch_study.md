# 1.基本配置
## 1.导入包和版本查询
import torch
import torch.nn as nn
import torchvision
print(torch.__version__)
print(torch.version.cuda)
print(torch.backends.cudnn.version())
print(torch.cuda.get_device_name(0))

##2.可复现性
在程序开始的时候固定torch的随机种子，同时也把numpy的随机种子固定。

np.random.seed(0)
torch.manual_seed(0)
torch.cuda.manual_seed_all(0)

torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False

## 3.显卡设置
### 1.如果只需要一张显卡

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

### 2.如果需要指定多张显卡，比如0，1号显卡
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0,1'

也可以在命令行运行代码时设置显卡：
CUDA_VISIBLE_DEVICES=0,1 python train.py

清除显存
torch.cuda.empty_cache()

也可以使用在命令行重置GPU的指令
nvidia-smi --gpu-reset -i [gpu_id]

# pytorch保存和加载模型
pytorch保存和加载模型后缀：.pt和.pth
1.保存整个模型:torch.save(model, "save.pt")
2.只保存训练好的权重:torch.save(model.state_dict(), "save.pt")
3.加载模型:pretrained_dict = torch.load("save.pt")
4.只加载模型参数:model.load_state_dict(torch.load("save.pt"))
5.加载某一层的训练参数:conv1_weight_state = torch.load("save.pt")["conv1.weight"]

# torch对图像padding
torch.nn.functional.pad(input, pad, mode=‘constant’, value=0)
# 引入模型
from torchvision.models import vgg16
# 将np.array()转换为Tensor
from torch.autograd import Variable
# 双线性插值
nn.functional.interpolate(x, size=(h, w))
#　自适应卷积
m = nn.AdaptiveMaxPool2d(size=(size_h, size_w))
x = m(inputs)


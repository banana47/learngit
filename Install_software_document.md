# ubuntu sodtware install and problem solutions

# nvidia_cuda_cudnn install link
https://blog.csdn.net/BigData_Mining/article/details/99670642#commentBox

# 双显卡笔记本安装双系统ubuntu开机、分辨率、卡logo、黑屏的解决方法
https://blog.csdn.net/n66040927/article/details/79019891

# cuda 历史版本
https://developer.nvidia.com/cuda-toolkit-archive

# ubuntu搜狗拼音安装教程
https://blog.csdn.net/lupengCSDN/article/details/80279177

# pycharm 安装教程
https://blog.csdn.net/qq_15192373/article/details/81091278

# conda install 慢
1.sudo gedit ~/.condarc
  清华大学开源软件镜像站:https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/
  link:https://blog.csdn.net/watermelon1123/article/details/88122020

# git慢
link:https://www.jianshu.com/p/3f6477049ece
## 思路：
git clone特别慢是因为github.global.ssl.fastly.net域名被限制了。只要找到这个域名对应的ip地址，然后在hosts文件中加上ip–>域名的映射，刷新DNS缓存便可
## 方法：
1.在网站 https://www.ipaddress.com/ 分别搜索：
github.global.ssl.fastly.net
github.com

2.打开hosts文件
Windows上的hosts文件路径在C:\Windows\System32\drivers\etc\hosts
Linux的hosts文件路径在：sudo vim /etc/hosts

3.在hosts文件末尾添加两行(对应上面查到的ip)
151.101.185.194 github.global-ssl.fastly.net
192.30.253.112 github.com

4.保存更新DNS
Winodws系统的做法：打开CMD，输入ipconfig /flushdns
Linux的做法：在终端输入sudo /etc/init.d/networking restart

# 换源
sudo gedit /etc/apt/sources.list
清华源网址：https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/
如果出现异常，可以试下：sudo apt install -f

# 上传github
连接教程：https://www.yiibai.com/git/git_remote.html
1.新建一个目录．　mkdir xxx
2.初始化：git init
3.添加文件：git add file
4.提交到本地：git commit -m "注释"
5．git remote add origin https://github.com/banana47/ubuntu_software_Install.git：(首次创建使用)
6.git push






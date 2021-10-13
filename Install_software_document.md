# ubuntu sodtware install and problem solutions

#tf 和keras对应的关系 
https://docs.floydhub.com/guides/environments/

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
｀｀｀
echo "# CoarseToFineGAN" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/pankSM/CoarseToFineGAN.git
｀｀｀

# 离线安装
## 1.pytorch:https://blog.csdn.net/Suan2014/article/details/80410144
首先，到https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/linux-64/中下载所需的.tar.bz2，如果是环境python，就采用
            conda install --offline -n XXXX..tar.bz2
如果是虚拟环境，就采用
　　　　 conda install --offline -n env_name XXXX..tar.bz2　　　
其中env_name是虚拟环境名称。　

## 2.python包官网连接:https://pypi.org/
##3.将下载后的包解压，解压后进入该包的目录下，执行　python setup.py install;如果下载后的为．whl文件，直接执行 pip install -U file.whl

主要过程：
才开始搜索＂conda离线安装python包＂，不管怎么搜，都没搜索到，这个过程没有仔细想，哪里出问题了，不停的在搜这个，耗费了太长时间；然后在下载好各种包，因为＂.whl＂文件不知道是干嘛用的，又因为conda 对pytorch的安装的直接是对".tar.gz"这种文件直接操作的，所以就没想着解压，一直想着对＂.tar.gz＂文件操作，无意中查到需要解压，然后又对每一个文件解压操作，当一切准备好后，对scikit-image的安装仍然出问题，最后才查阅了＂.whl＂文件的的作用．当下载好后，在服务器上安装，由于忘了进入虚拟环境，一直提示该包不支持这个平台．

### 经验总结：
1.如果一个搜索方式一直没有结果，可以想想应该怎样搜索，不能拿着一个一直搜；
2.当下载某个文件话，遇到不懂的后缀，要先查查，他们是干什么用的，这个不会花费太多时间，但这样做的话，会让效率提高；
3.当下载的话，需要判断是否在指定的虚拟环境中．
4.在這個過程中最大的問題是把＂tensorflow=1.14.0" 錯記成＂tensorflow=1.4.0＂, 結果花了一天一夜時間，還沒正好．

# conda 虚拟环境迁移
1.首先要有一个已经创建好的虚拟环境，以MYvirtual为例；

2.将Ｍyvirtural 移到服务器下/home/smpk/.conda/envs下，在./conda下，有一个envitonment.txt文件，需要将该虚拟环境的路径添加进去；

３．进入Myvirtual虚拟环境下，修改pip路径：https://blog.csdn.net/ganxiwu9686/article/details/98736127?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param

	which pip
	/home/pengwei/.conda/envs/py35/bin/pip

	which python
	/home/pengwei/.conda/envs/py35/bin/python

	vim /home/pengwei/.conda/envs/py35/bin/pip
	把#！后面的改成python的路径就好了












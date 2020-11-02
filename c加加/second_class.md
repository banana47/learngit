# 1.变量
## 1.内存如何存放数据
### 1.**变量**是计算机中一块特定的**内存空间**
1.由一个或多个连续的字节组成. 8 bit = 1 byte
2.变量的命名:通过变量名可以简单快速的找到内存中的数据
	1.首字母只能是"_" 字母
	2.其他可以是字母数字和下划线
	3.不可以使用关键字

# 2.数据类型
## 1.数值
### 1.整型
	1.int(32bit,既4个字节)和long int　位数一样
	2.short int(16bit)
	3.long 
	4.long long
	5.char
	6.bool(0或者1)
	
### 2.浮点型
	1.float(32位):6~7为有效数字
	2.double(64bit, 8个字节):
	3.long double
## 2.非数值
	string
## 3．其他数据类型：size_t类型，　枚举类型,自定义类型，指针类型，空类型等；
**定义别名:** typedef string wode_string;表示wode_string 为string

# 3.命令方式
建议两种:
1.wife_name
2.wifeName

**Note:**如果要使用 printf(), 需要在头文件导入<cstdio>

## 4.控制cout显示的精度
	#include<iomanip>
	1.控制浮点型以小数的方式显示
	cout << fixed;
	2. 控制显示的小数的位数；
	cout << setprecision(2);

# 4.sizeof()　获得数据的长度






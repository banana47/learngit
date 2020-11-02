# 1
1.#include<iostream>
iostream: 包含了有关输入输出语句的函数．(input and output)．为了后面使用cin 和cout．
	1.cout相当于将一个字符串插入到了输出流中；
	2.cin相当于将一个字符串插入到了输入流中；
2.using namespace std; 
	cout << "a" << endl;
如果没有命名空间：std::cout <<  "a" << endl;
	
3.endl(相当于end line)，是控制符，相当于("\n")．两者区别：
	"\n":只换行
	"endl":1.换行；2.fflush(stdin)清除缓存


# 命名空间 std
1.定义:一个由程序设计者命名的内存区域．其作用就是建立一些相互分割的作用域，把一些全局实体分分割开，以免产生命名混淆．
2.用法：
	namespace ns1
	{
	int a;
	int b;
	}
	注意:和class的定义不同，后面没有";"
	
	用法：ns1::a. 这种用法被称为"命名空间限定"
	"ns1::a":被称之为限定名

3.使用命名空间成员的方法
	命名空间名::命名空间成员名
	1.使用命名空间别名
		namespace Television
		{...}
		调用:namespace TV = Television
	2.使用　using命名空间成员名
		using ns1::student
		student stud1()
	3.使用using namespace 命名空间名
		using namespace std;	

# 2.c++编程规范

#3.编译执行过程
## 1.编译（预处理 -> 编译　->目标文件）
形成目标代码文件，　目标代码是编译器的输出结果，常见扩展名：".o"或者".obj"
## 2．连接
1.将目标代码跟c++函数库相连接，并将源程序用的库代码与目标代码合并．
2.形成最终可执行的二进制机器代码(可执行程序)．
## 3.执行
在待定的机器环境下运行c++应用程序．

###例子(以HelloWorld.cpp为例子)
1.预处理: g++ -o HelloWorld.ii -E HelloWorld.cpp
2.编译：g++ -o HelloWorld.s -S HelloWold.ii
3.目标文件: g++ -o HelloWorld.o -e HellloWorld.s
4.link: g++ -o HelloWorld.exe HelloWorld.o	

### "\t"代表"tab"键.

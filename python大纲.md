是晚风，是落日， 是心动，是无可替代，是你 ，始于颜值，陷于才华， 忠于人品，痴于肉体， 迷于声音，最后折扣于物质，败于现实..... 当新鲜感褪去， 真正的爱情才会浮出水面， 如果连专一都做不到， 那就永远逃不出新鲜感的死循环。 但只要爱着彼此，我就沉沦在那入水一样的温柔里..... 候鸟南飞，万河归海，不远千里. 你的过去我没有参与，你的未来我陪你！ 地球之所以是圆的，就是为了让迷路的人重逢. 爱是天时地利的迷信，原来你也在这里！ 我会用尽全力去爱你，接受你的坏脾气. 容忍的小任性，分享你的一切. 无论是开心，还是难过....

# 第一章

###  一、print 函数

```python
#输出到文件中
fp=open('D:/text.txt','a+')
print('helloworld',file=fp)
fp.close()
#所制定的内存盘符要存在
#file=fp
#a+如果文件不存在就创建，如果文件存在就进行追加内容，运行一次加一次内容
#如果不进行换行
print('hello','world','python')    
```

### 二、转义字符

```python

print('hello\nworld')
#\  +  转义功能的首字母n  newline换行
print ('hello\tworld')
print('helloooo\tworld')
#\t占用四个字符 四个字符为一个制表位，小于四个就用补齐
print('hellooo\tworld')   
print('hello\rworld')#\r表示回车
print('hello\bworld')#\b表示退格
print('http:\\\\www.baidu.com')#\表示转义一个\转义一个字符
print('老师说：‘大家好’')
#原字符  不希望字符串中的字符发生转义 在字符串前面加上一个r或R
print(r'\n是换行字符')
#注意事项  字符串最后一个符号不能是一个\  可以使两个
```

### 三、信息轰炸qq

```python
from pynput.keyboard import Key,Controller
import time
keyboard=Controller()
messages=input("请输入你要轰炸的信息：")
times=eval(input("请输入你要轰炸的次数："))
print("数据已被后台接受，请将光标移动至会话框")
time.sleep(2)
for i in range(3):
    print("距离信息轰炸还需要%d秒"%(3-i))
    time.sleep(1)
for i in range(times):
    keyboard.type(messages)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.1)
print("信息轰炸已经顺利完成，已退出！")
#信息轰炸
```

# 第二章

### 四、二进制编码

```python
#二进制与ascii码
#GB18030 中国的编码
#unicode 全世界几乎所有字符的字符编码
print(chr(0b100111001011000))
print(ord('乘'))
```

### 五、标识符与保留字

有些单词被赋予特殊意义，在给任何对象起名字时都不可以用

```python
inport keyword
print(keyword.kwlist)
#kwlist  关键字（保留字）
```

规则：

 1、字母，数字，下划线

2、不能以字母开头

3、不能是保留字

4、严格区分大小写

### 六、 变量的命名和使用

三要素：标识、  类型、   值

```python
name='玛利亚'
print(name)
print('地址',id(name))
print('类型',type(name))
print('值',name)


```

### 七、变量的多次赋值

```python
name='玛利亚'
name='楚留香'
print(name)
#輸出“楚留香”
```

### 八、数据类型

```python
#整数类型

#二进制  0b开头
#十六进制  0x开头
#八进制  0o开头
#十进制  默认类型
print('十进制',123)
print('二进制',0b101001)
print('八进制',0o1654)
print('十六进制',0x12abfc)
#浮点类型
n1 = 1.1
n2 = 2.2
print(n1 + n2)  # 3.3000000000000003

from decimal import Decimal
print(Decimal('1.1') + Decimal('2.2'))  # 3.3oat
#bool类型
#转化为整数  ture  1  false  0
f1 = True
f2 = False
print(f1, type(f1))  # True <class 'bool'>
print(f2, type(f2))  # False <class 'bool'>
print(f1 + 1)
print(f2 + 2)
#字符串类型
s
```

### 九、数据类型转换

```python
#将其他类型转换成字符串类型
print('------将其他转换成字符串类型------')
a1=12
a2=False
a3=12.987
print(type(a1),type(a2),type(a3))
print(str(a1),str(a2),str(a3),type(str(a1)),type(str(a2)),type(str(a3)))

#将其他类型转换成int类型   文字类和小数类无法转换
b1='12'
b2=98.3
b3='98.3'
b4=True
b5='hello'
print(type(b1),type(b2),type(b3),type(b4),type(b5))
print(int(b1))
print(int(b2))
#print(int(b3))
print(int(b4))
#将其他数据类型转换成float类型
print('------将其他类型转换成float类型-------')
c1=23
c2=True
c3='23'
c4='23.4'
c5='hello'
print(type(c1),type(c2),type(c3),type(c4),type(c5))
print(float(c1),type(float(c1)))
print(float(c2),type(float(c2)))
print(float(c3),type(float(c3)))
print(float(c4),type(float(c4)))
#print(float(c5),type(float(c5)))))

```

# 第三章

### 十、input函数的使用

### 十 一、python中的运算符

#### 1、算数运算符

```python
#算数运算符
print(1+2)
print(2-1)
print(1*2)
print(1/2)
print(12//5)#整除运算符
print(11%2)#取余运算符
print(2**2)#幂运算符


#一正一负取整和求余
print(-9%4)#-3
print(9%-4)#-3
print(-9//4)#3
print(9//-4)#-3     余数等于被除数-除数*商

```

#### 2、赋值运算符

```python
   # 链式赋值
a = b = c = 27
print(a, id(a))
print(b, id(b))
print(c, id(c))
# 参数赋值

a = 30
a += 20
print(a)
a -= 20
print(a)
a *= 2
print(a)
a /= 10
print(a)
a //= 2
print(a)
a %= 2
print(a)

# 系列解包赋值
i,j,k=10,20,30
print(i,j,k)
   #交换两个变量的值
i,j=j,i
print(i,j)
```

#### 3、比较运算符

```python
# 比较运算符
a, b = 10, 276
print(a >= b)
print(a <= b)
print(a != b)
print(a == b)
# ==比较的是对象的值
# is比较的是对象的标识
print(a is b)  # 如果值相同，则指向的空间也相同
list1 = [11, 22, 33, 44]
list2 = [11, 22, 33, 44]
print(list1 == list2)
print(list1 is list2)
print(id(list1))
print(id(list2))
print(a is not b)
print(list1 is not list2)
```

#### 4、bool运算符

```python
# bool運算符
#   and   同真为真，否则为假
f, g = 2, 3
print(f == 2 and g == 3)  # True
print(f != 2 and g == 3)  # False
print(f == 2 and g != 3)  # Flase
print(f < 1 and g > 4)  # False

#   or   有真为真，否则为假
print(f == 2 or g == 3)  # True
print(f != 2 or g == 3)  # True
print(f == 2 or g != 3)  # True
print(f < 1 or g > 4)  # False

# 取反运算符   not
f1 = False
f2 = True
print(not f1)
print(not f2)

# in 与 not in   存在与不存在
s1='helloworld'
print('e' in s1)
print('l' not in s1)
```

#### 5、位运算符

```python
# 位运算符
# 按位与   &  二进制数值  同为1取1 否则为0
print(4 & 8)
# 按为或   |  同为0为0 否则为1
print(4 | 8)
#左移运算符  高位溢出 低位补0   <<
print(4<<1)
#右移运算符  低位溢出 高位补0   >>
print(4>>1)
```

### 十二、运算符的优先级

# 第四章

### 十三、程序的组织结构

#### 1、顺序结构

对象的bool值：

```python
     # 对象的bool值

print("bool值为false")
print(bool(0))
print(bool(0.0))
print(bool(''))
print(bool(""))
print(bool([]))  # 空列表
print(bool(None))
print(bool(list()))  # 空列表
print(bool(()))  # 空元组
print(bool(tuple()))  # 空元组
print(bool({}))  # 空字典
print(bool(dict()))  # 空字典
print(bool(set()))  # 空集合
print("其他对象的bool值均为true")
```

#### 2、选择结构

##### （1）单分支结构

```python
money = 1000
    s = int(input('请输入你的取款金额：'))
    if s <= money:
        money = money - s
        print('取款成功，余额为', money)

```

##### （2）、双分支结构

```python
money = 1000
    s = int(input('请输入你的取款金额：'))
    if s <= money:
        money = money - s
        print('取款成功，余额为', money)
    else:
        print('输入的取款金额不对，清重新输入！')
```

##### （3）、多分支结构

```python
 # 输入分数查询等级
score = int(input("请输入你的分数："))
if score < 100 and score >= 90:
    print("A")
elif score < 90 and score >= 80:
    print('B')
elif score < 80 and score >= 70:
    print('C')
elif score < 70 and score >= 60:
    print('D')
elif score < 60 and score >= 0:
    print('E')
else:
    print("请输入正确的分数!")
 # 输入分数查询等级
score = int(input("请输入你的分数："))
if 100> score >= 90:
    print("A")
elif 90 > score >= 80:
    print('B')
elif  80 > score >= 70:
    print('C')
elif  70 > score >= 60:
    print('D')
elif  60 > score >= 0:
    print('E')
else:
    print("请输入正确的分数!")


```

##### （4）、if else的循环嵌套使用

```python
answer = input("你是会员吗？")
money = float(input("请问你所购买的价值是多少？"))
if answer == '是':
    if money >= 200:
        print("折扣后的价钱是：", money * 0.8)
    elif 100 <= money <= 200:
        print("折扣后的金额为:", money * 0.9)
    else:
        print('不打折')
elif answer == '不是':
    if money >= 200:
        print('打折后的价格是：', money * 0.95)
    else:
        print('不打折')
```

##### （5）if  else简化使用

```python
num_a = int(input('请输入一个数'))
num_b = int(input('请再次输入一个数'))
print("条件判断语句")
print(str(num_a) + '大于' + str(num_b)    if num_a >= num_b else     str(num_a) + '小于' + str(num_b))

#pass代码   在还没有想好代码的时候用
if num_b>num_a:
    pass
```

### 十四、range（）函数的使用

优点：不管整数序列有多长，占用内存是相同的，只有当用到range对象时，才回去计算range当中的相关元素。

```python
# range的三种创建方式
r = range(10)
print(r)
print(list(r))  # 用于查看range对象中的数列

r = range(2, 12)
print(r)
print(list(r))

r = range(1, 10, 2)
print(r)
print(list(r))
#判断指定的某个数在整个序列中是否存在
print(10 in r)
print(5 not in r)   
```

### 十五、while循环

if判断一次，条件为True执行一次

while判断N+1次，条件为True执行N次

```python
a = 0
sum = 0  # 初始化和
# 条件判断
while a <= 10:
    # 执行循环体
    sum += a
    # 改变变量
    a += 1

print('sum=', sum)


a = 0
sum = 0  # 初始化和
# 条件判断
while a <= 100:
    # 执行循环体
    if a%2==0:
        sum += a
    # 改变变量
    a += 1

print('sum=', sum)


a = 0
sum = 0  # 初始化和
# 条件判断
while a <= 100:
    # 执行循环体
    if not bool(a%2):
        sum += a
    # 改变变量
    a += 1

print('sum=', sum)
```

### 十六、for in循环

in表示从（字符串，列表中）依次取值（遍历）

for in遍历的对象必须是可迭代对象  

```python
print('使用for循环打印1000以内的水仙花数')
for item in range(100, 1000):
    if (item // 100) ** 3 + (item // 10 % 10) ** 3 + (item % 10) ** 3 == item:
        print(item, end='  'for i in range(10, 34, 2):
    print(i)

for _ in range(12):
    print('你好')
'''你好
你好
你好
你好
你好
你好
你好
你好
你好
你好
你好
你好'''


sum = 0
for item in range(0, 101):
    if item % 2 == 0:
        sum += item
print(sum)

sum = 0
for item in range(0, 101, 2):
    sum += item
print(sum))


```

### 十七、结束循环体的条件语句

##### 1、break 用于结束循环结构，通常与if搭配使用

```python
a = 0
while a < 3:
    password=input('請輸入密碼')
    if password == '203':
        print('密碼正確')
        break
    else:
        print('密碼錯誤，請輸入密碼')
    a+=1


for password in range(3):
    password = input('请输入密码：')
    if password == '203617':
        print('密码正确')
        break
    else:
        print('密码错误，请重新输入!')
```

##### 2、continue:结束当前循环，进行下一次循环

```python
print('学生成绩评价表')

while 1:
    score = int(input('请输入你的分数'))
    if 60 <= score <= 100:
        print('学生成绩合格！')
        continue
    elif 0 <= score < 60:
        print('学生成绩不合格！')
        continue
    elif 0 >= score or score >= 100:
        print('成绩输入错误！')

```

##### 3、else的使用

###### （1）else和for循环搭配使用

```python
for password in range(3):
    password = input('请输入密码：')
    if password == '203617':
        print('密码正确')
        break
    else:
        print('密码错误，请重新输入!')
else:
    print('該卡已凍結，請到銀行服務中心咨詢')
```

###### （2）else和while搭配使用

```python
for password in range(3):
    password = input('请输入密码：')
    if password == '203617':
        print('密码正确')
        break
    else:
        print('密码错误，请重新输入!')
else:
    print('該卡已凍結，請到銀行服務中心咨詢')


a = 0
while a < 3:
    password=input('請輸入密碼')
    if password == '203':
        print('密碼正確')
        break
    else:
        print('密碼錯誤，請輸入密碼')
    a+=1
else:
  print('该卡已经冻结')
```

### 十八、嵌套循环

```python
# 2、用while循环
a = 1
b = 1
while a < 10:
    while b <=a:
        print(b, '*', a, '=', a * b, end='\t')
        b += 1
    print()
    a += 1
    b=1#
```

```python
for i in range(10):
    for j in range(1, 23):
        if not bool(j % 3):
            break
        print(j,end=' ')
    print()
'''
1 2 
1 2 
1 2 
1 2 
1 2 
1 2 
1 2 
1 2 
1 2 
1 2 
'''
for i in range(10):
    for j in range(1, 23):
        if not bool(j % 3):
            continue
        print(j,end=' ')

    print()

'''
1 2 4 5 7 8 10 11 13 14 16 17 19 20 22 
1 2 4 5 7 8 10 11 13 14 16 17 19 20 22 
1 2 4 5 7 8 10 11 13 14 16 17 19 20 22 
1 2 4 5 7 8 10 11 13 14 16 17 19 20 22 
1 2 4 5 7 8 10 11 13 14 16 17 19 20 22 
1 2 4 5 7 8 10 11 13 14 16 17 19 20 22 
1 2 4 5 7 8 10 11 13 14 16 17 19 20 22 
1 2 4 5 7 8 10 11 13 14 16 17 19 20 22 
1 2 4 5 7 8 10 11 13 14 16 17 19 20 22 
1 2 4 5 7 8 10 11 13 14 16 17 19 20 22 

'''
```

# 第五章

### 十九、列表的创建与删除

```python
list1=['nihao','ofcouse',234]
list2=list(['nihao','ofcouse',234])
print(list1,list2)

list1=['nihao','ofcouse',234]
list2=list(['nihao','ofcouse',234])
print(list1[0],list2[-2])                      #nihao ofcouse

#对list3循环赋值

for i in range(1,20):
    list3 = i**3
    print('list3[%d]=%d' % (i, list3))


  # 获取列表的指定元素索引
print(list1.index('nihao'))  # 0
# 当列表中存在相同元素时，只返回第一个元素出现的索引
print(list1.index('nihao', 1, 5))  # 3
# 查找元素

```

#### 1、列表的特点：

1、列表元素按顺序有序排序

2、索引映射唯一的数据

3、列表可以储存重复数据

4、列表可以任意*数据类型混合存储

5、根据需要动态分配内存和收回内存

6、in或not in查询列表元素是否存在

```python
# 所属学校：贵州师范大学
# 开发人员：陶景航
# 开发时间：2023/1/3 17:49
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# step为正数的情况
list2 = list1[1:8:1]  # step默认为1如果没有值，则start和stop默认为开始和结尾
print(list2)
# step为负数的情况
list3 = list1[::-1]#开始和结束默认，step为-1时逆序输出原列表
print(list1)
print(list3) 


'''
[2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
''' 

```

### 二十、列表的增删查改

##### 1、列表元素的添加

```python
# 向末尾添加一个元素
list = [1, 2, 3, 4, 5]
print(list)
list.append(6)
print(list)
#向列表的末尾添加至少一个元素
list2=[7,8,9]
#list.append(list2)    #list整体以元素的形式添加list
#print(list)
list.extend(list2)
print(list)
#向列表中任意位置添加一个元素
list.insert(4,4.5)
print(list)
#向列表任意位置添加多个元素
list3=['ni','hao','a']
list[1:]=list3
print(list)
```

##### 2、列表元素的刪除

```python
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]

for j in range(11):
    if list[j] == 1:
        print('找到元素1的位置在list中的第%d个' % j)

list.remove(1)  # 刪除列表中指定元素，重复元素只删除第一个
print(list)
list.pop(1)
print(list)  # 删除列表指定位置上的元素，没有指定位置删除最后一个元素
list.pop()
print(list)

# 切片操作，至少删除一个元素
new_list = list[1:7]
print(new_list)  # 产生一个新的列表

list[1:3] = []  # 不产生新的列表，用空列表代替指定位置的元素
print(list)

# 清空列表
list.clear()
print(list)

# 删除列表
del list
print(list)

```

##### 3、列表元素的修改

```python
#列表的修改
list[2]=3
print(list)

#切片修改
list[1:3]=[7,8,9]
print(list)
```

##### 4、列表元素的排序

```python
#使用内置函數進行排序  產生一個新的列表，源列表不發生變化
list=[2,5,3,8,5,3,8,0,2]
list1=sorted(list)
print(list)
print(list1)
list2=sorted(list,reverse=True)#使用指定关键字进行排序
print(list2)
list3=sorted(list,reverse=False)
print(list3)
'''
[1, 2, 2, 3, 4, 4, 5, 6, 8]
[8, 6, 5, 4, 4, 3, 2, 2, 1]
[1, 2, 2, 3, 4, 4, 5, 6, 8]
[2, 5, 3, 8, 5, 3, 8, 0, 2]
[0, 2, 2, 3, 3, 5, 5, 8, 8]
[8, 8, 5, 5, 3, 3, 2, 2, 0]
[0, 2, 2, 3, 3, 5, 5, 8, 8]
'''
```

### 二十二、列表推导式

```python
#列表生成式
list4=[i*i for i in range(1,10)]
print(list4)
#[1, 4, 9, 16, 25, 36, 49, 64, 81]

```

# 第六章

### 二十三 、什么是字典

python内置的数据结构，可变序列，字典是一个无序的序列

### 二十四、字典的原理

根据key查找value所在的位置

### 二十五、字典的创建与删除

#### 1、使用花括号

#### 2、使用内置函数dict（）

```python
#1、使用花括号
student={'moke':20,'jack':21,'jone':19}
print(student,type(student))
#2、使用内置函数dict（）
student1=dict(name='jack',age=17)
print(student1)
```

### 二十六、字典的查询操作

```python
student={'moke':20,'jack':21,'jone':19}
print(student,type(student))
student['jack']
print(student['jack'])
#print(student['jakj'])
print(student.get('jack'))
print(student.get('shdf'))

```

### 二十七、字典元素的增删查改

```python
student={'moke':20,'jack':21,'jone':19}
print(student,type(student))
student['jack']
print(student['jack'])
#print(student['jakj'])
print(student.get('jack'))
print(student.get('shdf'))
del student['jack']#删除字典元素
student.clear()#清空字典元素
print(student)
student['june']=28#新增元素
print(student)
student['june']=29#修改元素
print(student)
```

```python
student = {'moke': 20, 'jack': 21, 'jone': 19}
keys=student.keys()
print(keys,type(keys),list(keys))

values=student.values()
print(values,type(values),list(values))

items=student.    items()
print(items,type(items),list(items))
```

### 二十八、字典推导式

```python
items=['jack','june','jone']
prices=[12,23,34]
student={item.upper():price for item,price in zip(items,prices)}
print(student)
#{'JACK': 12, 'JUNE': 23, 'JONE': 34}
lst=zip(items,prices)
print(list(lst))
#[('jack', 12), ('june', 23), ('jone', 34)]
```

# 第七章

### 二十九、什么是元组

元组是python的内置数据结构之一，是一个不可变序列 

### 三十、元组的创建

```python
t=('ni','hao',2023)
t1='ni','hao',2023
print(t,t1)
print(type(t),type(t1))
t2=tuple(('ni','hao',2023))
print(t2)

#当元组只有一个元素时，
t3=('nihao')
print(type(t3))#<class 'str'>
t4=('nihao',)
print(type(t4))#<class 'tuple'>
#空列表
list1=[]
list2=list()
#空字典
d1={}
d2=dict()
#空元组
t5=()
t6=tuple()

```

为什么要将元组设计成不可变序列

1、在多任务环境下，同时操作对象时不需要加锁

注意事项：

元祖中存储的是对象的引用

1、如果元祖中对象本身不可对象，则不能再引用其他对象

2、如果元组中对象时可变对象，则可变对象的引用不允许改变，但数据可以改变

### 三十一、元祖的遍历

```python
t=('ni','hao',2023)

for i in range(0,3):
    print(t[i])

for item in t:
    print(item)
```

### 三十二、集合的创建

```python
s={1,22,3,4,5,5,6,5}
print(s,type(s))

#可以將其他类型的转换为集合 类型       列表【】，元组（），集合{}
#空集合不可以直接定义，需要使用内置函数进行定义
s1=set()
print(set(),type(set()))
```

### 三十三、集合的增删查改操作

```python

s={1,22,3,4,5,5,6,5}
print(s,type(s))

#可以將其他类型的转换为集合 类型       列表【】，元组（），集合{}
#空集合不可以直接定义，需要使用内置函数进行定义
s1=set()
print(set(),type(set()))

s.add(20)
print(s)

s.update({12,23,24})
print(s)#{1, 3, 4, 5, 6, 12, 20, 22, 23, 24}
#s.update(集合，元组，列表均可以)
s.remove(12)#如果元素不存在，keyerror抛异常
print(s)#
s.discard(200)#如果元素不存在，不报错
print(s)
s.pop()#不能够指定餐数，一般删除第一个，一次随机删除一个元素
print(s)
s.clear()
print(s)
```

##### 1、集合的子集关系

```python
s1={10,20,30,40}
s2={20,30,10,40}
#两个集合是否相等
print(s1==s2)
print(s1!=s2)
#集合之间子集关系
s3={10,20}
print(s3.issubset(s1))
#超集关系
print(s3.issuperset(s1))
#两个集合是否含有交集
print(s2.isdisjoint(s3))#False  有交集为False

```

##### 2、集合的数学操作

```python
s1={1,2,3,4,5,6}
s2={3,4,5,6,7,8,9}
print(s1.intersection(s2))#交集
print(s1 & s2)
#print(s1.intersection_update(s2))
print(s1.union(s2))#并集
print(s1 | s2)

print(s1.difference(s2))#s2在s1里的补集
print(s1 - s2)
print(s2.difference(s1))
print(s2-s1)

#对称差集
print(s1.symmetric_difference(s2))#除去相同的元素剩下的元素
print(s1^s2)
```

### 三十四、集合生成式

```python
#集合生成式
s={i**2 for i in range(1,10)}#{64, 1, 4, 36, 9, 16, 49, 81, 25}
print(s)#集合是無序的
```

# 第八章

### 三十五、字符串的驻留机制

仅保存一份相同且不可变字符串的方法不同的值被存放在字符串的驻留池中，python的驻留机制对相同的字符串只保留一份拷贝，后续创建相同字符串时，不会开辟新空间，而是把该字符串的地址赋给新创建的变量（只有符合标识符的字符串具有驻留机制（字母数字下划线组成），只在编译时驻留，而非运行时，只在（-5,256）之间的数字驻留）

在需要使用字符串拼接时使用join方法

```python
c=''.join(['ab','c'])
```

### 三十六、字符串的常用操作

##### 1、字符串的查找

```python

#字符串的字串查找
s='nihao,hello'
print(s.index('o'))#查找首次出現的位置
print(s.rindex('o'))#查找最後一次出現的位置
print(s.find('o'))
print(s.rfind('o'))
#print(s.index('r'))             #  ValueError: substring not found
print(s.find('r'))#-1




```

##### 2、字符串的对齐

```python
#字符串的对齐操作
s1='I love you'#如果指定宽度没有字符串长，直接输出原字符串
print(s1.center(20,'#'))#居中对齐，第一个参数为指定宽度，第二个参数为填充字符，默认为空格
print(s1.ljust(20,'#'))#左对齐
print(s1.rjust(20,'#'))#右对齐
print(s1.zfill(20))#只有一个参数的右对齐，空格用0不上
```

##### 3、字符串的劈分操作

```python
#字符串的劈分操作
'''1,从字符串的左侧开始劈分'''
print(s1.split())#默认为用空格劈分          ['I', 'love', 'you']
s2='I|love|you'
print(s2.split(sep='|'))#分隔符为指定的|           ['I', 'love', 'you']
print(s2.split(sep='|',maxsplit=1))#从左边开始分割，最大分个数为1，            ['I', 'love|you']

'''从右边开始分割'''
print(s2.rsplit())#如果分隔符没有空格，则作为一个字符串进行划分           ['I|love|you']
print(s2.rsplit(sep='|'))
print(s2.rsplit(sep='|',maxsplit=1))#           ['I|love', 'you']
```

##### 4、字符串的判断方法

```python
#字符串的判斷方法
#1、判断字符串是否是合法标识符
print('123zhangsan'.isidentifier())#False
print('zhagsan123'.isidentifier())#True
#2、判断字符串是否全部由空白字符组成
print('\t'.isspace())#True
print(' '.isspace())
#3、判断字符串是否全部由字母组成
print('zhangsan'.isalpha())#True
print('张三'.isalpha())#True
#4、判断字符串是否全部由十进制数字组成
print('10001110'.isdecimal())#True
print('16e1f'.isdecimal())#False
#5、判断字符串是否全部由数字组成
print('一二三'.isnumeric())##True
print('ⅡⅠⅢ'.isnumeric())#True
#6、判断字符串是否全部由数字和字母组成
print('zhangsan123'.isalnum())#True
print('ⅡⅠⅢzhangsa'.isalnum())#True

```

##### 5、字符串的替换与合并

```python
s3 = 'I|love you'
print(' '.join(s3.split(sep='|', maxsplit=1)))  # I love you
print(s3.replace('|', ' '))  # I love you
s4 = 'ni hao hao ma'
# 字符串的替換與合并
print(s4.replace('hao', '', 1))  # 第一個参数为被替换字符串，第二个参数为替换的字符串，第三个参数为替换的次数
# ni  hao ma
list1=['ni','hao','ma']
print(''.join(list1))#nihaoma
print('*'.join(list1))#ni*hao*ma
t=('ni','hao','ma')
print(''.join(t))#nihaoma
print('#'.join('lovevol'))#l#o#v#e#v#o#l
```

### 三十七    字符串的比较

##### 比较规则

 首先比较第一个字符，相等则一直比较下去，知道两个字符串中的字符不相等时，其比较结果就是两个字符串的比较结果，后续字符将不再被比较

##### 比较原理

两个字符进行比较时比较的是原始值（ordinal value）,调用内置函数ord可以得到字符的原始值，内置函数chr与ord相反，调用chr可以得到对应原始值的字符

```python
a='apple'
b='banan'
print(a>b)
print(ord('a'),ord('b'))
print(ord('陶'))#38518
print(chr(38518))#陶
#is和==的区别
#is是id的比较，==是值的比较

```

### 三十八、字符串的切片操作

```python
s = 'nihao,ma'
s1 = s[:5]
s2=s[6:]
s3='?'

str=s1+s3+s2

print(s1,s2)
print(str)#nihao?ma
print(s[-2::1])#ma
print(s[::-1])#am,oahin
```

### 三十九、格式化字符串

```python
name='JackTao'
age=19
#1、%格式化字符串
print('我今年%d岁，我的名字叫%s'%(age,name))
#2、format格式化字符串
print('我叫{0}，我今年{1}岁'.format(name,age))
#3、f-string格式化字符串
print(f'我叫{name}，我今年{age}岁')

print('{0:10.3}'.format(3.1415926535))#.3表示總共三位數
print('{:.3f}'.format(3.141592))#表示三位有效数字

```

### 四十、字符串的编码转换

编码与解码的方式

编码：将字符串转换为二进制数据（BYTES）

解码：将二进制转换为字符串类型的数据

```python
#字符串的编码与解码
s='何处无芳草'
#编码
print(s.encode(encoding='GBK'))
print(s.encode(encoding='UTF-8'))
#解码
byte=s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))
byte=s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))

```

# 第九章

### 四十一、函數的創建和调用

```python
#函数定义调用
def calc(a,b):
    c=a+b
    return c

a=int(input())
b=int(input())
print(calc(a,b))
```

### 四十二、函数的参数传递

形式參數在定义函数时，实际参数在调用函数时

函数参数传递的内存分析

```python
def nwn(n1, n2):
    print(n1)#20
    print(n2)#[10, 30, 40]
    n1=100
    n2.append(20)
    print(n1)#100
    print(n2)#[10, 30, 40, 20]
    return 0


n1 = 20
n2 = [10, 30, 40]
print(n1, n2)#20 [10, 30, 40]
nwn(n1, n2)
print(n1, n2)#20 [10, 30, 40, 20]

```

### 四十三、函数的返回值

```python

def fun(num):
    odd = []
    even = []
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)


    return even, odd

list1=[10,13,15,11111117,94,287,89]
print(fun(list1))#([10, 94], [13, 15, 11111117, 287, 89])

```

### 四十四、函数的参数定义

```python
# 所属学校：贵州师范大学
# 开发人员：陶景航
# 开发时间：2023/1/19 20:22
# 默认参数值
def fun1(a, b=10):
    print(a, b)
    # return


fun1(10)  # 10 10
print(fun1(10, 20))
'''
10 20
None
'''


# 位置可变的函数参数
def fun2(*num):  # 定义函数时，位置可变
    print(num)


fun2(10)
fun2(10, 20, 30)  # (10, 20, 30)     结果为元组


# 个数可变的关键字形参
def fun3(**num):
    print(num)


fun3(a=10)
fun3(a=20, b=30, c=40)  # 結果爲字典      {'a': 20, 'b': 30, 'c': 40}


# 在同一个函数定义中，个数可变的位置形参放在个数可变的关键字形参之前

# 在实参中转换个数可变的位置形参和关键字形参

def fun4(a, b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)


list = [11, 22, 33]
fun4(*list)
'''
a= 11
b= 22
c= 33
'''
dict = {'a': 123, 'b': 234, 'c': 345}
fun4(**dict)


def fun5(a, b, *, c, d):  # *后面的只能用关键字形参传递
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)


fun5(10, 20, c=30, d=40)


def fun6(a, b=10, *, c, d,**argss1):
    pass

def fun7(*args2,**argss2):
    pass


```

### 四十五、变量的作用域

```python
# 所属学校：贵州师范大学
# 开发人员：陶景航
# 开发时间：2023/1/26 19:23
def fun(age):
    print(age)

fun(12)

age=12
def fun2():
    print(age)

fun2()

def fun3():
    global age#將局部变量变为全局变量
    age=23

    print(age)

fun3()
print(age)
```

### 四十六、递归函数

```python
def fun(n):
    if n==1:
        return n
    else:
        return n*fun(n-1)

print(fun(5))
```

```python
#斐波那契数列
def fib(n):
    if n==1:
        return 1
    if n==2:
        return 1

    else:
        return fib(n-1)+fib(n-2)

for i in range(1,10):
    print(fib(i),end='  ')#1  1  2  3  5  8  13  21  34  


```

# 第十章

### 四十七、BUG的由来及分类

#### 1、粗心导致的错误

##### 1、漏了末尾的冒号

##### 2、缩进错误

##### 3、字符串拼接的时候，把字符串和数字连在一起

##### 4、没有定义变量的初始值

##### 5、‘==’和‘=’符号混用

#### 2、知识点不熟练导致的错误

##### 1、索引越界问题（IndexError）

##### 2、append（）方法使用掌握不熟练

#### 3、思路不清导致的问题（勤加练习）

### 四十八、不同异常类型的处理方式

### 四十九、异常处理机制

```python

try:
    a=int(input('请输入一个整数'))
    b=int(input('请输入另一个整数'))
    result=a/b

except BaseException as error:
    print('出錯了')
else:

    print(result)
```

```python
try:
    a=int(input('请输入一个整数'))
    b=int(input('请输入另一个整数'))
    result=a/b
    print(result)
except ZeroDivisionError:
    print('除数不能为零')
except ValueError:
    print('只能输入正整数')
print('程序结束')
```

```python

try:
    a=int(input('请输入一个整数'))
    b=int(input('请输入另一个整数'))
    result=a/b

except BaseException as error:
    print('出錯了')
    print(error)
else:
    print(result)
finally:
    print('謝謝你的使用')
```

ZeroDivisionError:(除或取模)零（所有数据类型）  
IndexError:序列中没有此索引  
KeyError:映射中没有这个键  
NameError:没有声明或初始化对象  
SyntaxError：语法错误  
ValueError：传入无效的参数

```python

import traceback
try:
    print('nihao')
    print(10/0)
except:
    traceback.print_exc()
```

### 五十、Pycharm的调试模式

# 第十一章

### 五十一、两大编程思想

解决复杂问题，面向对象更有利于从宏观上把握事物之间复杂的联系方便我们分析整个系统      具体到微观操作，仍然使用面向过程来实现

### 五十二、类和对象的创建

l类是多个相似事物组成的群体总成，能够帮助我们快速理解和判断事物的性质

类里面的一个数据称为对象Cl

```python
class Student:  # Student为类的名称，由一个或多个单词组成
    native_pace = '云南'  # 直接写在类里面的变量称为类属性

    def __init__(self, name, age):
    self.name = name  # self.name称为实例属性，在这里有一个赋值的操作
    self.age = age


# 实例方法
    def eat(self):
      print('在学生仓陈思南')


# 静态方法
    @staticmethod
    def method():
        print(',,,,,')


# 类方法
    @classmethod
    def cm(cla):
      print('kjlkjljjhgshjfg')


```

对象的创建

```python
class Student:  # Student为类的名称，由一个或多个单词组成
    native_pace = '云南'  # 直接写在类里面的变量称为类属性

    def __init__(self, name, age,class1):
        self.name = name  # self.name称为实例属性，在这里有一个赋值的操作
        self.age = age
        self.class2=class1

    # 实例方法
    def eat(self):
        print('在学生仓陈思南')

    # 静态方法
    @staticmethod
    def method():
        print(',,,,,')

    # 类方法
    @classmethod
    def cm(cla):
        print('kjlkjljjhgshjfg')

# 对象的创建
stu1=Student('彭俊',23,'应用统计学')
stu1.eat()
stu1.method()
stu1.cm()#kjlkjljjhgshjfg
print(stu1.class2,stu1.age,stu1.name)#应用统计学 23 彭俊

Student.eat(stu1)#在学生仓陈思南
```

各种类方法的使用

```python
class Student:  # Student为类的名称，由一个或多个单词组成
    native_pace = '云南'  # 直接写在类里面的变量称为类属性

    def __init__(self, name, age, class1):
        self.name = name  # self.name称为实例属性，在这里有一个赋值的操作
        self.age = age
        self.class2 = class1

    # 实例方法
    def eat(self):
        print('在学生仓陈思南')

    # 静态方法
    @staticmethod
    def method():
        print(',,,,,')

    # 类方法
    @classmethod
    def cm(cla):
        print('kjlkjljjhgshjfg')

stu1=Student('nihao',23,'nihanih')
print(Student.native_pace)#云南
print(id(Student.native_pace))
Student.native_pace='贵州'
print(Student.native_pace)#贵州
print(id(Student.native_pace))
#类方法的使用
stu1.cm()
#静态方法的使用
stu1.method()
```

### 五十三、类对象与属性

### 五十四、类方法与静态方法

### 五十五、动态绑定属性和方法

```python
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat(self):
        print(self.name+'在吃饭')


stu1=Student('彭俊',20)
stu1.gendal='女'
print(stu1.name,stu1.age,stu1.gendal)#彭俊 20 女

def show():
    print('女de')
stu1.show=show
stu1.show()#女de
#print(stu1.name,stu1.age)

```

# 第十二章

### 五十六、封装

```python
class Student:
    native_place='云南'
    def __init__(self,name,age):
        self.name=name
        self.__age=age#前面得下划线是使得age不能再类之外被访问
    def stop(self):
        print(self.name,self.__age)

stu1=Student('彭俊',23)
stu1.stop()
print(stu1._Student__age)#能够访问封装的内容
```

### 五十七、继承

```python
class Person(object):
    def __init__(self, name, age, gendal):
        self.name = name
        self.age = age
        self.gendal = gendal

    def xinxi(self):
        print(self.name, self.age, self.gendal)


class Student(Person):
    def __init__(self, name, age, gendal, stu_no):

        super().__init__(name, age, gendal)
        self.stu_no=stu_no

class Teacher(Person):
    def __init__(self,name,age,gendal,teacherofyear):
        super().__init__(name,age,gendal)
        self.teacherofyear=teacherofyear

class Header(Student,Teacher):
    pass

stu1=Student('彭俊',23,"男" , 211198741134)
tea1=Teacher('Mark',45,"男",23)

#一個子类可以继承多个父类

stu1.xinxi()
tea1.xinxi()
```

### 五十八、方法重写

```python
class Person(object):
    def __init__(self, name, age, gendal):
        self.name = name
        self.age = age
        self.gendal = gendal

    def xinxi(self):
        print(self.name, self.age, self.gendal)


class Student(Person):
    def __init__(self, name, age, gendal, stu_no):
        super().__init__(name, age, gendal)
        self.stu_no = stu_no

    def xinxi(self):#方法重寫
        super().xinxi()
        print('学号', self.stu_no)


class Teacher(Person):
    def __init__(self, name, age, gendal, teacherofyear):
        super().__init__(name, age, gendal)
        self.teacherofyear = teacherofyear

    def xinxi(self):#方法重写
        super().xinxi()
        print('教龄', self.teacherofyear)


class Header(Student, Teacher):
    pass


stu1 = Student('彭俊', 23, "男", 211198741134)
tea1 = Teacher('Mark', 45, "男", 23)

stu1.xinxi()  # 想要输出学号，重写父类的方法
tea1.xinxi()  # 同理


```

### 五十九、object类

重写父类中的属性方法

```python

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #self.gendal = gendal
    def __str__(self):
        print('我是{0}，我今年{1}岁'.format(self.name,self.age))

per1=Person('彭俊',23)
print(dir(Person))
per1.__str__()#我是彭俊，我今年23岁

```

### 六十、多态

```python
# 所属学校：贵州师范大学
# 开发人员：陶景航
# 开发时间：2023/1/30 15:34
class Movies(object):
    def __init__(self,diqu,yuyan):
        self.diqu=diqu
        self.yuyan=yuyan
    def __str__(self):
        print('中国，汉语',end=' ')

class War(Movies):
    def __str__(self):
        super().__str__()
        print('战争',end=" ")

class Kehuan(Movies):
    def __str__(self):
        super().__str__()
        print('科幻',end=' ')

class Love(Movies):
    def __str__(self):
        super().__str__()
        print('爱情',end=' ')

class Jishi(Movies):
    def __str__(self):
        super().__str__()
        print('纪实',end=' ')

#Ji1=Jishi('中国','汉语')
#Ji1.__str__()

class M(War):
    def __init__(self,name,year,fen):
        self.name=name
        self.year=year
        self.fen=fen
    def __str__(self):
        super().__str__()
        print(self.name,self.year,self.fen)

#m1=M('金刚川',2020,9.0)
#m1.__str__()
class MA(War):
    def __init__(self,name,year,fen):
        self.name=name
        self.year=year
        self.fen=fen
    def __str__(self):
        super().__str__()
        print(self.name,self.year,self.fen)

class MB(Kehuan):
    def __init__(self, name, year, fen):
        self.name = name
        self.year = year
        self.fen = fen

    def __str__(self):
        super().__str__()
        print(self.name, self.year, self.fen)

class MC(War,Love):
    def __init__(self, name, year, fen):
        self.name = name
        self.year = year
        self.fen = fen
        def __str__(self):
            super().__str__()
            print(self.name, self.year, self.fen)

class MD(War,Jishi):
     def __init__(self, name, year, fen):
         self.name = name
         self.year = year
         self.fen = fen
     def __str__(self):
         super().__str__()
         print(self.name, self.year, self.fen)

m1=MA('金刚川',2020,9.0)
m1.__str__()
m2=MB('流浪地球',2019,8.4)
m2.__str__()
m3=MC('霸王别姬',1993,9.2)
m3.__str__()
m4=MD('红海行动',2018,9.3)
m4.__str__()
```

### 六十一、特殊方法和特殊属性

```python
#特殊方法
class A():
    pass
class B():
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age
c1=C('Jack',23)
print(c1.__dict__)#实例对象的属性字典
print(c1.__class__)#输出对象所属的类
print(C.__bases__)#输出C类的所有父类
print(C.__mro__)#输出类的层次结构
print(A.__subclasses__())#输出子类的列表
```

```python
class Student:
    def __init__(self,name):
        self.name=name

    def __add__(self, other):
        return self.name+other.name

    def __len__(self):
        return len(self.name)

s1=Student('jack')
s2=Student('marry')
s=s1+s2
print(s)#4

list=[11,22,33,44]
print(len(list))
print(len(s))#9
```

```python
# new 與init創建對象的過程
class Person(object):
    def __new__(cls, *args, **kwargs):
        print('cls的id 為{}'.format(id(cls)))#2
        obj = super().__new__(cls)
        print('obj的id{}'.format(id(obj)))#3
        return obj

    def __init__(self, name, age):
        print('self的id為{}'.format(id(self)))#3
        self.name = name
        self.age = age


print('object的id{}'.format(id(object)))#1
print('Person的id為{}'.format(id(Person)))#2
p1 = Person('nihao', 23)
print('p1的id為{}'.format(id(p1)))#3
'''object的id140706060668400
Person的id為2976926098176
cls的id 為2976926098176
obj的id2976928780048
self的id為2976928780048
p1的id為2976928780048'''
```

### 六十二、类对象的赋值与拷贝

```python
class CPU:
    pass
class DISK:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk
#类对象的赋值
cpu1=CPU()
cpu2=cpu1
print(id(cpu1),id(cpu2))#2010816336272 2010816336272

disk1=DISK()
computer=Computer(cpu1,disk1)

#浅拷贝
import copy
computer2=copy.copy(computer)
print(id(computer2),id(computer))#2010816336464 2010816336336
print(id(computer.cpu),id(computer2.cpu))#2010816336272 2010816336272

#深拷贝

computer3=copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)   #<__main__.Computer object at 0x0000023582E65310> <__main__.CPU object at 0x0000023582E652D0> <__main__.DISK object at 0x0000023582E65350>
print(computer3,computer3.cpu,computer3.disk)#<__main__.Computer object at 0x0000023582E65450> <__main__.CPU object at 0x0000023582E65490> <__main__.DISK object at 0x0000023582E656D0>
```

# 第十三章

### 六十三、什么叫模块

```python
from  math import pi                #導入其中一個模塊
import math   #直接导入
print(math.pi)
print(math.sin(1))

```

### 六十四、自定义模块

```python
mport calc
#导入自定义模块
from calc import add
#导入其中一个

'''calc'''
def add(a,b):
    return a+b
def div(a,b):
    return a/b
```

### 六十五、以主程序的形式执行

```python
'''calc'''


def add(a, b):
    return a + b


def div(a, b):
    return a / b


if __name__=='__main__':#只有當calc为主程序时才会执行的语句
    print(add(10, 20))

#第二个模块
mport calc
#导入自定义模块
from calc import add
#导入其中一个

print(add(20,30))#50
```

### 六十六、python中的包

```python
import clm.ahb as am
#  软件包名。模块名 as 别名
print(am.a)#1000
```

| sys      | 与python解释器及其操作环境相关      |
|:--------:|:-----------------------:|
| time     | 时间相关                    |
| os       | 访问操作系统服务功能              |
| calender | 日期相关                    |
| urllib   | 读取网上服务器数据标准库            |
| json     | 使用JSON序列化和反序列化对象        |
| re       | 字符串中执行正则表达式执行匹配和替换      |
| math     | 数学运算函数                  |
| decimal  | 精确控制精度，有效位数   和四舍五入     |
| logging  | 灵活的记录时间，错误，警告和调试信息等日志相关 |

### 六十七、第三方模块的安装及使用

安装：win+r》cmd》pip  instull  模块名

python

使用import  模块名

# 第十四章

### 六十八、编码格式介绍

### 六十九、文件读写原理

### 七十、文件读写操作

| r   | 只读模式，如果文件存在，指针在文件的开头                       |
| --- | ------------------------------------------ |
| w   | 只写模式，如果文件不存在，则创建新文件，如果文件存在，则覆盖源文件，指针在文件的开头 |
| a   | 追加模式，文件不存在则创建文件，文件存在则在文件末未进行追加，指针在文件的末尾    |
| b   | 二进制打开模式，不能单独使用，与其他功能一起使用                   |
| +   | 以读写模式打开，不能单独打开，与其他模式混合使用                   |

### 七十一、文件对象常用的方法

| reda([size])          | 读取size个字节的内容返回，若省略，则读取到末尾                                                                                                                                                                                                                                                                                                                                              |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| readline()            | 从文中读取一行内容                                                                                                                                                                                                                                                                                                                                                              |
| readlines()           | 把文本中每一行作为独立的字符串对象放入列表返回                                                                                                                                                                                                                                                                                                                                                |
| write(str)            | 将str内容写入文件                                                                                                                                                                                                                                                                                                                                                             |
| writelines(s_list)    | 将字符串s_list写入文本，不添加换行符                                                                                                                                                                                                                                                                                                                                                  |
| seek(offset[,whence]) | 把文件指针移动到新的位置offset表示相对于 whence的位置：      offset：为正往结束方向移动，为负往结束方向移动                        whence不同的值代表不同的含义                                                                    0：从文件头开始计算（默认值）                                                               1：从当前位置开始计算                                                                                  2 ：从结尾位置开始计算 |
| tell()                | 返回文件指针的当前位置                                                                                                                                                                                                                                                                                                                                                            |
| flush()               | 把缓冲区的内容写入文件，但不关闭文件                                                                                                                                                                                                                                                                                                                                                     |
| close()               | 关闭文件，释放文件对象的相关资源                                                                                                                                                                                                                                                                                                                                                       |

### 七十二、with语句（上下文管理器）

```python
class MyContengGer():
    def __enter__(self):
        print("1")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("2")

    def show(self):
        print("3")


with MyContengGer() as File:
    File.show()#1 3 2
```

### 七十三、目录操作

os是python内置与操作系统和文件系统 相关的模块

os模块和    os.path模块用于对目录或文件进行操作

os操作目录相关函数

| getcwd()                        | 返回当前的工作目录       |
| ------------------------------- | --------------- |
| listdir(path)                   | 返回指定路径下的文件和目录信息 |
| mkdir(path.[,mode])             | 创建目录            |
| makedirs(path1/path2...[,mode]) | 创建多级目录          |
| redir(path)                     | 删除目录            |
| removedirs(path1/path2...)      | 删除多级目录          |
| chdir(path)                     | 将path设置为当前工作目录  |

os.path操作目录相关函数

| abspath(path)   | 用于获取文件或目录的绝对路径           |
| --------------- | ------------------------ |
| exists(path)    | 用于判断文件或者是目录是否存在，存在返回True |
| join(path,name) | 将目录与目录或者文件名拼接起来          |
| splitext()      | 分离文件名和扩展名                |
| basename(path)  | 从一个目录中提取文件名              |
| dirname(path)   | 从一个路径中提取文件路径 ，不包括文件名     |
| isdir(path)     | 用于判断是否为路径                |

```python
 #用于获取指定路径下的所有文件
import os
path=os.getcwd()
list=os.listdir(path)
for filename in list:
    if filename.endswith('.py'):
        print(filename)
```

# py3_practice
some practice;

aaaa



# numpy 的属性:

- ndim：维度
- shape：行数和列数
- size：元素个数


```python
import numpy as np
import matplotlib.pyplot as plt
```


```python
array = np.array([[1,2,3],[2,3,4]])  #列表转化为矩阵
```


```python
print('number of dim:',array.ndim)  # 维度
# number of dim: 2

print('shape :',array.shape)    # 行数和列数
# shape : (2, 3)

print('size:',array.size)   # 元素个数
```

    number of dim: 2
    shape : (2, 3)
    size: 6
    

# 创建 array 的多种形式

- array：创建数组
- dtype：指定数据类型
- zeros：创建数据全为0
- ones：创建数据全为1
- empty：创建数据接近0
- arrange：按指定范围创建数据
- linspace：创建线段


```python
a = np.array([2,23,4])  # list 1d
a
```




    array([ 2, 23,  4])




```python
a = np.array([2,23,4],dtype=np.int)
print(a.dtype)
# int 64
a = np.array([2,23,4],dtype=np.int32)
print(a.dtype)
# int32
a = np.array([2,23,4],dtype=np.float)
print(a.dtype)
# float64
a = np.array([2,23,4],dtype=np.float32)
a
# float32
```

    int32
    int32
    float64
    




    array([  2.,  23.,   4.], dtype=float32)




```python
#创建特定数据 

a = np.array([[2,23,4],[2,32,4]])  # 2d 矩阵 2行3列
a
```




    array([[ 2, 23,  4],
           [ 2, 32,  4]])




```python
#创建全零数组
a = np.zeros((3,4)) # 数据全为0，3行4列
a
```




    array([[ 0.,  0.,  0.,  0.],
           [ 0.,  0.,  0.,  0.],
           [ 0.,  0.,  0.,  0.]])




```python
# 创建全1的数据
a = np.ones([3,4])
a
```




    array([[ 1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.]])




```python
#创建全一数组, 同时也能指定这些特定数据的 dtype:
a = np.ones((3,4),dtype = np.int)   # 数据为1，3行4列
a
```




    array([[1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1]])




```python
#创建全空数组, 其实每个值都是接近于零的数:
a = np.empty((3,4)) # 数据为empty，3行4列
a
```




    array([[ 1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.]])




```python
#用 arange 创建连续数组:
a = np.arange(10,20,2) # 10-19 的数据，2步长
a
```




    array([10, 12, 14, 16, 18])




```python

#使用 reshape 改变数据的形状
a = np.arange(12).reshape((3,4))    # 3行4列，0到11
a
```




    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]])




```python
#用 linspace 创建线段型数据:
a = np.linspace(1,10,20)    # 开始端1，结束端10，且分割成20个数据，生成线段
a
```




    array([  1.        ,   1.47368421,   1.94736842,   2.42105263,
             2.89473684,   3.36842105,   3.84210526,   4.31578947,
             4.78947368,   5.26315789,   5.73684211,   6.21052632,
             6.68421053,   7.15789474,   7.63157895,   8.10526316,
             8.57894737,   9.05263158,   9.52631579,  10.        ])




```python
#同样也能进行 reshape 工作:
a = np.linspace(1,10,10).reshape((5,2)) # 更改shape
a
```




    array([[  1.,   2.],
           [  3.,   4.],
           [  5.,   6.],
           [  7.,   8.],
           [  9.,  10.]])



# numpy的基本运算

### 一维


```python
a=np.array([10,20,30,40])   # array([10, 20, 30, 40])
b=np.arange(4)              # array([0, 1, 2, 3])
```


```python
c=a-b
c
```




    array([10, 19, 28, 37])




```python
c=a+b
c
```




    array([10, 21, 32, 43])




```python
c = a*b
c
```




    array([  0,  20,  60, 120])




```python
c = a**2
c
```




    array([ 100,  400,  900, 1600], dtype=int32)




```python
c=10*np.sin(a) 
c
```




    array([-5.44021111,  9.12945251, -9.88031624,  7.4511316 ])




```python
c = b<3  # 逻辑判断
c
```

### 多维


```python
a=np.array([[1,1],[0,1]])
b=np.arange(4).reshape((2,2))
print(a)
print(b)
```

    [[1 1]
     [0 1]]
    [[0 1]
     [2 3]]
    


```python
c_dot = np.dot(a,b) # 矩阵相乘
c_dot
```




    array([[2, 4],
           [2, 3]])




```python
c_dot2=a.dot(b) # 另一种用法
c_dot2
```




    array([[2, 4],
           [2, 3]])



### 常用方法


```python
a=np.random.random((2,4))
a
```




    array([[ 0.51848395,  0.61883962,  0.40433263,  0.61301354],
           [ 0.14642716,  0.08890739,  0.41561434,  0.24841116]])




```python
np.sum(a)
```




    3.0540297911076144




```python
np.min(a) 
```




    0.088907386512613762




```python
np.max(a)  
```




    0.61883962244165069




```python
np.mean(a)
```




    0.3817537238884518




```python
a.min()  # 另一种用法
```




    0.088907386512613762



#### axis参数 
- 对行或者列进行查找运算，就需要在上述代码中为 axis 进行赋值。 当axis的值为0的时候，将会以列作为查找单元， 当axis的值为1的时候，将会以行作为查找单元。


```python
print("a =",a)

print("sum =",np.sum(a,axis=1))

print("min =",np.min(a,axis=0))

print("max =",np.max(a,axis=1))
```

    a = [[ 0.51848395  0.61883962  0.40433263  0.61301354]
     [ 0.14642716  0.08890739  0.41561434  0.24841116]]
    sum = [ 2.15466975  0.89936004]
    min = [ 0.14642716  0.08890739  0.40433263  0.24841116]
    max = [ 0.61883962  0.41561434]
    

#### 数组的切片：获取子数组
- x[start:stop:step]


```python
x = np.arange(10)
x
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
x[:2]
```




    array([0, 1])




```python
x[3::2]
```




    array([3, 5, 7, 9])




```python
x[5::-2]
```




    array([5, 3, 1])




```python
x2 = np.arange(12).reshape(3,4)
x2
```




    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]])




```python
x2[:2,:3] #两行三列
```




    array([[0, 1, 2],
           [4, 5, 6]])




```python
x2[::-1,::-1] # 逆序
```




    array([[11, 10,  9,  8],
           [ 7,  6,  5,  4],
           [ 3,  2,  1,  0]])



- 获取数组的行和列


```python
x2
```




    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]])




```python
x2[:,0] # 第一列
```




    array([0, 4, 8])




```python
x2[0,:] # 第一行
```




    array([0, 1, 2, 3])




```python
x2[0] # 另一种取法
```




    array([0, 1, 2, 3])



### 数组切片返回的数组数据的视图，而不是数据的副本，修改切片会修改原始数据！


```python
x2
```




    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]])




```python
x2_sub = x2[:2,:2]
x2_sub
```




    array([[0, 1],
           [4, 5]])




```python
x2_sub[0,0] = 1 # 修改第一个数
```


```python
x2
```




    array([[ 1,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]])




```python
x2[0,0] = 0
```

#### 创建数组的副本
-  通过copy()方法实现,修改副本数据不会影响原数据


```python
x2_sub_copy = x2[:2,:2].copy()
x2_sub_copy
```




    array([[0, 1],
           [4, 5]])




```python
x2_sub_copy[0,0] = 1
x2
```




    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]])



### 数组的拼接和分裂

### 数组的拼接
- np.concatenate
- np.vstack
- np.hstack


```python
x = np.array([1,2,3])
y = np.array([4,5,6])
z = np.array([99,99])
```


```python
np.concatenate([x,y])
```




    array([1, 2, 3, 4, 5, 6])




```python
np.concatenate([x,y,z])
```




    array([ 1,  2,  3,  4,  5,  6, 99, 99])




```python
grid = np.arange(6).reshape(2,3)
grid
```




    array([[0, 1, 2],
           [3, 4, 5]])




```python
np.concatenate([grid,grid])
```




    array([[0, 1, 2],
           [3, 4, 5],
           [0, 1, 2],
           [3, 4, 5]])




```python
np.concatenate([grid,grid],axis=1) #沿第二个轴拼接
```




    array([[0, 1, 2, 0, 1, 2],
           [3, 4, 5, 3, 4, 5]])



- 用np.vstack（垂直栈）和np.hstack（水平栈）函数更简洁


```python
x = np.array([1,2,3])
y = np.array([[99],[99]])
grid = np.array([[9,8,7],
                [6,5,4]])
```


```python
np.vstack([x,grid])
```




    array([[1, 2, 3],
           [9, 8, 7],
           [6, 5, 4]])




```python
np.hstack([grid,y])
```




    array([[ 9,  8,  7, 99],
           [ 6,  5,  4, 99]])



#### 数组的分裂
- np.split
- np.hsplit
- np.vsplit


```python
x = [1,2,3,99,99,3,2,1]
```


```python
x1,x2,x3 = np.split(x,[3,5])
```


```python
print(x1,x2,x3)
```

    [1 2 3] [99 99] [3 2 1]
    


```python
grid = np.arange(16).reshape(4,4)
grid
```




    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11],
           [12, 13, 14, 15]])




```python
upper,lower = np.vsplit(grid,[2])
```


```python
upper
```




    array([[0, 1, 2, 3],
           [4, 5, 6, 7]])




```python
lower
```




    array([[ 8,  9, 10, 11],
           [12, 13, 14, 15]])




```python
left,right = np.hsplit(grid,[2])
```


```python
left
```




    array([[ 0,  1],
           [ 4,  5],
           [ 8,  9],
           [12, 13]])




```python
right
```




    array([[ 2,  3],
           [ 6,  7],
           [10, 11],
           [14, 15]])



### 通用函数
- numpy为多种数据类型的操作提供了方便的，静态类型的，可编译程序的接口，也被称作<向量操作>
- 通过简单地对数组执行操作，操作会作用于数组中的每一个元素

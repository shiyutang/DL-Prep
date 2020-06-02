
# 深度学习知识总结
先从伯禹的学习资料入手，边学习，边 [整理记录](https://github.com/shiyutang/Hands-on-deep-learning) +《
[神经网络和深度学习](https://nndl.github.io/nndl-book.pdf)
》补充；
累了可以听听 [MIT 的6.S191](https://www.youtube.com/watch?v=JN6H4rQvwgY) refresh一下

根据下列框架进行结构性的知识总结。

1.浅层神经网络及模型基础

* [1.1 线性回归](线性回归.ipynb)
    * 定义
    * 实施步骤
    * 要点
    * 主要函数
    * 主要问题：
        * 1.构建一个深度学习网络并训练需要哪些步骤
        * 2.什么时候该用parameter.data

* [1.2 分类模型和softmax](分类模型和Softmax.ipynb)
    * 定义
    * softmax的性质
    * softmax的优势
    * 分类模型
    * 交叉熵函数

* [1.3 多层感知机](多层感知机.ipynb)
    * 定义
    * 激活函数
    * 主要问题：
        * 如何选择不同激活函数

* [1.4 模型选择（过拟合欠拟合的出现和解决)](模型选择（过拟合欠拟合出现和解决）.ipynb)
    * 模型选择的方法
    * 欠拟合和过拟合定义和影响因素
    * 欠拟合和过拟合的解决方法
        * 权重衰减和正则化
        * dropout

* [1.5 数值稳定性与模型初始化](数值稳定性与模型初始化.ipynb)
    * 梯度消失和梯度爆炸
    * 导致梯度消失和爆炸的原因
    * 神经原初始化

2.卷积神经网络详解
* [2.1 卷积神经网络](卷积神经网络.ipynb)
    * 起源和特点
    * 卷积神经网络组成
    * 卷积层及其可选操作
        *  空洞卷积  **todo**
        *  感受野的计算  **todo**
    * Pooling层
    * 归一化层： 
        *  实例归一化 **todo**
        *  批归一化 
        *  组归一化 **todo**
    * 损失函数  **todo**
        *  交叉熵损失函数
        *  L2损失
        *  L1损失
    * 卷积神经网络的整体结构
    * 主要网络架构及其特点
        * Lenet
        * Alexnet
        * VGG
        * Network in Network（NIN）
        * GoogLenet  
        * Resnet  
        * DenseNet

* 3.循环神经网络  **todo**
    * 基础
    * GRU
    * Lstm
    * 深度循环神经网络
    * 双向循环神经网络

* 4.注意力机制  **todo**
    * 基础
    * Seq2seq中的应用

* 5.Transformer  **todo**

* [6.优化](优化.ipynb)
    * 深度学习优化：
        * 深度学习优化和普通优化的差异
        * 基于梯度的优化方法的挑战
    * 凸优化
        * 凸性
        * 凸函数的性质和 Jensen 不等式
        * 如何优化带有限制条件的函数 
    * 优化算法
        * 牛顿法
        * 共轭梯度法
        * 随机梯度下降法
        * 小批量随机梯度下降法 (SGD)
    * 高阶优化算法
        * momentum
        * AdaGrad       
        * RMSProp
        * AdaDelta
        * Adam

* 7.数据增强  **todo**

* 8.模型微调  **todo**

* 9.GAN     **todo**
    * basic
    * DCGAN

* 10.目标检测  **todo**

* 11.语义分割  **todo**

* 12.领域自适应  **todo**

* 13.风格迁移  **todo**

* 14.变化检测  **todo**

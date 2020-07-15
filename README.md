# DL-Prep
**深度学习基础知识，算法，面试题**
**由 UESTC DL 学习小组开发和维护**

1. [数学相关(Math)](01_Math/README.md)
2. [机器学习基础相关(ML)](02_ML_knowledge/README.md)
3. [深度学习相关(DL)](03_DL_knowledge/README.md)
4. [基础算法题相关(AL)](04_Algorithms/README.md)
5. [语言相关(LA)](05_Language/README.md)
6. [深度学习框架(DF)](06_DL_framework/README.md)
6. [面试题(IQ)](07_Interview_Questions/README.md)


## 维护笔记
1. 当需要更改前，增加一个新的 branch，确认自己的更改好之后，再和 master 合并
1. 当需要添加新知识时，可以对照目录，插入到对应的位置，并按照格式增加目录和在相应位置增加内容
2. 插入图片时，先将图片放入 Pics 文件夹，随后按照相对路径插入
3. 插入了目录，但是又没有时间写内容？ 可以加个 **todo** 之后补全
3. 大纲和格式可能有错漏，欢迎互相指正修改~

### 增加了 Jupyter Notebook之后
我们将在 README.md 的基础上增加 Jupyter Notebook， 这样，我们可以方便在本地查看公式，并运行代码。MD则在 Github 上可以提供大纲的预览。
建议的方式是：
- 查看：将 Github 的仓库拉取到本地，并在本地 launch Jupyter Server 进行查看，查看时先打开第一层级的 README.ipynb 进行索引
- 修改：新开 branch 后在 Pycharm / Jupyter Notebook 等编辑器中编辑，编辑 Jupyter Notebook 的同时，我们需要在MD里面进行目录的同步。并用【查看】的方式预览编辑效果
- 合并：本地修改好了之后，使用 Git commit， Git push， 再在本地或者云端merge

原则是：Jupyter Notebook 负责内容，因此 MarkDown 中有的内容，Jupyter Notebook 中一定会有； 同时 Readme.md 提供预览，因此需要有大纲和相关说明。
先行编辑 Jupyter Notebook，之后在 MarkDown 中相应更新。

### 如何添加 Anchor ？
Anchor 帮助我们快速跳转到需要的内容，那么如何添加 anchor 呢？
详见 [添加Anchor](Utils/AddAnchor.ipynb)

## 其他
欢迎大家 fork, pull request, star 这个项目
大部分都是手打，根据资料整理，如有问题，欢迎 fork 之后 pull request 或者 issue 中提出，我们会尽可能及时回复


## 主要内容

### 1. 数学知识：矩阵理论，概率论等
* 2.线性代数
    * 2.1 标量，向量，矩阵和张量
    * 2.2 矩阵和向量相乘：
    * 2.3 单位矩阵和逆矩阵：
    * 2.4 线性相关和生成子空间：
    * 2.5 范数:衡量向量大小的函数

* 3.概率和信息论

* 4.数值计算
    * 4.1 上溢和下溢
    * 4.2 病态条件
    * 4.3基于梯度的优化方法
        * 4.3.1 雅可比和海森矩阵

### 2.#  机器学习知识总结
李航机器学习整理+ [this repo](https://github.com/shiyutang/MachineLearning)+ [shuhuai 的白板推导视频](https://www.bilibili.com/video/BV1aE411o7qd?p=2)

* [1. 频率派和贝叶斯派](#1.频率派和贝叶斯派)
    * 频率派
    * 贝叶斯派

* [2. 聚类](#2.聚类) 
    * 聚集派
    * 连接派

* [3. 降维](#3.降维)
    * PCA
    * SVD



### 3. 深度学习知识总结
先从伯禹的学习资料入手，边学习，边 [整理记录](https://github.com/shiyutang/Hands-on-deep-learning) +《
[神经网络和深度学习](https://nndl.github.io/nndl-book.pdf)
》补充；
累了可以听听 [MIT 的6.S191](https://www.youtube.com/watch?v=JN6H4rQvwgY) refresh一下

根据下列框架进行结构性的知识总结。

1.浅层神经网络及模型基础

* [1.1 线性回归](01_线性回归.ipynb)
    * 定义
    * 实施步骤
    * 要点
    * 最小二乘法（基于数据计算得到解析解的线性回归）
        * 1. 矩阵推导出最小二乘解析解
        * 2. 利用函数求导方式求得最小二乘估计解析解
        * 3. 最小二乘估计的集合解释
    * 主要函数
    * 主要问题：
        * 1.构建一个深度学习网络并训练需要哪些步骤
        * 2.什么时候该用parameter.data

* [1.2 分类模型和softmax](02_分类模型和Softmax.ipynb)
    * 定义
    * softmax的常数不变性
    * softmax的优势
    * 分类模型
        * 定义
        * 交叉熵函数

* [1.3 多层感知机](03_多层感知机.ipynb)
    * 定义
    * 激活函数
    * 主要问题：
        * 如何选择不同激活函数

* [1.4 模型选择（过拟合欠拟合的出现和解决)](04_模型选择（过拟合欠拟合出现和解决）.ipynb)
    * 模型选择的方法
        * 验证数据集进行验证
        * k折验证法(数据少)
    * 欠拟合和过拟合定义和影响因素
    * 欠拟合和过拟合的解决方法
        * 权重衰减和正则化
        * dropout

* [1.5 数值稳定性与模型初始化](05_数值稳定性与模型初始化.ipynb)
    * 梯度消失和梯度爆炸
    * 导致梯度消失和爆炸的原因
    * 缓解梯度消失/爆炸：
        * 神经元初始化
        * 选择激活函数
        * 批归一化

2.卷积神经网络详解
* [2.1 卷积神经网络](06_卷积神经网络.ipynb)
    * 起源和特点
    * 卷积神经网络组成
    * 卷积层及其可选操作AM
        *  空洞卷积  **todo**
        *  感受野的计算  **todo**
    * Pooling层
    * 归一化层：
        *  实例归一化 **todo**
        *  批归一化
            * 全连接层的批归一化
            * 卷积层的批归一化
            * 训练和预测的批归一化
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

* [3.注意力机制](08_注意力机制.ipynb)
    * 1. 简介
    * 2. SEnet (Squeeze-excitation network)
    * 3. SKNET, CBAM 等

* 4.循环神经网络  **todo**
    * 基础
    * GRU
    * Lstm
    * 深度循环神经网络
    * 双向循环神经网络

* 5.Transformer  **todo**

* [6.优化](09_优化.ipynb)
    * 深度学习优化：
        * 深度学习优化和普通优化的差异
        * 基于梯度的优化方法的挑战
            * 山间缝隙（梯度反复震荡）
            * 鞍点
            * 梯度消失
        * 基于梯度优化算法
            * 证明：沿梯度反方向移动自变量可以减小函数值
    * 凸优化
        * 凸性
        * 凸集合
        * 凸函数的判定： Jensen 不等式
        * 凸函数的性质
            * 无局部最小
            * 和凸集的关系：水平面截取定义域
            * 二阶条件证明： 凸函数 $\Longleftrightarrow$ 二阶导数大于0
        * 如何优化带有限制条件的函数 
    * 优化算法
        * 优化方法：
            * 解析方法
            * 迭代方法
                * 一阶方法
                * 二阶方法
        * 最速下降法:
            * 凸函数下不同学习率的实验
            * 非凸函数的实验
            * 多维梯度下降
        * 二阶方法：
            * 优势
            * 牛顿法
            * 收敛性分析
        * 共轭梯度法
        * 随机梯度下降法
            * 参数更新
            * 抖动问题：
                * 调整学习率
                * 增大batch
        * 小批量随机梯度下降法 (SGD)
    * 高阶优化算法
        * 病态问题：
            * 公式定义：条件数
            * 解决方法：
                * 归一化统一量纲
                * 平均历史梯度
                * hessian矩阵预处理
        * momentum（历史梯度滑动平均）
            * 算法表达
            * (指数加权平均)滑动平均
                * 权值之和为（1-b^t）
                * 指数加权平均约等于 $\frac{1}{1-\beta}$ 个历史结果的指数加权平均
                * 由指数加权移动平均理解动量法
        * AdaGrad: 累计梯度平方归一化       
        * RMSProp：梯度平方滑动平均归一化
        * AdaDelta：RMS基础上使用自变量变化量的指数滑动平均来替代学习率
        * Adam：动量的滑动平均使用梯度平方滑动平均归一化当作自变量的梯度

* 7.[模型微调](10_模型微调.ipynb)
    * 模型微调的定义和方法
    * 训练热狗分类任务
        * 获取数据集
        * 加载模型，设置微调层和优化器
        * 使用/不使用模型微调的结果对比
        * 总结


* 8.GAN     **todo**
    * basic
    * DCGAN

* 9.目标检测  **todo**

* 10.语义分割  **todo**

* 11.领域自适应  **todo**

* 12.风格迁移  **todo**

* 13.变化检测  **todo**

### 4. 主要算法总结
根据斯坦福 CS97SI 课程整理相关知识，并辅助以leetcode中有疑惑的算法题解析进行讨论

根据CS 97SI 总结的笔记，以及 python 语法笔记，在[这里](https://www.notion.so/shiyu00daisy/Xtreme-0f9c9b3264ea4126b02dc89224d6a524) 

### 5. Python等计算机语言
这部分主要有一个大概框架来汇总语法糖和语言中常见的机制内部实现等

### 6. 深度学习框架
总结深度学习框架：pytorch，tensorflow等中的语法和机制

根据[深度学习框架pytorch 入门与实践](https://github.com/chenyuntc/pytorch-book) 的结构总结+[网页](https://pytorch.apachecn.org/docs/1.2/intermediate/model_parallel_tutorial.html)

### 7. 面试题
将见过的面试题和自己想到查到的回答

* [1. 训练加速](#1.训练加速)
    * 数据并行
        * Pytorch 的 DataParallel 流程图
    * 数据并行(nn.distributed) \* [todo]
    * 模型并行
    * pytorch的dataparallel

* [2. 目标检测](#2.目标检测) 
    * 1.算法有哪些？他们的对比？
        * RCNN：
        * fast RCNN
        * faster RCNN
        * YOLO
            * YOLOV2
            * YOLOV3
        * SSD
    * 2.简述一下YOLOv2的原理，v1和v2有什么区别？
    * 3.非极大抑制是什么，有什么作用？
    * 4.如何计算 Anchor 和真实 bbox 之间的 mIOU，以及如何在此基础上进行 NMS 算法？
    * 5.nms的发展（greedy-nms，soft-nms，fast-nms，matrix-nms） \* [todo]
    * 6.YOLOv2为什么将输入尺寸从448降到416
    * 7.YOLOv2对于anchor的使用与faster-rcnn有何不同?
    * 8.YOLOv2,v3一个anchor可以对应几个GT？SSD呢？RCNN系列呢？
    * 9.YOLOv3对于v2做了怎样的改进？
    * 10.YOLOv2与v3筛选正负样本的方式类似，具体是怎样进行的？这种操作解决了什么问题？
    * 11.YOLOv3的多尺度输出结构与FPN有何不同？
    * 12.YOLOv2,v3的anchor聚类如何做？指标是什么？
    * 13.FPN的多尺度输出结构与SSD的多尺度输出结构哪个效果更好
    * 14.faster-rcnn在撒anchor的时候，是如何把特征图坐标映射到图像上的？
    * 15.faster-rcnn的OHEM与ssd的OHEM有何不同
    * 16.roi pooling与roi align的具体操作
    * 17.retinanet解决了以往one-stage检测器的什么问题
    * 18.Focal loss一定有效吗？为什么？试举出一个例子
    * 19.介绍cascade-RCNN和DCN模块。Cascade-rcnn解决了什么问题？cascade-RCNN一般选用几个阶段？
    * 20.anchor-free的方式大概分为哪两种？各有什么特点？
    * 21.coco的mAP的计算公式
    * 22.为什么 Faster RCNN 相较 YOLO v2 更慢？
    * 23.为什么 Faster RCNN 预测准确度相比于 一阶段网络更高？
    * 24.介绍一下 RPN 的结构？
    * 25.YOLO 和 SSD 的区别？

* [3. 循环卷积神经网络](#3.循环卷积神经网络) 
    * 1.LSTM为什么会导致梯度爆炸？要如何解决？

* [4. 语义分割](#4.语义分割) 
    * 1.主要语义分割的算法有哪些，他们有什么区别？
        * 1. FCN(全卷积网络)
        * 2. Unet
        * 3. SegNet
        * 4. Deeplab v3+
        * 5. PSPNet(金字塔场景分割网络) 
    * 2.感受野会受到什么因素的影响？怎么影响？
    * 3.遥感图像语义分割和普通图像的语义分割有什么区别？
    * 4.语义分割中的样本不均衡介绍一下？
    * 5.双线性插值，转置卷积和反卷积的区别与联系 \* [todo]
    * 6.介绍语义分割、实例分割和全景分割 \* [todo]
    * 7.后处理方法：CRF \* [todo]
    * 8.介绍空洞卷积以及DeepLabv3中的ASPP模块 \* [todo]


* [5. Backbone](#5.Backbone) 
    * 1.resnet中的恒等快捷连接在前向传播和反向传播都有什么作用？
    * 2.ResNet和ResNeXt的区别 \* [todo]
    * 3.Inception中的deep supervision有什么作用 \* [todo]  
    * 4.resnet的shortcut结构有什么缺点?如何改进? \* [todo]    
    * 5.resnet的post activation有什么作用? \* [todo]  
    * 6.shufflenet的shuffle操作如何进行? \* [todo]  
    * 7.比较一下 Inception v1， v2，v3？

* [6. 卷积神经网络基础](#6.卷积神经网络基础)
    * 1.Batch Normalization 在卷积神经网络中的作用是什么?
    * 2.1* 1卷积的作用是什么？
    * 2.1. 深度可分离卷积介绍一下?
    * 3.两层较小的卷积核和一个较大的卷积核比较，各有什么缺点和优点？
    * 4.不同激活函数有什么区别？
    * 5.卷积层输出大小的计算?
    * 5.1.卷积层中计算量的计算：
    * 6.dropout层为什么可以促进正则化？pytorch中dropout在训练与测试时如何使用？
    * 7.平方误差损失函数和交叉熵损失函数分别适用于什么场景？
    * 8.梯度消失/爆炸的原因?
    * 9.损失降不下来怎么办？
    * 10.weight decay vs L2 正则项
    * 11.avarage-pooling与max-pooling的区别与联系？它们的梯度反传如何进行？
    * 12.各种normalization层了解多少？(包括SyncBN)
    * 13.为什么学习率的设置要与batchsize成线型关系
    * 14.ReLU有哪些改进的方式
    * 15.神经网络中参数中的偏置bias有什么作用
    * 16.caffe的im2col是怎么操作的？ \* [todo]
    * 17.转置卷积和反卷积的区别？
    * 18.什么是空洞卷积，它的感受野如何计算？ 给定 dialation rate 为 Drate 的卷积核，他的输出和输入大小的对应关系又是什么？


* [7. 神经网络训练场景问题](#7.神经网络训练场景问题)
    * 1.怎么判断过拟合，怎么处理？
    * 2.怎么解决图像语义分割中的样本不均衡问题?

* [8. Python](#8.Python)
    * 1.装饰器是什么，有什么作用？
    * 2.迭代器
    * 3.生成器
    * 4.深拷贝与浅拷贝的区别 \* [todo]
    * 5.Python中is和==的区别
    * 6.解释with语句
    * 7.什么是面向对象？面向过程和面向对象的区别？
    
* [9. 机器学习](#9.机器学习)
    * 1.讲讲支持向量机，间隔，对偶，核技巧，如何将分类问题转化成最优化问题的（手推公式）？
    * 2.手写逻辑回归的损失函数 \* [todo]
    * 3.简单介绍一下集成学习？
        * BAGGING
        * BOOSTING
        * GB
        * STACKING

* [10.传统图像处理](#10.传统图像处理)
    * 1.直方图均衡  
    * 2.直方图匹配  
    * 3.SIFT的特点  
    * 4.刚体变换，仿射变换，透视变换（投影变换）  
    * 5.索贝尔算子长什么样?为什么长这样?
    * 6.拉普拉斯边算子?  
    * 7.图像亮度、对比度、饱和度 
    * 8.高斯金字塔与拉普拉斯金字塔


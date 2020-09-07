import numpy as np

# 要点：
# 0. 多维数组broadcast注意维度匹配，keepdims 等操作
# 1. np 矩阵多维数组索引的语法，
def softmaxce(logits,label):
    """
    :param logits: (N,C)
    :param label: (N,1)
    :return: float
    """
    softmax = np.exp(logits)/np.sum(np.exp(logits),axis=1,keepdims=True)  # broadcast 需要维度相同，可拓展维度是1
    # print('softmax,softmax[label]',softmax)
    # print(softmax[range(label.shape[0]),label])   # np 索引二维数组使用两个长度相同的单行/列的数组获得里面对应位置的元素
    loss = -np.sum(np.log(softmax[np.array([i for i in range(label.shape[0])]),label]))  # 损失前面有-号，同时一般是自然对数为底
    return loss


# 要点：
# 0. 和交叉熵一样，在one-hot中只索引y=1的向量，代表对标签那一类的关注
# 1. 和为了平衡不同类别的样本，应当让alpha 在不同类别时有不同的数值
# 2. gamma 值是对不同logit 的索引，所以可以直接获得对应的结果

def focalloss(logits,label,alpha,gamma):
    #-alpha(1-logit)**gamma*log(logit)
    softmax = np.exp(logits)/np.sum(np.exp(logits),axis=1,keepdims=True)  # broadcast 需要维度相同，可拓展维度是1
    logits = softmax[range(label.shape[0]),label]
    weight = alpha[label]
    print(weight,logits.shape)

    return -np.sum(weight*((1-logits)**gamma)*np.log(logits))


dlogits = np.array([[0.1,0.1,8,1],
                    [1,2,4,1],
                    [2,4,1,3]])
dlabel = np.array([2,3,2])
# dlabel = np.expand_dims(dlabel,1)   # 拓展维度使用np.expand_dims
print(softmaxce(dlogits,dlabel))
print(focalloss(dlogits,dlabel,np.array([0.1,0.21,0.5,0.19]),2))
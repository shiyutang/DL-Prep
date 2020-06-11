from datetime import time

import matplotlib.pyplot as plt
import numpy as np
import torch
from torch import nn


def train_2d(trainer, steps=20):
    x1, x2 = -5, -2
    results = [(x1, x2)]
    for i in range(steps):
        x1, x2 = trainer(x1, x2)
        results.append((x1, x2))
    print('epoch %d, x1 %f, x2 %f' % (i + 1, x1, x2))
    return results


def show_trace_2d(f, results):
    plt.plot(*zip(*results), '-o', color='#ff7f0e')
    x1, x2 = np.meshgrid(np.arange(-5.5, 1.0, 0.1), np.arange(-3.0, 1.0, 0.1))
    plt.contour(x1, x2, f(x1, x2), colors='#1f77b4')
    plt.xlabel('x1')
    plt.ylabel('x2')


def show_trace(res, f, n=None):
    if n is None:
        n = max(abs(min(res)), abs(max(res)))
    f_line = np.arange(-n, n, 0.01)
    plt.plot(f_line, [f(x) for x in f_line], '-')
    plt.plot(res, [f(x) for x in res], '-o')
    plt.xlabel('x')
    plt.ylabel('f(x)')


def train_2d_momentum(trainer, steps=20):
    x1, x2 = -5, -2
    v1, v2 = 0, 0
    results = [(x1, x2)]
    for i in range(steps):
        x1, x2, v1, v2 = trainer(x1, x2, v1, v2)
        results.append((x1, x2))
    print('epoch %d, x1 %f, x2 %f' % (i + 1, x1, x2))
    return results


def train_pytorch_ch7(optimizer_fn, optimizer_hyperparams, features, labels,
                      batch_size=10, num_epochs=2):
    # 初始化模型
    net = nn.Sequential(
        nn.Linear(features.shape[-1], 1)
    )
    loss = nn.MSELoss()
    optimizer = optimizer_fn(net.parameters(), **optimizer_hyperparams)

    def eval_loss():
        return loss(net(features).view(-1), labels).item() / 2

    ls = [eval_loss()]
    data_iter = torch.utils.data.DataLoader(
        torch.utils.data.TensorDataset(features, labels), batch_size, shuffle=True)

    for _ in range(num_epochs):
        start = time.time()
        for batch_i, (X, y) in enumerate(data_iter):
            # 除以2是为了和train_ch7保持一致, 因为squared_loss中除了2
            l = loss(net(X).view(-1), y) / 2

            optimizer.zero_grad()
            l.backward()
            optimizer.step()
            if (batch_i + 1) * batch_size % 100 == 0:
                ls.append(eval_loss())
    # 打印结果和作图
    print('loss: %f, %f sec per epoch' % (ls[-1], time.time() - start))
    plt.plot(np.linspace(0, num_epochs, len(ls)), ls)
    plt.xlabel('epoch')
    plt.ylabel('loss')


## not yet validate
def train(train_iter, test_iter, net, loss, optimizer, device, num_epochs):
    ls = []
    for _ in range(num_epochs):
        start = time.time()
        for batch_i, (X, y) in enumerate(train_iter):
            X = X.to(device);
            y = y.to(device)
            l = loss(net(X).view(-1), y)

            optimizer.zero_grad()
            l.backward()
            optimizer.step()
        test_loss_epoch = 0
        for (X_test, y_test) in test_iter:
            X_test = X_test.to(device);
            y_test = y_test.to(device)
            l = loss(net(X_test).view(-1), y_test)
            test_loss_epoch += l
        test_loss_epoch /= len(test_iter)
        ls.append(test_loss_epoch)

        # 打印结果和作图
        print('loss: %f, %f sec per epoch' % (ls[-1], time.time() - start))
        plt.plot(np.linspace(0, num_epochs, len(ls)), ls)
        plt.xlabel('epoch')
        plt.ylabel('loss')

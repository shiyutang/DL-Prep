import math

import numpy as np


def focal_loss(logit, target, alpha, gamma):
    # logit: shape N C
    # target shape N
    p = logit[:][target]
    ret = sum((1 - p) ** gamma * alpha * math.log(p))
    return ret


lodit = np.array([[0, 1, 0, 1, 0, 5, 0, 4],
                  [0, 1, 0, 1, 0, 5, 0, 4],
                  [0, 1, 0, 1, 0, 5, 0, 4]])
target = np.array([1, 2, 3])

print(focal_loss(lodit, target, 0.4, 0.9))

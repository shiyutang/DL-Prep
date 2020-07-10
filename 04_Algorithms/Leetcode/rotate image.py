import cv2
import math
import numpy as np


class Img:
    def __init__(self, image, beta, center=[0, 0]):
        self.rows = src.shape[0]  # 原始图像的行数
        self.cols = src.shape[1]  # 原始图像的列数
        self.dst = np.zeros((self.rows, self.cols), dtype=np.uint8)
        # beta<0表示逆时针旋转；beta>0表示顺时针旋转
        self.transform = np.array([[math.cos(beta), -math.sin(beta), 0],
                                   [math.sin(beta), math.cos(beta), 0],
                                   [0, 0, 1]])
        self.src = image  # 原始图像
        self.center = center  # 旋转中心，默认是[0,0]

    def Process(self):
        for i in range(self.rows):
            for j in range(self.cols):
                src_pos = np.array([i - self.center[0], j - self.center[1], 1])
                [x, y, z] = np.dot(self.transform, src_pos)
                x = int(x) + self.center[0]
                y = int(y) + self.center[1]

                if x >= self.rows or y >= self.cols or x < 0 or y < 0:
                    self.dst[i][j] = 255
                else:
                    self.dst[i][j] = self.src[x][y]


if __name__ == '__main__':
    src = cv2.imread(r'../../03_DL_knowledge\Pics\VGG.png', 0)
    img = Img(src, beta=0.785398, center=[src.shape[0]//2,src.shape[1]//2])  # 以中心旋转弧度0.78，即0.78*180度
    img.Process()
    cv2.imshow('rotate', img.dst)
    cv2.waitKey(0)

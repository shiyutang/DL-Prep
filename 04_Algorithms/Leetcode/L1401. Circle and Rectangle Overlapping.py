import math


# 在圆的相对位置发生变化时，会导致相似三角形的边对应不对的问题。
class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        halfheight = (y2 - y1) / 2
        matcenter = ((x1 + x2) / 2, (y1 + y2) / 2)
        distance = math.sqrt((x_center - matcenter[0]) ** 2 + (y_center - matcenter[1]) ** 2)
        if y_center - matcenter[1] == 0:
            matdis = abs(matcenter[0] - x_center)
        else:
            matdis = (distance / abs(y_center - matcenter[1])) * halfheight
        return (distance - matdis) - radius < 0


# 划分区域方法： 根据圆心在矩形的不同相对位置，分别计算圆心到边的距离和判断矩形的角点是否在圆中
class Solution1:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # 条件 1：首先判断圆心是否在矩形内
        if x1 <= x_center <= x2 and y1 <= y_center <= y2:
            return True
        # 条件 2：圆心位于矩形的上下左右四个区域
        elif x_center > x2 and y1 <= y_center <= y2:  # 右
            return radius >= x_center - x2
        elif y_center < y1 and x1 <= x_center <= x2:  # 下
            return radius >= y1 - y_center
        elif x_center < x1 and y1 <= y_center <= y2:  # 左
            return radius >= x1 - x_center
        elif y_center > y2 and x1 <= x_center <= x2:  # 上
            return radius >= y_center - y2
        else:
            # 条件 3：判断矩形的四个顶点是否在圆的内部
            return min((x1 - x_center) ** 2 + (y2 - y_center) ** 2, \
                       (x2 - x_center) ** 2 + (y2 - y_center) ** 2, \
                       (x2 - x_center) ** 2 + (y1 - y_center) ** 2, \
                       (x1 - x_center) ** 2 + (y1 - y_center) ** 2) <= radius ** 2


sol = Solution1()
print(sol.checkOverlap(radius=1, x_center=0, y_center=0, x1=1, y1=-1, x2=3, y2=1))
print(sol.checkOverlap(radius=1, x_center=0, y_center=0, x1=-1, y1=0, x2=0, y2=1))
print(sol.checkOverlap(4, 102, 50, 0, 0, 100, 100))
print(sol.checkOverlap(1, 0, 3, 7, 3, 10, 6))
print(sol.checkOverlap(radius=1, x_center=1, y_center=1, x1=-3, y1=-3, x2=3, y2=3))
print(sol.checkOverlap(radius=1, x_center=1, y_center=1, x1=1, y1=-3, x2=2, y2=-1))

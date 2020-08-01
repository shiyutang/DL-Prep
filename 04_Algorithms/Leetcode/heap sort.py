def heap_sort(lst):
    def sift_down(start, end):
        """最大堆调整"""
        root = start
        while True:
            child = 2 * root + 1
            if child > end:  # 没有孩子
                break
            if child + 1 <= end and lst[child] < lst[child + 1]:  # 左孩子小于右孩子
                child += 1
            if lst[root] < lst[child]:  # 根小于孩子，那么交换并继续向下
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break

    # 从倒数第一层向上，查看是否满足最大堆性质，来创建最大堆
    for start in range((len(lst) - 2) // 2, -1, -1):
        sift_down(start, len(lst) - 1)

    # 每次交换最大和队尾元素，并维持堆进行堆排序
    for end in range(len(lst) - 1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        sift_down(0, end - 1)
    return lst


if __name__ == "__main__":
    l = [9, 2, 1, 7, 6, 8, 5, 3, 4]
    print(heap_sort(l))


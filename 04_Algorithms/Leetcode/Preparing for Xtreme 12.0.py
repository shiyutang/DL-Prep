# line = input().split(' ')
# topicDict,books,cnt = {},[],0
# while line != []:
#     books.append(line)
#     for topic in line[1:]:
#         if not topic in topicDict:
#             topicDict[topic] = [1,(cnt,line[0])]
#         else:
#             topicDict[topic].append[(cnt,line[0])]
#             topicDict[topic][0] += 1
#     line = input.split(' ')
#     cnt+=1
# print('topicDict,books',topicDict,books)

# definitBooks = []
# for topic in topicDict:
#     if topicDict[0] == 1:
#         definitBooks.append(topicDict[1])


# res = a + b
# print(res)

import math
import sys

def solve():
    topic_id = {}
    i = 0
    books = []
    line = input().split()
    while line!=[]:
        line = line
        time = int(line[0])
        topics = line[1:]
        for topic in topics:
            if topic not in topic_id.keys():
                topic_id[topic] = i
                i += 1
        bitmask = 0
        for topic in topics:
            bitmask |= 1 << topic_id[topic]
        books.append((time, bitmask))
        line = input().split()
        # print('line',line)
    print('books',books)

    subsets = 2**len(topic_id)
     # arr两行，一行保存之前流程中每个topic的最小值
     #（用于现在所有topic状态的更新），一行保存现在更新的最小值
    arr = [[sys.maxsize]*subsets for _ in range(2)]
    for i in range(2):
        arr[i][0] = 0
    for i in range(1, len(books)+1):
        time, bitmask = books[i-1]
        for j in range(1, subsets):
            prev = j & (~bitmask) # 这个状态需要的，新来的这本书也没有的topic，即需要从其他状态中找的topic
            # print j, prev
            if j == prev: # 没有需要从其他状态继承的topic
                arr[i&1][j] = arr[(i-1)&1][j]
            else:
                arr[i&1][j] = min(arr[(i-1)&1][j], time+arr[i&1][prev])
        print('arr after book {}'.format(books[i-1]),arr)

    print(arr[len(books)&1][-1])

# reflection：自己之前在想的时候都是想怎么通过一个流程把topic都填满，并且要求时间最少
# 但是topic填满是有一个状态转移的，每一本书都是一个用于状态转移的元素，且它有不同的代价
# 那么可以对于所有状态下，探索加入一本新书对于状态转移的影响，并在这个状态转移的过程中
# 寻找使得状态转移代价最小的步骤。那么关键点就是发现其实一直想找的topic的全集就是所有的状态数
# 而每一本新书就是状态转移的物料，目标则是寻找转移到最终状态后，我们的最小代价是什么。

def main():
    solve()

if __name__ == "__main__":
    main()
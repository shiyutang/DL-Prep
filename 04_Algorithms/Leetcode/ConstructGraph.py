# class edge:
#     def __init__(self,ID):
#         self.id = ID
#         self.to = None
#         self.nextID = None

adjMat = [[0,7,1000*100,5,1000*100,1000*100,1000*100],
          [1000*100,0,8,9,7,1000*100,1000*100],
          [1000*100,1000*100,0,1000*100,5,1000*100,1000*100],
          [1000*100,1000*100,1000*100,0,15,6,1000*100],
          [1000*100,1000*100,1000*100,1000*100,0,8,9],
          [1000*100,1000*100,1000*100,1000*100,1000*100,0,11],
          [1000*100,1000*100,1000*100,1000*100,1000*100,1000*100,0]]

LE = [-1]*len(adjMat)
edges = []
k = 0
for i in range(len(adjMat)):
    for weight in adjMat[i]:
        if weight >0 and weight<10*10:
            newedge = [k,-1,-1]
            newedge[1] = adjMat[i].index(weight)
            newedge[2] = LE[i]
            edges.append(newedge)
            LE[i] = k
            k += 1

print(LE)
print(edges)


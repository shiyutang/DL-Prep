import copy
class Solution:
	def isEscapePossible(self, blocked, source, target):
		if blocked == []:
			return True

		self.blocked,self.source,self.target = blocked,source,target
		# print('self.blocked,self.source,self.target',self.blocked,self.source,self.target)
		self.preprocess()
		# print('self.rows,self.cols',self.rows,self.cols)
		self.visited = [[False for _ in range(self.cols)] for pp in range(self.rows)]
		self.visited[self.source[0]][self.source[1]] = True
		self.path,self.find,self.stack = [self.source],False,[self.source]
		self.DFS()
		# print('self.path',self.path)
		return self.find

	def preprocess(self):
		rowblock,colblock = set([self.source[0],self.target[0]]),\
						set([self.source[1],self.target[1]])
		for item in self.blocked:
			rowblock.add(item[0])
			colblock.add(item[1])
		rowblock,colblock = sorted(list(rowblock)),sorted(list(colblock))
		# print('rowblock,colblock',rowblock,colblock)
		rowMap,colMap = {},{}
		for i in range(len(rowblock)):
			if i == 0:
				rowMap[rowblock[i]] = 0
			else:
				if rowblock[i] - rowblock[i-1] == 1:
					rowMap[rowblock[i]] = rowMap[rowblock[i-1]]+1
				else:
					rowMap[rowblock[i]] = rowMap[rowblock[i-1]]+2
			# print('i,rowMap',i,rowMap)

		for j in range(len(colblock)):
			if j == 0:
				colMap[colblock[j]] = 0
			else:
				if colblock[j] - colblock[j-1] == 1:
					colMap[colblock[j]] = colMap[colblock[j-1]]+1
				else:
					colMap[colblock[j]] = colMap[colblock[j-1]]+2
			# print('j,colMap',j,colMap)

		self.rows,self.cols = rowMap[rowblock[i]]+1,colMap[colblock[j]]+1
		# print('rowMap,colMap',rowMap,colMap,self.rows,self.cols)

		self.source,self.target = [rowMap[self.source[0]],colMap[self.source[1]]], \
								  [rowMap[self.target[0]],colMap[self.target[1]]]
		for i in range(len(self.blocked)):
			self.blocked[i] = [rowMap[self.blocked[i][0]],colMap[self.blocked[i][1]]]
		# print('self.source,self.target,self.blocked', self.source,self.target,self.blocked)


	def filterUtil(self,pos):
		return pos[0]>=0 and pos[0]< self.rows and \
		   pos[1]>=0 and pos[1]< self.cols and \
		   not pos in self.blocked and not self.visited[pos[0]][pos[1]]


	def DFS_recursive(self,pos):
		# print('pos',pos)
		self.visited[pos[0]][pos[1]] = True
		self.path.append(pos)
		available = filter(self.filterUtil,[[pos[0]-1,pos[1]],\
					[pos[0],pos[1]+1],[pos[0]+1,pos[1]],[pos[0],pos[1]-1]])
		# atmp = copy.deepcopy(available)
		# print('pos,available',pos,[item for item in atmp])
		for posi in available:
			# print('posi',posi)
			self.DFS_recursive(posi)
			if self.find:
				return
		# print('self.target',self.target)
		if pos == self.target:
			self.find = True
		else:
			self.path.pop(-1)
		return
	
	## 非递归DFS：取栈顶元素（不出栈），找到栈顶元素的一个未被访问过的邻接结点
	##（注意是一个就行，不需要所有邻接结点入栈，与BFS不同），
	## 访问、标记为已访问并入栈，直到栈顶元素的所有邻接结点都被访问过，
	## 栈顶元素出栈，直到栈空
	def DFS(self):
		# print('pos',pos)
		
		while self.stack:
			pos = self.stack[-1]
			available = filter(self.filterUtil,[[pos[0]-1,pos[1]],\
						[pos[0],pos[1]+1],[pos[0]+1,pos[1]],[pos[0],pos[1]-1]])
			# atmp = copy.deepcopy(available)
			# print('pos,available',pos,[item for item in atmp])
			if pos == self.target:
				self.find = True
				self.stack = []
				
			for posi in available:
				# print('posi',posi)
				self.path.append(posi)
				self.visited[posi[0]][posi[1]] = True
				self.stack.append(posi)
				break
			else:
				self.stack.pop()
				self.path.pop()
			# print('self.target',self.target)


sol = Solution()
# print(sol.isEscapePossible([[0,1],[1,0]],[0,0],[0,2])) # FALSE
# print(sol.isEscapePossible([],[0,0],[0,2])) # TRUE
# print(sol.isEscapePossible([[691938,300406],[710196,624190],[858790,609485],
# 	[268029,225806],[200010,188664],[132599,612099],[329444,633495],[196657,757958],
# 	[628509,883388]],
# 	[655988,180910],[267728,840949])) ## True 超时，需要改map
# print(sol.isEscapePossible([[345768,774229],[629817,136967],[409670,248157],[74349,779559],[414786,649526],[65010,348383],[356331,240766],[660411,476477],[644279,105302],[955741,329877],[429628,276130],[790163,499966],[268344,285645],[256763,589331],[43275,742978],[893783,82932],[554616,774196],[860429,627202],[34599,104279],[551144,965286],[255590,437156],[506004,846474],[458787,981145],[808869,39198],[462580,311927],[261777,988501],[376399,275522],[945969,704741],[851410,62469],[53829,925643],[920188,984203],[558061,829317],[543474,898023],[417456,498582],[102203,779821],[96249,249477],[647685,534966],[643349,816670],[153118,747744],[841398,816111],[648251,554700],[478323,794316],[674292,672543],[76294,264013],[15878,770881],[690636,64779],[557264,916577],[38537,534822],[749846,565998],[984737,868609],[710017,216223],[493472,150788],[583197,498605],[464755,490778],[877274,659348],[553709,704497],[386700,905174],[475971,294460],[795115,561143],[293008,639220],[781972,856578],[815890,34643],[463621,732482],[381547,953623],[750821,186506],[42145,690245],[864122,495406],[157150,169764],[255537,56968],[297520,190590],[52121,610868],[530122,285986],[638248,680915],[873026,567653],[44277,756684],[829329,182108],[256572,657671],[962390,645155],[614109,601008],[757843,760345],[743838,393018],[122862,556386],[300580,7641],[500402,503332],[856638,280327],[462667,670666],[481370,736448],[430350,967492],[472910,712645],[272494,923269],[511248,162205],[526472,27908],[12222,757392],[152920,609019],[538968,703338],[821698,547755],[420673,206206],[684938,929878],[634689,301472],[966108,557956],[174854,469098],[205701,649087],[957598,555768],[880695,85078],[526142,239404],[879305,22814],[820286,467626],[784437,897900],[637147,310429],[745305,506076],[8436,887537],[512054,789390],[25422,946262],[726324,590627],[315984,538436],[541724,890308],[296455,870833],[582428,321244],[90467,102620],[10247,644569],[298552,818310]]\
# ,[493823,803252]\
# ,[67475,651887])) ## True 爆栈
print(sol.isEscapePossible([[100005,100073],[100006,100074],[100007,100075],[100008,100076],[100009,100077],[100010,100078],[100011,100079],[100012,100080],[100013,100081],[100014,100082],[100015,100083],[100016,100084],[100017,100085],[100018,100086],[100019,100087],[100020,100088],[100021,100089],[100022,100090],[100023,100091],[100024,100092],[100025,100091],[100026,100090],[100027,100089],[100028,100088],[100029,100087],[100030,100086],[100031,100085],[100032,100084],[100033,100083],[100034,100082],[100035,100081],[100036,100080],[100037,100079],[100038,100078],[100039,100077],[100040,100076],[100041,100075],[100042,100074],[100043,100073],[100044,100072],[100043,100071],[100042,100070],[100041,100069],[100040,100068],[100039,100067],[100038,100066],[100037,100065],[100036,100064],[100035,100063],[100034,100062],[100033,100061],[100032,100060],[100031,100059],[100030,100058],[100029,100057],[100028,100056],[100027,100055],[100026,100054],[100025,100053],[100024,100052],[100023,100053],[100022,100054],[100021,100055],[100020,100056],[100019,100057],[100018,100058],[100017,100059],[100016,100060],[100015,100061],[100014,100062],[100013,100063],[100012,100064],[100011,100065],[100010,100066],[100009,100067],[100008,100068],[100007,100069],[100006,100070],[100005,100071]]\
,[100024,100072]
,[999994,999990]))


# import random 
# def test():
# 	start = [random.randint(1,1e6),random.randint(1,1e6)]
# 	end = [random.randint(1,1e6),random.randint(1,1e6)]
# 	numofBlock = random.randint(1,20)
# 	# print('numofBlock',numofBlock)
# 	blocked = []
# 	for i in range(numofBlock):
# 		blocked.append([random.randint(1,1e6),random.randint(1,1e6)])
# 	sol = Solution()
# 	# print(start,end,blocked)
# 	print(sol.isEscapePossible(blocked, start, end))

# test()


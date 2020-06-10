def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()
    data = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2]
    res = sol.hasGroupsSizeX(data)
    print(res)

    if random_samples:
        import random

        for _ in range(times):
            len1 = random.randint(0, 20)
            nums = []
            for __ in range(len1):
                num1 = random.randint(1, 3)
                nums.append(num1)
            print('the nums are', nums)
            res = sol.hasGroupsSizeX(data)
            print(res)


test(Solution, True)



# def ans(n,num,query):
#     for i in range(n):
#         for j in range(i+1,n):
#             if num[i]|num[j] == query:
#                 return True
#     return False

# num = int(input())
# element = input().split()
# num = []
# for i in range(len(element)):
#     num.append(int(element[i]))
# qnum = int(input())
# for i in range(qnum):
#     query = int(input())
#     res = ans(len(num),num,query)
#     if res:
#         print('YES')
#     else:
#         print('NO')


# a = [1,2,3,2,42,1]
# a.pop(-1)






# class Fruit(object):
# 	"""docstring for Fruit"""
# 	total = 0
# 	@staticmethod
# 	def print_total(cls):
# 		print(cls.total)
# 		print(Fruit.total)
# 		print(id(Fruit.total))
# 		print(id(cls.total))



# 	@classmethod
# 	def set(cls,value):
# 		cls.total = value

# class APPLE(Fruit):
# 	"""docstring for APPLE"""
# 	pass

# class Orange(Fruit):
# 	"""docstring for APPLE"""
# 	pass

# app = APPLE()
# app.set(100)
# ora = Orange()
# ora.set(239)
# app.print_total()
# ora.print_total()		
		
# from collections import Counter

# A = Counter('sefsgsdasdfa')
# print(A['A'])

# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield(3)
#     print('step 3')
#     yield(5)

# o = odd()
# next(o)
# next(o)
# next(o)

# def is_pa(n):
# 	n = str(n)
# 	if len(n) == 1:
# 		return True
# 	for i in range(len(n)//2):
# 		if not n[i]==n[-(i+1)]:
# 			return False
# 	return True

# def is_palindrome(n):
# 	return filter(is_pa, [k for k in range(1,n)])


# print(list(filter(is_pa, range(1, 200))))
# if list(filter(is_pa, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')

## itertools groupby
# import itertools
# result = '1113213211'

# for digit, group in itertools.groupby(result):
# 	print(digit,group)


# ## 闭包
# def print_msg():
#     # print_msg 是外围函数
#     msg = "zen of python"
#     def printer():
#         # printer 是嵌套函数
#         print(msg)
#     return printer

# another = print_msg()
# # 输出 zen of python
# another()

## logging 允许你指定记录信息的级别，
## 有debug，info，warning，error等几个级别

# import logging

# logging.basicConfig(level=logging.DEBUG)

# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)


# a= [[0,0,1,1,1,2,2,3,3,4],[2,3,4,4,2,1,3]]
# b = 'dadfFGREGFAGR'
# print(b[0:4])
# # [[1,2,3,4],
# #  [5,6,7,8],
# #  [9,10,11,12],
# #  [13,14,15,16]]
# # [[13, 9, 5, 1], 
# #  [14, 10, 6, 2],
# #  [15, 11, 7, 3], 
# #  [16, 12, 8, 4]]
# a = [[1,3],[2,6],[8,10],[15,18],[1,23]]
# s = sorted(a,key = lambda val: val[0])
# s = ["word","good","best","word"]
# s.sort()
# print(['bar', 'foo'] == ['bar', 'foo'])

# import itertools
# a = [1,2,3]
# a = map(str,a)
# for val in itertools.permutations(a,3):
# 	print(val)

# a = {}
# a[2] = 10
# a[3] = 100
# dictMerged = {100:2}
# dictMerged.update(dictMerged)
# print( dictMerged)

# a = iter([1,2,3])
# print(next(a))
# print(next(a))
# print(next(a))

# del a[1]
# a.extend([1,2,3])
# print(a)
# print("/a//b////c/d//././/..".split('/'))

# import math
# a = 7
# a *= 0 or 3

# import itertools
# for item in itertools.permutations([i for i in range(10)],10):
# 	print(item)

# import collections
# def minWindow( s, t):
#     need, missing = collections.Counter(t), len(t)
#     i = I = J = 0
#     for j, c in enumerate(s, 1):
#         missing -= need[c] > 0
#         need[c] -= 1
#         print('missing,need,i,c',missing,need,i,c)
#         if not missing:
#             while i < j and need[s[i]] < 0:
#                 need[s[i]] += 1
#                 i += 1
#             if not J or j - i <= J - I:
#                 I, J = i, j
#     return s[I:J]

# s = 'ADOBECODEBANC'
# t = 'ABC'

# print(minWindow(s,t))

# import itertools
# # string = 'bcfhupsnoyiwvk'
# # string = 'adegjlmqrtxz'
# # string = 'abcdefghijklmnopqrstuvwxyz'
# string = 'abcdefg'
# pool = ['h','he','li','be','b','c','n','o','f','ne','na','mg','al','si','p','s',
# 		'cl','ar','k','ca','sc','ti','v','cr','mn','fe','co','ni','cu','zn','ga',
# 		'ge','as','se','br','kr','rb','sr','y','zr','nb','mo','tc','ru','rh','pd',
# 		'ag','cd','ln','sn','sb','te','l','xe','cs','ba','hf','og','ta','w','re',
# 		'']
# for item in itertools.permutations(string,len(string)):
# 	print(''.join(item))
# 	res.append(''.join(item))

# print(res)

# print(53+6*9, 31 +11*8)
# a = [1,2,3,4,5]
# c = a.pop(0)
# print(a,c)


# # a = [[5,4],[6,4],[6,7],[2,3]]
# # x = sorted(a, key=lambda x: (x[0],x[1]))
# print([1,2]<[2,1])
# print([i for i in range(10000)])
res = 4
# for i in range(5,20):
# 	res = res^i
# res = res^23^24^25^26
# for j in range(30,39):
# 	res = res^j
# for i in range(5,39):
# 	res = res^i
# res =  res^20^21^22^27^28^29
# print(res)

# families = 10
# available = [j for j in range(families) if j != 3]
# print(available)

# visitF = list(map(str,input().strip().split()))
# visitF.sort()

# def gcd(a,b):
# 	while a!=0:
# 	  a,b = b%a,a
# 	return b
# #定义一个函数，参数分别为a,n，返回值为b
# def findModReverse(a,m):#这个扩展欧几里得算法求模逆
# 	if gcd(a,m)!=1:
# 	    return None
# 	u1,u2,u3 = 1,0,a
# 	v1,v2,v3 = 0,1,m
# 	while v3!=0:
# 	    q = u3//v3
# 	    v1,v2,v3,u1,u2,u3 = (u1-q*v1),(u2-q*v2),(u3-q*v3),v1,v2,v3
# 	return u1%m   # 逆元b

# a = 100
# b = findModReverse(a,10007)

# print(b)
# print(a*b%10007)

# import random 
# numofstr = random.randint(1,17)
# pool  = ['A','B','C','D']
# res = ''
# for I in range(numofstr):
# 	tmp = random.randint(0,3)
# 	res += pool[tmp]
# print(res)

# 6
# {"publications": [
# 				 {"publicationTitle" : "Letters on IEEEXtreme", 
# 				 "publicationNumber" : "1","articleCounts" : 
#                   [{"year" : "2017","articleCount" : "3"}, 
#                   {"year" : "2018","articleCount" : "6"}]},
                 
#                  {"publicationTitle" : "Journal of 24 hours programing", 
#                  "publicationNumber" : "2","articleCounts" : 
#                   [{"year" : "2017","articleCount" : "1"},
#                    {"year" : "2018","articleCount" : "4"}

#                  ]}]}

# {"publisher": "IEEE", 
#  "title": "Publication Title 1",
#  "contentType": "periodicals",
#  "ieeeCitationCount": "4",
#  "publicationNumber": "15",
#  "paperCitations": 
# 	{"ieee": [{"order": "1","articleNumber" : "41","publicationNumber" : "4","year" : "2018","title": "Article 41"},
# 			  # {"order": "2","articleNumber" : "109","publicationNumber" : "3","year" : "2015","title": "Article 109"},
# 			  {"order": "3","articleNumber" : "135","publicationNumber" : "1","year" : "2018","title": "Article 135"},
# 			  # {"order": "4","articleNumber" : "97","publicationNumber" : "1","year" : "2016","title": "Article 97"},
# 			  # {"order": "5","articleNumber" :"31","publicationNumber" : "1","year" : "2015","title": "Article 31"},
# 			  {"order": "6","articleNumber" : "89","publicationNumber" : "4","year" : "2018","title": "Article 89"},
# 			  {"order": "7","articleNumber" : "9","publicationNumber" : "4","year" : "2018","title": "Article 9"},
# 			  # {"order": "8","articleNumber" : "26","publicationNumber" : "1","year" : "2015","title": "Article 26"},
# 			  # {"order": "9","articleNumber" : "117","publicationNumber" : "1","year" : "2015","title": "Article 117"},
# 			  # {"order": "10","articleNumber" : "35","publicationNumber" : "2","year" : "2019","title": "Article 35"},
# 			  # {"order": "11","articleNumber" : "9","publicationNumber" : "2","year" : "2016","title": "Article 9"},
# 			  {"order": "12","articleNumber" : "61","publicationNumber" : "1","year" : "2017","title": "Article 61"},
# 			  # {"order": "13","articleNumber" : "75","publicationNumber" : "3","year" : "2019","title": "Article 75"},
# 			  # {"order": "14","articleNumber" : "25","publicationNumber" : "2","year" : "2019","title": "Article 25"},
# 			  # {"order": "15","articleNumber" : "56","publicationNumber" : "3","year" : "2016","title": "Article 56"}]}}

# {"publisher": "IEEE","title": "Publication Title 2","contentType": "periodicals","ieeeCitationCount": "2","publicationNumber": "28",
# 					"paperCitations": 
# 					{"ieee": [{"order": "1","articleNumber" : "14","publicationNumber" : "1","year" : "2018","title": "Article 14"},
# 					{"order": "2","articleNumber" : "105","publicationNumber" : "2","year" : "2017","title": "Article 105"},{"order": "3","articleNumber" : "130","publicationNumber" : "4","year" : "2017","title": "Article 130"},{"order": "4","articleNumber" : "61","publicationNumber" : "4","year" : "2019","title": "Article 61"},{"order": "5","articleNumber" : "115","publicationNumber" : "3","year" : "2015","title": "Article 115"},{"order": "6","articleNumber" : "84","publicationNumber" : "4","year" : "2015","title": "Article 84"},{"order": "7","articleNumber" : "57","publicationNumber" : "2","year" : "2018","title": "Article 57"},{"order": "8","articleNumber" : "96","publicationNumber" : "4","year" : "2019","title": "Article 96"},{"order": "9","articleNumber" : "9","publicationNumber" : "1","year" : "2017","title": "Article 9"},{"order": "10","articleNumber" : "67","publicationNumber" : "4","year" : "2018","title": "Article 67"},{"order": "11","articleNumber" : "114","publicationNumber" : "2","year" : "2016","title": "Article 114"},{"order": "12","articleNumber" : "59","publicationNumber" : "1","year" : "2015","title": "Article 59"},{"order": "13","articleNumber" : "118","publicationNumber" : "3","year" : "2015","title": "Article 118"},{"order": "14","articleNumber" : "61","publicationNumber" : "4","year" : "2016","title": "Article 61"},{"order": "15","articleNumber" : "79","publicationNumber" : "4","year" : "2017","title": "Article 79"},{"order": "16","articleNumber" : "83","publicationNumber" : "3","year" : "2018","title": "Article 83"},{"order": "17","articleNumber" : "24","publicationNumber" : "4","year" : "2016","title": "Article 24"},{"order": "18","articleNumber" : "48","publicationNumber" : "3","year" : "2015","title": "Article 48"},{"order": "19","articleNumber" : "11","publicationNumber" : "4","year" : "2019","title": "Article 11"},{"order": "20","articleNumber" : "125","publicationNumber" : "2","year" : "2019","title": "Article 125"},{"order": "21","articleNumber" : "64","publicationNumber" : "1","year" : "2016","title": "Article 64"},{"order": "22","articleNumber" : "25","publicationNumber" : "4","year" : "2016","title": "Article 25"},{"order": "23","articleNumber" : "27","publicationNumber" : "1","year" : "2015","title": "Article 27"},{"order": "24","articleNumber" : "100","publicationNumber" : "4","year" : "2019","title": "Article 100"},{"order": "25","articleNumber" : "108","publicationNumber" : "1","year" : "2018","title": "Article 108"},{"order": "26","articleNumber" : "82","publicationNumber" : "2","year" : "2017","title": "Article 82"},{"order": "27","articleNumber" : "22","publicationNumber" : "2","year" : "2016","title": "Article 22"},{"order": "28","articleNumber" : "113","publicationNumber" : "1","year" : "2015","title": "Article 113"}]}}
# {"publisher": "IEEE","title": "Publication Title 3","contentType": "periodicals","ieeeCitationCount": "4","publicationNumber": "23","paperCitations": {"ieee": [{"order": "1","articleNumber" : "75","publicationNumber" : "2","year" : "2016","title": "Article 75"},{"order": "2","articleNumber" :"88","publicationNumber" : "2","year" : "2018","title": "Article 88"},{"order": "3","articleNumber" : "12","publicationNumber" : "2","year" : "2016","title": "Article 12"},{"order": "4","articleNumber" : "90","publicationNumber" : "2","year" : "2015","title": "Article 90"},{"order": "5","articleNumber" : "126","publicationNumber" : "1","year" : "2017","title": "Article 126"},{"order": "6","articleNumber" : "12","publicationNumber" : "1","year" : "2018","title": "Article 12"},{"order": "7","articleNumber" : "7","publicationNumber" : "1","year" : "2017","title": "Article 7"},{"order": "8","articleNumber" : "49","publicationNumber" : "2","year" : "2015","title": "Article 49"},{"order": "9","articleNumber" : "54","publicationNumber" : "2","year" : "2019","title": "Article 54"},{"order": "10","articleNumber" : "133","publicationNumber" : "2","year" : "2019","title": "Article 133"},{"order": "11","articleNumber" : "3","publicationNumber" : "1","year" : "2017","title": "Article 3"},{"order": "12","articleNumber" : "23","publicationNumber" : "4","year" : "2015","title": "Article 23"},{"order": "13","articleNumber" : "5","publicationNumber" : "1","year" : "2016","title": "Article 5"},{"order": "14","articleNumber" : "8","publicationNumber" : "3","year" : "2019","title": "Article 8"},{"order": "15","articleNumber" : "1","publicationNumber" : "3","year" : "2016","title": "Article 1"},{"order": "16","articleNumber" : "129","publicationNumber" : "4","year" : "2019","title": "Article 129"},{"order": "17","articleNumber" : "57","publicationNumber" : "2","year" : "2019","title": "Article 57"},{"order": "18","articleNumber" : "106","publicationNumber" : "1","year" : "2016","title": "Article 106"},{"order": "19","articleNumber" : "67","publicationNumber" : "3","year" : "2015","title": "Article 67"},{"order": "20","articleNumber" : "42","publicationNumber" : "1","year" : "2019","title": "Article 42"},{"order": "21","articleNumber" : "14","publicationNumber" : "1","year" : "2015","title": "Article 14"},{"order": "22","articleNumber" : "76","publicationNumber" : "4","year" : "2018","title": "Article 76"},{"order": "23","articleNumber" : "134","publicationNumber" : "1","year" : "2016","title": "Article 134"}]}}
# {"publisher": "IEEE","title": "Publication Title 4","contentType": "periodicals","ieeeCitationCount": "1","publicationNumber": "21","paperCitations": {"ieee": [{"order": "1","articleNumber" : "126","publicationNumber" : "1","year" : "2015","title": "Article 126"},{"order": "2","articleNumber" : "35","publicationNumber" : "4","year" : "2017","title": "Article 35"},{"order": "3","articleNumber" : "7","publicationNumber" : "1","year" : "2016","title": "Article 7"},{"order": "4","articleNumber" : "116","publicationNumber" : "2","year" : "2018","title": "Article 116"},{"order": "5","articleNumber" : "58","publicationNumber" : "3","year" : "2015","title": "Article 58"},{"order": "6","articleNumber" : "24","publicationNumber" : "4","year" : "2018","title": "Article 24"},{"order": "7","articleNumber" : "136","publicationNumber" : "1","year" : "2015","title": "Article 136"},{"order": "8","articleNumber" : "29","publicationNumber" : "4","year" : "2019","title": "Article 29"},{"order": "9","articleNumber" : "118","publicationNumber" : "2","year" : "2015","title": "Article 118"},{"order": "10","articleNumber" : "102","publicationNumber" : "2","year" : "2015","title": "Article 102"},{"order": "11","articleNumber" : "41","publicationNumber" : "1","year" : "2019","title": "Article 41"},{"order": "12","articleNumber" : "87","publicationNumber" : "1","year" : "2017","title": "Article 87"},{"order": "13","articleNumber" : "61","publicationNumber" : "4","year" : "2019","title": "Article 61"},{"order": "14","articleNumber" : "91","publicationNumber" : "2","year" : "2017","title": "Article 91"},{"order": "15","articleNumber" : "88","publicationNumber" : "2","year" : "2015","title": "Article 88"},{"order": "16","articleNumber" : "83","publicationNumber" : "1","year" : "2019","title": "Article 83"},{"order": "17","articleNumber" : "103","publicationNumber" : "1","year" : "2017","title": "Article 103"},{"order": "18","articleNumber" : "107","publicationNumber" : "2","year" : "2015","title": "Article 107"},{"order": "19","articleNumber" : "81","publicationNumber" : "4","year" : "2016","title": "Article 81"},{"order": "20","articleNumber" :"76","publicationNumber" : "3","year" : "2018","title": "Article 76"},{"order": "21","articleNumber" : "31","publicationNumber" : "1","year" : "2017","title": "Article 31"}]}}
# {"publisher": "IEEE","title": "Publication Title 5","contentType": "periodicals","ieeeCitationCount": "2","publicationNumber": "15","paperCitations": {"ieee": [{"order": "1","articleNumber" : "28","publicationNumber" : "1","year" : "2017","title": "Article 28"},{"order": "2","articleNumber" : "1","publicationNumber" : "1","year" : "2018","title": "Article 1"},{"order": "3","articleNumber" : "109","publicationNumber" : "4","year" : "2018","title": "Article 109"},{"order": "4","articleNumber" : "82","publicationNumber" : "1","year" : "2016","title": "Article 82"},{"order": "5","articleNumber" : "83","publicationNumber" : "1","year" : "2017","title": "Article 83"},{"order": "6","articleNumber" : "136","publicationNumber" : "4","year" : "2018","title": "Article 136"},{"order": "7","articleNumber" : "36","publicationNumber" : "1","year" : "2018","title": "Article 36"},{"order": "8","articleNumber" : "83","publicationNumber" : "4","year" : "2015","title": "Article 83"},{"order": "9","articleNumber" : "132","publicationNumber" : "3","year" : "2018","title": "Article 132"},{"order": "10","articleNumber" : "83","publicationNumber" : "4","year" : "2016","title": "Article 83"},{"order": "11","articleNumber" : "51","publicationNumber" : "4","year" : "2015","title": "Article 51"},{"order": "12","articleNumber" : "37","publicationNumber" : "2","year" : "2015","title": "Article 37"},{"order": "13","articleNumber" : "112","publicationNumber" : "1","year" : "2016","title": "Article 112"},{"order": "14","articleNumber" : "16","publicationNumber" : "1","year" : "2015","title": "Article 16"},{"order": "15","articleNumber" : "2","publicationNumber" : "3","year" : "2019","title": "Article 2"}]}}


# a = 1.2
# print("%.2f" % a)

# a = input().split()
# print(len(a))
# a = input().split()
# print(len(a))
# print(a[0],a[1])

# n = 4
# # lookup = ['a','b','c','d']
# res = 0
# for j in range(100):
# 	res += 4**j
# 	print(res)

# print(int('000',2))
# import math
# print("math.log(10,2) : ", math.log(33,4))
# cnt,tmp = 0,7
# while tmp:
# 	print('tmp',tmp)
# 	if tmp%2 ==1:
# 		cnt+=1
# 	tmp = tmp>>1
# print(cnt)

A = list('AB')
B = list('C')
i = 0
while i < max(len(A),len(B)):
	if len(A)-1<i:
		print('A<B')
		break
	elif len(B)-1<i:
		print('A>B')
		break
	else:
		print('A[i],B[i]',A[i],B[i],A[i]>B[i])
		if A[i]>B[i]:
			print('A>B')
			break
		else:
			i += 1
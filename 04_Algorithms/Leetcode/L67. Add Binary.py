class Solution:
	def addBinary(self, a, b):
		res = []
		ca,remainA,remainB = 0,len(a),len(b)
		a,b = list(map(int,a)),list(map(int,b))
		while remainA>0 and remainB>0:
			tmp = a[remainA-1]+b[remainB-1]+ca
			if tmp >= 2:
				ca = 1
				tmp = tmp%2
			else:
				ca = 0
			remainA,remainB = remainA-1,remainB-1
			res.append(tmp)

		# print('res', res,remainA,remainB,ca)

		if ca == 1:
			if remainA>0 or remainB>0:
				remain = [remainA,remainB][remainB>0]
				print(remain)
				string = [a,b][remainB>0]
				while remain>0:
					tmp = string[remain-1]+ca
					if tmp >=2:
						ca =1
						tmp = tmp%2
					else:
						ca = 0

					remain -=1
					res.append(tmp)
					# print(res)
			if ca == 1:
				res.append(1)

			res = res[::-1]
			res = map(str,res)
			resstring = ''.join(res)
		else:
			res = res[::-1]
			res = map(str,res)
			if remainA>0 or remainB>0:
				remain = [remainA,remainB][remainB>0]
				string = [a,b][remainB>0]
				string = list(map(str,string))
				resstring = ''.join(string[:remain])+''.join(res)
			else:
				resstring = ''.join(res)

		return resstring


class Solution:
    def addBinary(self, a, b):
        if len(a)==0: return b
        if len(b)==0: return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[0:-1],b[0:-1])+'0'
        else:
            return self.addBinary(a[0:-1],b[0:-1])+'1'

sol = Solution()
print(sol.addBinary('1010','1011'))
print(sol.addBinary('101100','10111'))
print(sol.addBinary("101111","10")) #"110001"





        
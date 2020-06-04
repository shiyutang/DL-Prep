class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution:
# 	def mergeTwoLists(self, l1, l2):
# 		if l1 == None or l2 == None:
# 			if l1 == None and l2 == None
# 				return None
# 			elif l2 == None:
# 				return l1
# 			elif l1 ==None:
# 				return l2
# 		else:
# 			if l1.val<=l2.val:
# 				print('use l1 first')
# 				linkedList = ListNode(x =l1.val)
# 				l1 = l1.next
# 			else:
# 				print('use l2 first')
# 				linkedList = ListNode(x = l2.val)
# 				l2 = l2.next
		
# 		# while linkedList != None:
# 		# 	print(linkedList.val,'->',end = '')
# 		# 	linkedList = linkedList.next

# 		head = linkedList
# 		while l1 != None or l2 != None:
# 			if l1 != None and l2 != None:
# 				if l1.val<=l2.val:
# 					print('both here,use l1')
# 					linkedList.next = ListNode(l1.val)
# 					l1 = l1.next
# 					linkedList = linkedList.next
# 				else:
# 					print('both here,use l2')	
# 					linkedList.next = ListNode(l2.val)
# 					l2 = l2.next
# 					linkedList = linkedList.next
# 			elif l2 == None:
# 				print('l1 here,use l1')
# 				linkedList.next = l1
# 				l1 = None
# 			else:
# 				print('l2 here,use l2')
# 				linkedList.next = l2
# 				l2 = None
# 		return head


class Solution:
	'''do not initialize a node every time'''
	def mergeTwoLists(self, l1, l2):
		if l1 == None and l2 == None:
			return None
		else:
			linkedList = ListNode(0)
		
		head = linkedList
		while l1 != None or l2 != None:
			if l1 != None and l2 != None:
				if l1.val<=l2.val:
					print('both here,use l1')
					linkedList.next = l1
					l1 = l1.next
					linkedList = linkedList.next
				else:
					print('both here,use l2')	
					linkedList.next = l2
					l2 = l2.next
					linkedList = linkedList.next
			elif l2 == None:
				print('l1 here,use l1')
				linkedList.next = l1
				l1 = None
			else:
				print('l2 here,use l2')
				linkedList.next = l2
				l2 = None
		return head.next



sol = Solution()
a = ListNode(1);b = ListNode(2);c = ListNode(4);
d = ListNode(1);e = ListNode(3);f = ListNode(4);
a.next = b;b.next = c;c.next = None
d.next = e;e.next = f;f.next = None
l1 = a;l2 = d
# while l1 != None:
# 	print(l1.val,'->',end ='')
# 	l1 = l1.next

# 	print()
# while l2 != None:
# 	print(l2.val,'->',end = '')
# 	l2 = l2.next

res = sol.mergeTwoLists(l1,l2)
while res != None:
	print(res.val,'->',end ='')
	res = res.next

# time limit execed


class Solution:
    def robot(self, command, obstacles, x, y):
        collapse,reach = False,False
        i,pos = 0,[0,0]
        while not (collapse or reach):
        	commandnow = command[i]
        	if commandnow == 'U':
        		pos[1] += 1
        	elif commandnow == 'R':
        		pos[0] += 1

        	if pos[0] == x and pos[1] == y:
        		return True
        	elif pos in obstacles:
        		return False

        	i += 1
        	if i>= len(command):
        		i = 0


sol = Solution()
print(sol.robot(command = 'URR',obstacles = [[2,2]],x = 344,y = 234))






import random
import decimal

#
M=10
N=10
PROB =3
D =0.15

def makeGraph():
	list= [[0 for j in range(M)] for i in range(N)]
	for i in range(M):
		for j in range(N):
			if i ==j:
				continue
			elif random.randint(1,PROB) == PROB:
				list[i][j]=1
				list[j][i]=1
	return list


if __name__=="__main__":
	#Generates data set
	list = makeGraph()
	
	#Set link num
	link =[0 for i in range(M)]
	for i in range(M):
		link_num =0
		for j in list[i]:
			if j == 1:
				link_num=link_num+1
		link[i]=link_num
	
	#Prints link_num for debug
	print link
	
	#Initializes pagerank
	rank=[1 for i in range(M)]

	#Executes iteration
	for i in range(100):
		#Updates
		for j in range(M):
			r =0
			for k in range(M):
				if list[j][k] ==1:
					r +=rank[k]/link[k]
			rank[j]=round(D+(1.0 - D)*r,3)
		print rank





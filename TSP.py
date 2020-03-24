import random
import copy
def generate_initial_population(n):
	list1=[]
	new2=[]
	for i in range(0,200,1):
		a=[]
		j=0
		a=range(0,n)
		random.shuffle(a)
		list1.append(a)
	return list1

def ord_cross(li1,li2,n,ii,fi):
	count=[]
	a=[]
	sel=int(n/2)
	hsel=int(sel/2)
	while(ii<=fi):
		a.insert(ii,li2[ii])
		ii=ii+1
	count=[x for x in li1 if x not in a]
	m=0
	while(m<n):
		if (m<ii or m>fi) and (count!=[]):
			abc=count.pop(0)
			a.insert(m,abc)
		m=m+1
	return a

def get_best(temp,n,inputlist,div):
	sumarr=[]
	ilop=0
	div=int(div)
	while ilop<div:
		a=[]
		t=0
		s=0
		a=temp[ilop]
		j=0
		nm=n-1
		while j<nm:
			b=a[j]
			c=a[j+1]
			s=s+inputlist[b][c]
			j=j+1
		d=a[j-1]
		e=a[0]
		t=s+inputlist[d][e]
		sumarr.append(t)
		ilop=ilop+1
	sumindx=[]
	sumindx=sorted(range(len(sumarr)), key=lambda k: sumarr[k])
	list=[]
	indx=0
	while indx<div:
		ind=sumindx[indx]
		list.append(temp[ind])
		indx=indx+1
	listval=[]
	indx=0
	while indx<div:
		ind=sumindx[indx]
		listval.append(sumarr[ind])
		indx=indx+1
	return (list,listval)
def affect(slist,n,div,ii,fi):
	ap=0.6 * int(div)
	li=slist[0:12] #taking 12 best
	i=0
	while i<ap:
		li.append(ord_cross(li[i],li[i+1],n,ii,fi))
		i=i+2
	li.append(Global1)
	li.append(Global2)
	return li

def distribute(mainlist,n,dp,div,k):
	i=0
	Hlist=[]
	Llist=[]
	div=int(div)
	k=int(k)
	dprob=dp*div
	dprob=int(dprob)
	while i<k:
		li1=mainlist[i]
		Hlist.append(li1[0:dprob])
		Llist.append(li1[dprob:div])
		i=i+1
	j=0
	dlist=[]
	while j<k-1:
		temp1=[]
		temp2=[]
		temp3=[]
		temp1=Hlist[j]
		temp2=Llist[j+1]
		temp3=temp1+temp2
		dlist.append(temp3)
		j=j+1
	temp1=[]
	temp2=[]
	temp3=[]
	temp1=Hlist[j]
	temp2=Llist[0]
	temp3=temp1+temp2
	dlist.append(temp3)
	return dlist
	
def swapp(a,b):
	temp=0
	temp=a
	a=b
	b=temp
	return a,b

def sorted_matrix(inputlist,n):
	i=0
	sortedinput=[]
	subinput=[]
	while i<n:
		subinput=inputlist[i]
		subinput=sorted(subinput)
		sortedinput.append(subinput)
		i=i+1
	average(sortedinput,n)
	return sortedinput
		
def average(inputlist,n):
	i=0
	j=0
	sum=0
	fsum=0
	while i<n:
		while j<n:
			sum=sum+inputlist[i][j]
			j=j+1
		asum=sum/n
		fsum=fsum+asum
		i=i+1
	ave=fsum/n #average distance betwaeen any two node
	i=0
	sum=0
	fsum=0
	while i<n:
		sum=sum+inputlist[i][1]
		asum=sum/n
		fsum=fsum+asum
		i=i+1
	min=fsum/n
	i=0
	sum=0
	fsum=0
	while i<n:
		sum=sum+inputlist[i][n-1]
		asum=sum/n
		fsum=fsum+asum
		i=i+1
	max=fsum/n
	print "-----------------------------------------------------------------------"
	print "Average distance between any two distinct node : ",ave
	print "Average Minimum Possible distance between any two distinct node : ",min
	print "Average Maximum Possible distance between any two distinct node : ",max
	print "-----------------------------------------------------------------------"
	print "Average Tour length :",ave*n
	print "Minimum Average Tour length :",min*n
	print "Maximum Tour length :",max*n
	
	print "-------------------------------------------------------------------------"
	
	print "-------------------------------------------------------------------------"
	
	
		

def main():
	inputlist=[]
	f = open("H:/48inp.txt","r")
	inputlist=[[int(i) for i in line.split()] for line in f] #reading 26 cities tsp data
	n=len(inputlist)
	print n," Cities TSP : \n"
	
	sorted_matrix(inputlist,n)

	listpop=[]
	listpop =generate_initial_population(n) #100 initial population are generated

	#dividing 100 population into 5 local list
	nop=200
	div=20
	k=nop/div
	i=0
	ilist=[]
	while(i<nop):
		ilist.insert((i/div),listpop[i:i+div])
		i=i+div

	#getting the sorted list and the sorted value
	slcombo=[]
	svcombo=[]
	i2=0
	while(i2<k):
		sortedlist,sortedvalue=get_best(ilist[i2],n,inputlist,div)
		slcombo.append(sortedlist)
		svcombo.append(sortedvalue)
		global Global1
		Global1=sortedlist[0]
		global Global2
		Global2=sortedlist[1]
		i2=i2+1
	
	alist1=[]
	alist=[]
	i3=0
	# get the affected list
	"""The affected list means the list where 
	60% of the top population of sorted_list_combo + ordered crossover performed 
	over those 60% top-population + two global best """
	print "Enter the starting and last index for performing ordered crossover"
	ii=input()
	fi=input()
	while(i3<k):
		alist1=affect(slcombo[i3],n,div,ii,fi)
		alist.append(alist1)
		i3=i3+1
	
	#distribute the affected list 
	""" the last ten population of the 
	next affected list is popped out and added to their respective 
	index in the present affected list and so on....  """ 
	print "Enter the distribution probability"
	dp=input()
	dlist=distribute(alist,n,dp,div,k)
	i2=0
	while(i2<k):
		sortedlist,sortedvalue=get_best(dlist[i2],n,inputlist,div)
		slcombo.append(sortedlist)
		svcombo.append(sortedvalue)
		i2=i2+1
	loop=0
	print "How many populations do you want to perform swapping over?"
	swapPPL=input()
	inner=0
	print "How many pair of index do you want to swap?"
	swa=input()
	swa=int(swa)
	swa2=swa*2
	print "Enter the index you want to swap?"
	swapindx=[]
	while inner<swa2:
		swapindx.append(input())
		inner=inner+1
	print "No. of iterations?"
	iter=input()
	while loop<iter:
		alist1=[]
		alist=[]
		ALIST=[]
		i3=0
		while(i3<k):
			alist1=affect(slcombo[i3],n,div,ii,fi)
			ALIST=ALIST+alist1
			alist.append(alist1)
			i3=i3+1
		
		
		inner=0
		while inner<swapPPL:# only for 48 cities tsp
		# hard coding used for swapping two elements of the population
			lp=0
			lpi=0
			while lp<swa:
				ALIST[inner][swapindx[lpi]],ALIST[inner][swapindx[lpi+1]]=swapp(ALIST[inner][swapindx[lpi]],ALIST[inner][swapindx[lpi+1]])
				lpi=lpi+2
				lp=lp+1
			inner=inner+1
		i2=0
		while(i2<k):
			sortedlist,sortedvalue=get_best(alist[i2],n,inputlist,div)
			slcombo.append(sortedlist)
			svcombo.append(sortedvalue)
			i2=i2+1
		loop=loop+1
	print "----------------------------------------------------"
	print "----------------------------------------------------"
	print "Minimum Tour Path By Proposed Alogorithm :"
	print slcombo[0][0] #Best Path
	print "-----------------"
	
	print "Minimum Tour length By Proposed Alogorithm :"
	print svcombo[0][0] #Shortest distance
	
if __name__ == '__main__':
	main()

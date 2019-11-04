n=int(input()) #taking input from user
c1=1
c2=1
val1=[]
val2=[]
p=1
ext=n
#printing pattern
while(ext>0):
	val2=[]
	val1=[]
	q=((ext*ext)+p)
	if(n-ext>0):
		a=2*(n-ext)
		for i in range(a):
			val1.append('*')
	while(c1<ext+1):
		val2.append(p)
		p+=1
		c1+=1
 
	while(c2<ext+1):
		val2.append(q)
		q+=1
		c2+=1
 
	print(*val1, sep='',end='')	
	print(*val2, sep='0',end='\n')	
	ext-=1
	c1=1
	c2=1
